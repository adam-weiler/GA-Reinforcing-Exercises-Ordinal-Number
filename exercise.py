# ordinal_indicator = {0: 'th', 1:'st', 2:'nd', 3:'rd', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th', 10:'th', 11:'th', 12:'th', 13:'th', 14:'th', 15:'th', 16:'th', 17:'th', 18:'th', 19:'th', 20:'th', 21:'st'}

ordinal_indicator = {0: 'th', 1:'st', 2:'nd', 3:'rd', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th', 10:'th'}

def get_ordinal_number(num):
    last_digit = abs(num) % 10  # The abs function will treat all numbers as positive.

    return str(num) + ordinal_indicator[last_digit]


print(get_ordinal_number(-205))
print(get_ordinal_number(-6))
print(get_ordinal_number(0))
print(get_ordinal_number(1))
print(get_ordinal_number(2))
print(get_ordinal_number(23))
print(get_ordinal_number(100))
print(get_ordinal_number(104))
print(get_ordinal_number(1007))
print(get_ordinal_number(2118))
print(get_ordinal_number(3959))
print(get_ordinal_number(40153160))