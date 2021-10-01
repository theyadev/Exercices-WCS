import time
def writeAnimation(t):
    for l in t:
        print(l, end="", flush=True)
        if l == ",":
            time.sleep(0.06)
        if l == "." or l == "!" or l == "?":
            time.sleep(0.3)
        else:
            time.sleep(0.01)