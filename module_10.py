'''
Created on 2018 M02 6

@author: Nuno
'''


if __name__ == '__main__':

    text = input("Some text:")

    dict = {}
    for word in text.split():  # other variant split (",").split("\t")
                                # split("space")
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    print(dict)
