# practice with functions via Women Who Code MeetUp

# define a function
def funct1():
    return ("I'm all about functions and Women Who Code")

# function that takes argument
def funct2(arg1, arg2):
    return (arg1, "is WWC's year and also for " + arg2)

#function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=2):
    result = 1;
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

################################################################################
##Main Program

print (funct1())
print (funct2(2017, "Sarah"))
print (cube(6))
print (power(6))
print (multi_add(3,5,6,8,9))
