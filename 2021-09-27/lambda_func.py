# lambda function
# it's a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression.

summer = lambda a, b: a+b

print(summer(10,21))


def calculateInst(p, r):
	return lambda t : p * r * t / 100


inst = calculateInst(1000, 10)

print(inst(2))
print(inst(20))