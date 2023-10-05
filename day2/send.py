import sys
from formatting import format_msg

def send(name, website, verbose = False):
    msg = format_msg(name, website)
    return msg
# print(send("john", "http//www.site.com"))
# Python's standard way of calling a function in the page instead send()
if __name__ == "__main__":
    print(send("Johnpaul", "http//www.site.com"))