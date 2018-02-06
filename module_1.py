'''
Created on 2018 M02 6

@author: Nuno
'''


def is_number(valor):

    try:
        return int(valor)
    except:
        return None


if __name__ == '__main__':

    while True:
        valor_1 = input("first number integer?")
        valor_1 = is_number(valor_1)
        if (is_number(valor_1) != None):
            break

    while True:
        valor_2 = input("second number integer?")
        valor_2 = is_number(valor_2)
        if (is_number(valor_2) != None):
            break

    if (valor_1 == valor_2):
        print("IGUAIS")
    elif (valor_1 > valor_2):
        print("MAIOR: {}".format(valor_1))
    else:
        print("MAIOR: {}".format(valor_2))
