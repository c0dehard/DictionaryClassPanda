import names
import random

def add_domains(n):
    count = 0
    emails = []
    while count < n:
        emails.append(input(f"{count+1}/{n}) Enter domain > "))
        count += 1
    return emails

def gen_mail_address(emails,name_style):
    email = ""
    if name_style == 0:
        email = f'{names.get_full_name().replace(" ",".")}@{random.choice(emails)}'
    elif name_style == 1:
        email = f'{names.get_first_name()}@{random.choice(emails)}'
    elif name_style == 2:
        email = f'{names.get_last_name()}@{random.choice(emails)}'
    return email

def gen_x_mail_addresses(x,from_list):
    count = 0
    done= False
    style = int(input("Choose name style: 0 full, 1 first, 2 last > "))
    while not done:
        print(gen_mail_address(from_list,style))
        count +=1
        if count == x:
            done = True

if __name__ == "__main__":
    mylist = add_domains(int(input("How many domains? > ")))
    gen_x_mail_addresses(int(input("How many mail addresses? > ")),mylist)
