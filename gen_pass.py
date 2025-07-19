import string
import random

length = int(input('Enetr length of Password:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
password = "".join(temp)
print('________________________________')
print('Generated Password is:',password)
print('________________________________')