import numpy as np 

def read_data(filename):
	data = open(filename).readlines()
	n, d = int(data[0].split()[0]), int(data[0].split()[1])
	t = [int(n) for n in data[1].split()]
	return n, d, t


n,d,t = read_data('input0.txt')


def count_notifications(filename):
    n,d,t = read_data(filename)
    return len([t[i+1] for i in range(d-1, len(t)-1) if t[i+1] >= 2*(np.median(t[i::-1][0:d]))])



#Longer but also more readable solution:
def count_notifications_2(filename):
	n,d,t = read_data(filename)
	notifications=0
	for i in range(d-1, len(t)-1):
		m = np.median(t[i::-1][0:d])
		print("\nMedian preceding %d days: %d"%(d, m))
		c = t[i+1]
		print("Expenses current day: %d"%c)
		if c >= 2*m:
			print("Slow down with the credit card!")
			notifications+=1
	return notifications


