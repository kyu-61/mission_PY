import random

def banner():
    print ("""                                     _                        
     _ __   __ _ ___ _____      ____| |       __ _  ___ _ __  
    | '_ \ / _` / __/ __\ \ /\ / / _` |_____ / _` |/ _ \\ '_ \ 
    | |_) | (_| \__ \__ \\\\ V  V / (_| |_____| (_| |  __/ | | |
    | .__/ \__,_|___/___/ \_/\_/ \__,_|      \__, |\___|_| |_|
    |_|                                      |___/            
    """)

banner()
passwd = []
n = int(input("enter password length : "))
for i in range (0,n):
    a = chr(random.randint(48,127))
    passwd.append(a)
    passwd_to_str = ''.join(passwd)
print(f"Your generated password is {passwd_to_str}")
