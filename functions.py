# Functions in python
# What about len() 

# Examples of inbuilt functions
# list1 = [1,2,3,4,5,6]
# print("Maximum number from list : ", max(list1))
# print("Minimum number from list : ", min(list1))
# print("Sum number from list : ", sum(list1))

# How do functions works?
# They may or may not accepts input parameter
# They may or may not return any output


# # example of a function which doesn't accept any parameter
# # and doesn't return anything
# def welcome_message():
#     print("Welcome to iNeuron Batch-2 !!!")

# welcome_message()

# # example of a function which doesn't accept any parameter
# # and does return something
# def bot_message():
#     print("Message from Bot using Print!!")
#     return "Message from Bot !!"

# print( bot_message() )
# result = bot_message()
# print("Output from bot_message() ", result)


# example of a function which accepts some parameter
# and return the values
def avg_of_two_nums( a , b):
    count = 2
    print("First Value : ", a)
    print("Last Value : ", b)
    avg_result = (a+b)/2
    return avg_result

num1 = 10
num2 = 15
# output = avg_of_two_nums( num1, num2 )
# print("Result of avg_of_two_nums functions : ", output)

# output1 = avg_of_two_nums( num1 )
# print("Result of avg_of_two_nums functions : ", output1)


# Write a function to calculate the factorial of a num ?
def factorial(n):

    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(1, n+1):
        result = result * num
