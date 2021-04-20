import random

print("""
        INSTRUCTION:
            This is a best of 5 match.
            1. Press r for rock 👊
            2. Press p for paper 🖐
            3. Press s for scissors ✂️
""")

list_ = ['👊','🖐','✂️']
    
name = input("Enter Your Name : ")
print()
print(f" BOT    vs   {name}")
print("-" * (12 + len(name)+2))

for i in range(0,5):
    rand = random.randint(0,len(list_) - 1)
    bot = list_[rand]
    op = input("")
    if op == 'r':
        print(f" {bot}            {list_[0]}")
    elif op == 's':
        print(f" {bot}            {list_[2]}")
    elif op == 'p':
        print(f" {bot}            {list_[1]}")
    else:
        print(" you've pressed wrong key")
