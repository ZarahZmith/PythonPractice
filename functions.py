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

def tempConverter(temp, num=1):
    def celsius_to_fahrenheit(c_temp):
        return 9.0/5.0* c_temp + 32

    def fahrenheit_to_celsius(f_temp):
        return (f_temp - 32.0) * 5.0/9.0

    if num == 1:
        result = celsius_to_fahrenheit(temp)
        print (str(temp) + " celsius to fehrenheit:")
    elif num == 2:
        result = fahrenheit_to_celsius(temp)
        print (str(temp) + " fahrenheit to celsius:")
    else:
        result = 0
        print ("Temp not valid")
    print (result)

################################################################################
##Main Program

print (funct1())
print (funct2(2017, "Sarah"))
print (cube(6))
print (power(6))
print (multi_add(3,5,6,8,9))

#tempConverter
tempConverter(40)
tempConverter(67,2)
tempConverter(89,3)
