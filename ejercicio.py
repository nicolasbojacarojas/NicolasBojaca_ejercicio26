import numpy as np
import matplotlib.pyplot as plt
vi = 35
vf =45
thei = 0
thef = np.pi/2
v0 = np.random.uniform(vi, vf, 1000)
the0 = np.random.uniform(thei, thef, 1000)
g = 9.98
d = 61
pv0 = 1/(vf-vi)
pthe0 = 1/(thef-thei)
def fun(the0, v0, g):
	return (v0**2*np.sin(2*the0))/g
def distancias(d, df):
	for i in range(len(df)):
		if (df[i]>(d+5) and df[i]<(d-5)):
			df.remove(i)
	return df
df = fun(the0,v0, g)
dn = distancias(d, df)
s

		
