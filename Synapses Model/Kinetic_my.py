import numpy as np
from matplotlib import pyplot as plt


class Kinetic:
    def __init__(self, alpha, tau, is_saturation):
        self.alpha = alpha  # control the amplitude of spike rise
        self.tau = tau  # control the spike decay speed. The smaller, the faster.
        self.dt = 0.001  # decay the spike
        self.is_s = is_saturation  # saturation term

    def calculate_next_s(self, s, r):
        if self.is_s:
            s = s + self.alpha * r * (1 - s) - self.dt * s / self.tau
        else:
            s = s + self.alpha * r - self.dt * s / self.tau
        return s


# parameter
dt = 0.001
t_start = 0
t_end = 1
times = np.arange(t_start, t_end, dt)

# initialize Object
Kinetic1 = Kinetic(1, 0.25, False)
Kinetic2 = Kinetic(0.5, 0.25, True)
Kinetic3 = Kinetic(0.5, 0.025, True)

# init state
base_unit = np.append(np.zeros(99), 1)  # Input a spike every 100 times.
n_repeat = 10
s_input = np.tile(base_unit, int(n_repeat))

s_state1 = s_input * 0
s_state2 = s_input * 0
s_state3 = s_input * 0

ind = 0
for r in s_input[0:-1]:
    s_state1[ind + 1] = Kinetic1.calculate_next_s(s_state1[ind], r)
    s_state2[ind + 1] = Kinetic2.calculate_next_s(s_state2[ind], r)
    s_state3[ind + 1] = Kinetic3.calculate_next_s(s_state3[ind], r)
    ind += 1

plt.figure()
plt.plot(times, s_state1, label='tau=0.25,no saturation term')
plt.plot(times, s_state2, label='tau=0.25, saturation term')
plt.plot(times, s_state3, label='tau=0.025, saturation term')
plt.xlabel('time (ms)')
plt.ylabel('s')
plt.legend()
plt.show()
