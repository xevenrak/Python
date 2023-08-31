import random


def generate_password(length):

  password = ""

  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

  for i in range(length):

    password += random.choice(characters)
    
  return password

length = int(input("Enter the length of the password: "))

print("Your random password is:", generate_password(length))
