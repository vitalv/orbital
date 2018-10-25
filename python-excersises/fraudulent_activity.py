import numpy as np 

data = open('input0.txt').readlines()
n, d = int(data[0].split()[0]), int(data[0].split()[1])
t = [int(n) for n in data[1].split()]


#find d+1 position in list 

dix = d-1 #find preceding number for day d
t[dix::-1][0:d] #find the preciding d numbers from dix
#and continue with following days
t[dix+1::-1][0:d]

#do this until last element in list


for i in range(d-1, len(t)-1):
	m = np.median(t[i::-1][0:d])
	c = t[i+1]
	if c >= 2*m:
		print("Slow down with the credit card!")

#fancy one-liner:
[t[i+1] for i in range(d-1, len(t)-1) if t[i+1] >= 2*(np.median(t[i::-1][0:d]))]

