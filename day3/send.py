import re
from send_email import send_mail

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

print("format:  to_email, msg, html \n \n")
def send(to_email = None, msg = None, html = None):
    assert to_email != None
    if not(re.match(pattern=pattern, string = to_email)):
        print("email is invalid")
        return False
    
    # makes email strin a list
    if to_email is not list:
        to_email = to_email.split()

    response = send_mail(to_emails = to_email, text = msg, html = html)
    print (response)


# if __name__  == "__main__":
#     response = send(to_email = None, msg = "Hello Dear, this is just a message sent via python", html = None )
#     print("-----------------msg-----------------")
#     print(response)


    
        
