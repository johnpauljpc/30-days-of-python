template = """Hello {name}, thank you for joining {website}.
We are glad to have you here."""

def format_msg(my_name = None, my_website = None):
    msg = template.format(name = my_name, website = my_website)
    return msg



