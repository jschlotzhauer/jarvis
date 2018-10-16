
#Generate winning lottery number
def lottono():
    import random
    integer = []
    for number in range (0 , 5):
        integer.append(random.randint(0, 70))
    return integer

print('The winning numbers are {}'.format(lottono()))

#Generate selected lottery number
def lottopickno():
    import random
    integer = []
    for number in range (0 , 5):
        integer.append(random.randint(0, 70))
    return integer

print('You selected: {}'.format(lottopickno()))