from ntpath import join
import random
import string
import subprocess

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols =  string.punctuation
all = (lower + upper + numbers + symbols)

x = input("Which login are you creating for?")
y = input("What is your username?")
z = int(input("Enter the number of characters you want your password to have: "))
password = "".join(random.sample(all, z))
xyz = [("Account: {}".format(x)), ("Username: {}".format(y)), ("Password: {}".format(password))]
#xyz = x + '\n' + y + '\n' + str(password)
print('Here is your password: {}'.format(password))
#print(xyz)
f = open('password.txt', 'a')
f.write("\n")
for elements in xyz:
    f.write(elements + "\n")
f.write("\n")
f.close()
