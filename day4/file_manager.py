import os
# email_txt = "templates/email.txt"
this_file_path = os.path.abspath(__file__)
base_dir = os.path.dirname(this_file_path)

email_txt = os.path.join(base_dir, "templates", "email.txt")

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name="Johnpaul"))