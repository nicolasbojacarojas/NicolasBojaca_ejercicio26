import numpy as np
import matplotlib.pyplot as plt
vi = 35
vf =45
thei = 0
thef = np.pi/2
v0 = np.random.uniform(vi, vf, 1000000)
the0 = np.random.uniform(thei, thef, 1000000)
g = 9.98
d1 = 61
d2 = 115
d3 = 31
d4 = 177
pv0 = 1/(vf-vi)
pthe0 = 1/(thef-thei)
def fun(the0, v0, g):
	return (v0**2*np.sin(2*the0))/g, v0
def distancias(d, df, v0):
	x  = (df > (d-5)) & (df < (d+5))
	return df[x], v0[x]
df, v1 = fun(the0,v0, g)
dn1, v01 = distancias(d1, df, v1)
dn2, v02= distancias(d2, df, v1)
dn3, v03 = distancias(d3, df, v1)
dn4, v04 = distancias(d4, df, v1)
plt.hist(v01, normed = 1, label = 'distancia 61')
plt.hist(v02, normed = 1, label = 'ditancia 115')
plt.hist(v03, normed = 1, label = 'ditancia 31')
plt.hist(v04, normed = 1, label = 'ditancia 177')
plt.xlabel("velocidades")
plt.ylabel("probabilidad de velocidades")
plt.legend(loc=0)
plt.savefig("histograma")
		
