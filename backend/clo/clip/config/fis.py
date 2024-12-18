temperature = int(input("t "))
'''So first you have the function definition keyword
then its name and then a comma seperated list of 
parameters then a colon. The list has to be demited by parenthesis
even if it's empty however here it contains two arguments
arg1 and arg2.
Underneath that you've got Docstring containing a brief 
explaination.
Beneath that you have your primary code or function
body and below that you have a return statement.
I was able to find this example on @mathsppblog's twitter
/X '''
def function_name(arg1, arg2):
    """Does X, Y, Z"""

    # ... function body
    return rusult
''' An example that actually does something by Software carpentry 
lessons. Again you have the def keyword, the name and in the parameter
list you have one parameter name: initially I had assumed that this could have been a variable
 from a previous line but of course you can actually declare it here and then there's just a simple return statement with
 a return value'''   
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

# after this perhaps you wanna run the function may be even concatenate it in a string
fahr_to_celsius(32)
print("temperature is", fahr_to_celsius(32), "C")
# or we could take an input while executing the program

print("temperature is", fahr_to_celsius(temperature), "C")