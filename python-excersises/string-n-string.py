'''
We have a string s
We have a number n

Create a function string_n_string(s, n) that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars to the back and return the result of the string after applying the function to it n times.

Examples:

string_n_string("Wow Example!", 1)
> "WwEapeo xml!

string_n_string("qwertyuio",2)
> "qtorieuwy

'''

#('').join([('').join([i for i in s if s.index(i)%2==0]), ('').join([i for i in s if s.index(i)%2!=0]) ])

def concatenate(s):
	even, odd = [], []
	for i in range(len(s)):
		if i%2==0:
			even.append(s[i])
		else:
			odd.append(s[i])
	even = ('').join(even)
	odd  = ('').join(odd)
	return ('').join( [ even , odd ] )



def string_n_string(s, n):
	for i in range(n):
		s = string_n_string(concatenate(s), n-1)
		break # I don't want a second level of inception
	return s




def string_n_string(s, n):
	for i in range(n):
		s = concatenate(s)
		#s = ('').join([('').join([i for i in s if s.index(i)%2==0]), ('').join([i for i in s if s.index(i)%2!=0]) ])
	return s



self.assertEquals(string_n_string("better example", 2), "bexltept merae")


string_n_string("Greetings", 8)



def find_indices_of(char, in_string):
    index = -1
    while True:
        index = in_string.find(char, index + 1)
        if index == -1:
            break
        yield index
