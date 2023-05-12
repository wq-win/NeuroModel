import brainpy as bp
import brainpy.math as bm
import matplotlib.pyplot as plt

bm.set_platform('cpu')


@bp.odeint(method='rk4', dt=0.01)
def LIF(V, t, I, EL, GL, C):
    dVdt = (-GL * (V - EL) + I) / C
    # if -50 < V < 0:
    #     V = 30
    # elif V > 0:
    #     v = -60
    print('hh')
    return dVdt


I = 0.9
EL = -70
GL = 0.025
C = 0.5

runner = bp.IntegratorRunner(
    LIF,
    monitors=list('V'),
    inits=[-70.],
    args=dict(I=I,EL=EL,GL=GL,C=C),
    dt=0.01
)

runner.run(100.)

plt.plot(runner.mon.ts, runner.mon.V,label='V')
plt.legend()
plt.show()