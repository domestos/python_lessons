def myprint_text():
    """ this function prints the some text"""
    print(" i print very interesting text!")
    print("bay...\n")


def i_print_text_too():
    """ this function prints the some text too"""
    print(" i am very easy function")
    print("bay ... too\n")


def i_want_to_know_your_name(name):
    print("Hello "+name.title()+", now i know your name! ")


def i_like_the_numbers(x, y):
    print(x+y)

def i_will_give_you_sum(x,y):
    s=x+y
    return s

#factor function
#3! = 1*2*3

def factorial(x):
    """Calculate function of number X (X!)
       3! = 1*2*3
    """

    result = 1
    for i in range(1, x+1):
        result *=i
        print(str(i) + "!\t = "+ str(result))


myprint_text()
i_print_text_too()
i_want_to_know_your_name("valera")
i_like_the_numbers(10,20)
print(i_will_give_you_sum(5,30))
factorial(10)
