# How to create Lambda Functions

# First normal function to add integer 5 in given number
def add_five(num):
    result = num + 5
    return result

x = 7
print(add_five(x))

# Same program using lambda function
lambda_add_five = lambda x : x + 5

y = 10
print(lambda_add_five(y))

# Write a lambda function to add two input numbers
lambda_add_two_nums = lambda x , y : x + y

a = 30
b = 20
print(lambda_add_two_nums(a,b))

# Wite a lambda function to concatenate two input strings
lamda_q=lambda x,y: x + y
c="darshan"
d="shirke"
print(lamda_q(c,d))


# Write a lambda function to calculate maximum of two numbers
def max_two_nums(x,y):
    if x>y:
        return x
    else:
        return y

a = 5
b = 4
print(max_two_nums(a,b))

lambda_max_two_nums = lambda x,y : x if x>y else y

num1 = 20
num2 = 10
print(lambda_max_two_nums(num1,num2))
