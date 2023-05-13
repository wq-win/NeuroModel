import numpy as np
from matplotlib import pyplot as plt


class Kick:
    def __init__(self, J):
        self.EL = -70  # membrane potential
        self.J = J  # weight
        self.C = 0.5  # capacitance
        self.tau = 2

    def theta(self, t):
        if t.all() < 0:
            return 0
        if t.all() > 0:
            return 1

    def v_t(self, t):
        theta = self.theta(t)
        v = self.EL + self.J * np.exp(- t / self.tau) * theta / self.C
        return v


# parameter
dt = 0.1
t_start = 1
t_end = 20
times = np.arange(t_start, t_end, dt)

# Initialize Object
Kick = Kick(1)
v = Kick.v_t(times)
# ODE
# for t in times:
#     v_state.append(v)
#     v = LIF.step(v, dt)

plt.figure()
plt.plot(times, v, label='v')
plt.xlabel('time (ms)')
plt.ylabel('V (mv)')
plt.legend()
plt.show()
