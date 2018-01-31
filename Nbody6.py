from __future__ import division
from argparse import ArgumentParser
import scipy.constants as C
import visual as v
import numpy as np

# This version is for visual 6.11

SF = 1e-6
G = C.G * SF ** 3
DT = 3600 * 24
RATE = 50000

scene = v.display(title="Solar System variations", x=0, y=0, z=0,
                  width=600, height=600, range=1000e3,
                  background=v.color.black, center=v.vector(0, 0, 0),
                  forward=(0, -0.3, -1))


class Body(v.sphere):
    def __init__(self, mass, pos, vel, i, *arg, **kwargs):
        super(Body, self).__init__(*arg, **kwargs)
        self.vel = v.vector(vel)
        self.pos = v.vector(pos)
        self.mass = mass
        self.id = i

    def c_pos(self, obj, dt=DT):
        xm = self.pos + 0.5 * dt * self.vel
        self.vel = self.vel + dt * self.c_acel(xm, obj)
        self.pos = xm + 0.5 * dt * self.vel

    def c_acel(self, xm, obj):
        acel = v.vector(0, 0, 0)
        for i in obj:
            if i.id != self.id:
                acel += (i.mass * (v.norm(i.pos - xm) * G) /
                         (v.mag(i.pos - xm) ** 2))
        return acel


def generate(file):
    date = np.loadtxt(file, dtype='float')
    obj = []
    for i in date:
        obj.append(Body(i[0], i[1:4], i[4:], len(obj), color=(1, 0, 0),
                        radius=30, make_trail=True, trail_type="points",
                        interval=50, retain=1000))
        obj[len(obj) - 1].trail_object.size = 1
    return obj


parser = ArgumentParser(prog='N-Body', description='This program make the \
                        simulation of N-Body')
parser.add_argument('-f', '--INPUT', help='File of intput')
parser.add_argument('-sf', '--SCALE_FACTOR', help='Factor of scale for the \
                    simulation', type=float)
parser.add_argument('-dt', '--INCRASE', help='Incrase of the time', type=float)
parser.add_argument('-r', '--RATE', help='Velocity of simulation', type=float)
args = parser.parse_args()

if args.SCALE_FACTOR:
    SF = args.SCALE_FACTOR
if args.INCRASE:
    DT = args.INCRASE
if args.INPUT:
    obj = generate(args.INPUT)
if args.RATE:
    RATE = args.RATE
else:
    obj = generate('SSone.ap')
while True:
    for i in obj:
        i.c_pos(obj, dt=DT)
    v.rate(RATE)
