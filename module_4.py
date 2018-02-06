'''
Created on 2018 M02 6

@author: Nuno
'''

import time

import utils


def count_down(valor):

    for i in range(valor, 0, -1):
        print(i)
        time.sleep(1)
    print("final")


if __name__ == '__main__':

    while True:
        valor = input("Introduza um valor inteiro: ")
        valor = utils.is_number(valor)
        if valor != None and valor > 0:
            break

    # call count down
    count_down(valor)
