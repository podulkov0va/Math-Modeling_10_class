print('---------------------------------1---------------')
from phconst import g
from math import tan, cos, pi
h=100
B=30
A=pi/3
V=( (g*h*tan(B)**2 ) / (2 * cos(A)**2 * (1-tan(B)*tan(A) )))**0.5
print(V)
print('--------------------------2-----------')
from phconst import e,k,pl
from math import pi
T=200
n=300
N=2/pi**(0.5) * pl/(k*T)**(3/2) * n**(-n/k*T) * e**(T/2)
print (N)