x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

z = 5
y = "John"
print(type(z))
print(type(y))

import random

print(random.randrange(50, 55))

a = "Hello, World!"
print(a[6])

for i in "banana":
  print(i)

c = "Hello, World!"
print(len(c))

txt = "The best things in life are free!"
print("free" in txt)

txn = "The best things in life are free!"
if "free" in txn:
  print("Yes, 'free' is present.")

tx = "The best things in life are expensive!"
print("expensive" not in tx)

t = "Hello, World!"
print(t[-5:-2])

o = "Hello, World!"
print(o.upper())

p = "Hello, World! "
print(p.strip())+3
