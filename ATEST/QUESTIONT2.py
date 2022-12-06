import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./5)

sprint('Hello there!')

import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./5)

sprint('What is yours?')

name=input()

import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./5)

sprint(f'Hello {name}!')
