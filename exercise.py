ordinal_indicator = {1:'st', 2:'nd', 3:'rd', 4:'th', 5:'th', 6:'th', 7:'th', 8:'th', 9:'th', 10:'th', 11:'th', 12:'th', 13:'th', 14:'th', 15:'th', 16:'th', 17:'th', 18:'th', 19:'th', 20:'th', 21:'st'}


def get_ordinal_number(num):
    return str(num) + ordinal_indicator[num]


print(get_ordinal_number(1))
print(get_ordinal_number(7))
print(get_ordinal_number(21))