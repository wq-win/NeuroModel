import numpy as np
from matplotlib import pyplot as plt


def rk4(h, y, inputs, f):
    '''
    用于数值积分的rk4函数。
    args:
        h - 步长
        y - 当前状态量
        inputs - 外界对系统的输入
        f - 常微分或偏微分方程
    return:
        y_new - 新的状态量,即经过h时间之后的状态量
    '''
    k1 = f(y, inputs)
    k2 = f(y + h / 2 * k1, inputs)
    k3 = f(y + h / 2 * k2, inputs)
    k4 = f(y + h * k3, inputs)

    y_new = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_new


class LIF_rk4:
    def __init__(self, I):
        self.GL = 0.025
        self.EL = -70
        self.I = I
        self.C = 0.5
        # v_peak > v_threshold
        self.v_peak = 30
        self.v_reset = -60
        self.v_threshold = -50
        self.v_refractory_time = 0
        self.refractory_time = 400

    def derivative(self, v, inputs=0):
        Dv = (-self.GL * (v - self.EL) + self.I) / self.C
        return Dv

    def step(self, v, dt, inputs=0):
        v_new = rk4(dt, v, inputs, self.derivative)
        if self.v_threshold < v_new < 0:
            v_new = self.v_peak
        elif v_new > 0:
            v_new = self.v_reset
            self.v_refractory_time = self.v_refractory_time * 0 + self.refractory_time
        elif self.v_refractory_time > 0:
            v_new = self.v_reset
            self.v_refractory_time = self.v_refractory_time - 1

        return v_new


# parameter
dt = 0.001
t_start = 0
t_end = 200
times = np.arange(t_start, t_end, dt)


def I_with_plt(I):
    # Initialize Object
    LIF = LIF_rk4(I)
    v = -70  # init state
    v_state = []
    # ODE
    for t in times:
        v_state.append(v)
        v = LIF.step(v, dt)
    return v_state


v_state_2 = I_with_plt(0.2)
v_state_4 = I_with_plt(0.4)
v_state_6 = I_with_plt(0.6)
v_state_8 = I_with_plt(0.8)

plt.figure()
plt.plot(times, v_state_2, label='v2')
plt.plot(times, v_state_4, label='v4')
plt.plot(times, v_state_6, label='v6')
plt.plot(times, v_state_8, label='v8')
plt.xlabel('time (ms)')
plt.ylabel('V (mv)')
plt.legend()
plt.show()
