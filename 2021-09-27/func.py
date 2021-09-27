"""

Q. What is Function?
Ans. 
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

# define a function
def sayHello():
	# funciton body
	print("Hello")




# A function is a block of organized, reusable code that is used to perform a single, related action.
# which returns a value or does not return a value.


# function with a parameter
def say_hi(name):
    print("hi", name)


# default paramter function
def defaul_hi(name = "not found"):
    print("hi",name)


# named arguments example
def just_hello(fname, lname):
    print("welcome", fname, lname)


# variable arguments
def hello_to_all(*args):
    for a in args:
        print("hello",a)


# keyword arguments function where kwargs is a dictionary
def say_vip_hello(**kwargs):
    print(type(kwargs))
    a = kwargs["name"]
    print("vip hello",a)


# so to use a function you need to call it and this is known as 'function call'
sayHello() # funciton call

say_hi("cmpundhir")

defaul_hi()
defaul_hi("ali")

just_hello("museed","ali")
just_hello(lname="pundhir", fname="cm")

hello_to_all("ali","cm","alan","yogesh","dalima", "shikha")

say_vip_hello(name="cm",age=11)