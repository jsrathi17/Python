import math

def bisection(a,b):
	if function(a) ==0:
		return a

	elif function(b) ==0:
		return b

	elif function(a) * function(b) > 0:
		return "Roots are out of scope"

	else:
		root = (a+b)/2

		while abs(function(root)) > 0.005:
			
			if function(a) * function(root) < 0:
				b = root
			else:
				a = root
			root = (a + b)/2
	return root

def main():
	start = -1
	end = 10
	print(function(start), function(end))


def function(x):
	return math.pow(x,2) + x - 6 

if __name__=="__main__":
	main()

