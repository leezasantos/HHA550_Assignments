#!/usr/bin/env python
# coding: utf-8

# Leeza A. Santos
# 
# HHA 550 Session 2 Assignment
# 
# * Chapter 1: Exercise 1-7
# * Chapter 2: Exercise 2, 3, 4
# * Chapter 5: Exercise 1

# ## Chapter 1 Exercises 1-7

# #### Exercise 1: What is the function of the secondary memory in a computer?
# 
#     a) Execute all of the computation and logic of the program
#     b) Retrieve web pages over the Internet
#     c) Store information for the long term, even beyond a power cycle
#     d) Take input from the user
# 
# 
# ##### c) Store information for the long term, even beyond a power cycle

# #### Exercise 2: What is a program?
# 
# A computer program is a sequence of instructions that are written for a computer to carry out. Programming is the process of writing, editing, modifying, and debugging a computer program.

# #### Exercise 3: What is the difference between a compiler and an interpreter?
# 
# Compiler is a program system that is used as a tool in programming. The software code that performs the translation process made by the programmer into machine language. while the interpreter is a software that can execute the source code that was written by the programmer and translated into machine language.

# #### Exercise 4: Which of the following contains “machine code”?
# 
#     a) The Python interpreter
#     b) The keyboard
#     c) Python source file
#     d) A word processing document
# 
# ##### c) Python source file

# ##### Exercise 5: What is wrong with the following code:
# >>> primt 'Hello world!'
# File "<stdin>", line 1
# primt 'Hello world!'
# ^
# SyntaxError: invalid syntax
# >>>
# 
# ##### Incorrect spelling for print
# 

# In[3]:


print('Hello world!')


# #### Exercise 6: Where in the computer is a variable such as “x” stored after the following Python line finishes?
# 
#          x = 123
# 
#     a) Central processing unit
#     b) Main Memory
#     c) Secondary Memory
#     d) Input Devices
#     e) Output Devices
# 
# ##### b) Main Memory

# ##### Exercise 7: What will the following program print out:
# 
# x = 43
# x = x + 1
# print(x)
# 
# a) 43
# b) 44
# c) x + 1
# d) Error because x = x + 1 is not possible mathematically
# 
# ##### b) 44

# ## Chapter 2 Exercises 2, 3, 4

# #### Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
# 
# Enter your name: Chuck
# 
# Hello Chuck

# In[4]:


print('Hello',input('Enter your name: '))


# #### Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
# 
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# 
# We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.
# 

# In[5]:


print('Pay:',(float(input('Enter Hours: '))*float(input('Enter Rate'))))


# #### Exercise 4: Assume that we execute the following assignment statements:
# 
# width = 17
# height = 12.0
# 
# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
# 
# 1. width/2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# 
# Use the Python interpreter to check your answers.

# In[6]:


width = 17 
height = 12.0


# In[7]:


w = (width/2) 
d = (width/2.0)
h = height/3
x = 1 + 2 * 5

print(w, type(w))
print(d, type(d))
print(h, type(h))
print(x, type(x))


# ## Chapter 2 Exercises 2, 3, 4

# #### Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
# 
# Enter a number: 4
# 
# Enter a number: 5
# 
# Enter a number: bad data
# 
# Invalid input
# 
# Enter a number: 7
# 
# Enter a number: done
# 

# In[8]:


sum = 0
count = 0
average = 0

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input")
print (sum, count, average)

