print("Hello there! I am a repeating bot. I will repeat whatever you want me to! Cool right? Just type what you want me to say and I will say it. Have fun and please don't make me say anything stupid.")
repeat=input()
print("-")
print("-")
import sys,time
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./5)

sprint(f'{repeat}')
