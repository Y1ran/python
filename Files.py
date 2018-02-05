# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 22:35:56 2018

@author: Administrator
"""

#测试文件输入与输出

filename =r'011pi_million_digits.txt'

with open(filename, 'w') as fhand:
    list2 = [x for x in range(0,1000)]
    fhand.write(str(list2))

with open(filename) as fhand:

    lines = fhand.readlines()
    
pi = ''
if lines:
    try:
        for line in lines:
            pi = line.strip() + '\n'
    except:
        print("no file input \n")
    else:
        for line in lines:
            print(str(line.strip()) + '\n')
            print('\n')
        print("the file test is done.. \n")
    finally:
        pass

'''测试生日是否在π的小数位中
birthday = str(input("enter your birth : "))
if birthday in pi:
    print("great! your birthday in it")
else:
    print("your birthday does not..")
'''
#计算文件的总字数

def count_words(filename):
    
    try:   #测试open的执行
        with open(filename) as fh:
            contents = fh.read()
    except FileNotFoundError:
        msg = "sorry, it do not ..."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("the file total has " + str(num_words) + " words")

count_words(filename)
