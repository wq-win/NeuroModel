import numpy as np
from matplotlib import pyplot as plt


def calc_next_step_synaptic_kinetic(s,in1,tau,step):
    alphs_s = .5
    tau = tau/2000 #convert to s
    s = s + alphs_s*in1*(1-s) - step*s/tau
    return s

def calc_next_step_synaptic_simple(s,in1,tau,step):
    alphs_s = 1
    tau = tau/2000 #convert to s
    s = s + alphs_s*in1 - step*s/tau
    return s

def generate_spike_train(step,length,freq):
    T = 1/freq
    base_unit = np.append(np.zeros(-1 + int(T/step)),1)
    n_repeat = np.ceil(length/T)
    train = np.tile(base_unit,int(n_repeat))
    train = train[0:int(length/step)]
    return train

# simulate spike train
step_t = 0.001
freq = 10
duration = 1
tau = 500
train = generate_spike_train(step = step_t,length = duration,freq = freq)
s_timeseris = train*0
t = np.arange(0,1,step_t)

ind = 0
for ii in train[0:-1]:
    s_timeseris[ind+1] = calc_next_step_synaptic_kinetic(s = s_timeseris[ind],in1 = ii, tau = tau, step = step_t)
    ind+=1
plt.plot(t,s_timeseris,label = "tau=500ms, no saturation term")

ind = 0
for ii in train[0:-1]:
    s_timeseris[ind+1] = calc_next_step_synaptic_simple(s = s_timeseris[ind],in1 = ii, tau = tau, step = step_t)
    ind+=1
plt.plot(t,s_timeseris,label = "tau=500ms, kinetic model")

ind = 0
tau = 50
for ii in train[0:-1]:
    s_timeseris[ind+1] = calc_next_step_synaptic_kinetic(s = s_timeseris[ind],in1 = ii, tau = tau, step = step_t)
    ind+=1
plt.plot(t,s_timeseris,label = "tau=50ms, kinetic model")
plt.legend(loc='upper left', fontsize=10)
plt.xlabel("time /s")
plt.ylabel("s")
plt.show()