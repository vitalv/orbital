l0 = [27, -12, 66, 79, 14, 1, 92, 40]
l0 = sorted(l0)

l1 = [963, 1405, 1301, 950, 1028, 391, -12, 326, 222, 1249, 1067, 170, 937, 911, 664, 651, 300, 1327, 14, 1171, 105, 274, 417, 1340, 547, 378, 53, 807, 1158, 638, 1197, 248, 1379, 586, 1054, 794, 352, 404, 625, 209, 1106, 235, 1132, 1041, 456, 469, 573, 183, 924, 1457, 1353, 1002, 755, 872, 118, 1314, 716, 1093, 1431, 729, 898, 885, 677, 430, 1262, 1366, 1015, 742, 1236, 495, 534, 131, 313, 1184, 261, 976, 1418, 40, 1288, 1496, 703, 27, 820, 1275, 287, 79, 859, 1223, 157, 781, 1080, 144, 599, 1392, 989, 339, 768, 66, 1483, 1145, 508, 521, 1444, 1470, 1119, 92, 482, 365, 1210, 443, 612, 833, 1, 560, 846, 690 ]


#first find the 'step' by comparing step from 0 to 1 and -1 to -2
#if the steps don't match then 2nd or 2nd-to-last elements is the missing one

if abs(l[0]-l[1]) == abs(l[-1]-l[-2]):
	step = abs(l[0]-l[1])


#itertools.tee(iterable, n=2)
#Return n independent iterators from a single iterable.
#next(iterator, default)
#default (optional) - this value is returned if the iterator is exhausted (no items left)

from itertools import tee
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#look at all the difference between the elements pairwise:
def find_missing(l)
	diff = []
	for i in pairwise(l1): 
		diff.append(abs(i[0]-i[1]))
	step = [i for i in diff if diff.count(i) > 1][0]
	missed_step = [i for i in diff if diff.count(i) == 1][0]
	l[diff.index(missed_step)]+step
