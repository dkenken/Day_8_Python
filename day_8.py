# excercises Day #8

# AGENDA: Functions

# Simple Function
def greet():
    print("Hi")
    print("what is your name?")
    print('My name is Ken')

greet()

# Function that allows your input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}")

greet_with_name("King")

# Function with more than one input

def greet_with(name, location):
    print(f'Hello {name}')
    print(f"What is it like in {location}")

greet_with("Kenzu", "Broward")

# Function with keywords argument

def greet_with_name_locaton(name, location):
    print(f'Hello {name}')
    print(f"What is it like in {location}")

greet_with_name_locaton(name="Ken", location="Seattle")

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
#  You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5
#                = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width) / 5)
    return num_cans
    
can_needed = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You'll need {can_needed} cans of paint")

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# My OWN Excercise 

# You are fixing a wall. The instructions on the cement says that 1 cement can cover 10 square meters of wall. Given a random height and width of wall, calculate how many cements you'll need to buy.

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 10
# cement_calc(height = test_h, width = test_w, cover = coverage)

def cement_calc(height, width, cover):
    area = math.ceil((height * width) / 10)
    return area

num_of_cement = cement_calc(height = test_h, width = test_w, cover = coverage)
print(f"You'll need {num_of_cement} cement(s) to fix the wall")

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# You need to write a function that checks whether if the number passed into it is a prime number or not

def prime_checker(number):
    is_prime = True
    for i in range(2, number): 
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
      
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

should_continue = True

while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type 'Yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
    print("Goodbye")

