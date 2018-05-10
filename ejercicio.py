import numpy as np
import matplotlib.pyplot as plt
vi = 35
vf =45
thei = 0
thef = np.pi/2
v0 = np.random.uniform(vi, vf, 1000)
the0 = np.random.uniform(thei, thef, 1000)
g = 9.98
d1 = 61
d2 = 115
d3 = 31
d4 = 177
pv0 = 1/(vf-vi)
pthe0 = 1/(thef-thei)
def fun(the0, v0, g):
	return (v0**2*np.sin(2*the0))/g
def distancias(d, df):
	x  = (df > (d-5)) & (df < (d+5))
	return df[x]
df = fun(the0,v0, g)
dn1 = distancias(d1, df)
dn2 = distancias(d2, df)
dn3 = distancias(d3, df)
dn4 = distancias(d4, df)

		
