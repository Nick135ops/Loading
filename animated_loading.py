import time
import sys

def loading():
    l = ['|', '/', '-', '\\']
    for i in l+l+l+l+l+l+l+l+l+l:
        sys.stdout.write('\r' + f"Thinking of an insult... "+i)
        sys.stdout.flush()
        time.sleep(0.2)
