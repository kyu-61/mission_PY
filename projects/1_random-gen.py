import random

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white
def banner():
    print("""%s
                                 _                                        
             _ __ __ _ _ __   __| | ___  _ __ ___         __ _  ___ _ __  
            | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \ _____ / _` |/ _ \ '_ \ 
            | | | (_| | | | | (_| | (_) | | | | | |_____| (_| |  __/ | | |
            |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_|      \__, |\___|_| |_|
                                                         |___/            
    """ % (R))
    
banner()        

name = input("%s enter your name : %s" %(Y,W))
fav = input("%s enter your fav anime character : %s" %(Y,W))
pet_name = input("%s enter your pet name : %s" %(Y,W))

x = random.randint(1,len(name))
y = random.randint(1,len(fav))
z = random.randint(1,len(pet_name))

l = str(chr(random.randint(97,122)))
m = str(chr(random.randint(97,122)))
n = str(chr(random.randint(97,122)))

if name and fav and pet_name != '':
    rand = random.randint(1,50)
    a = str(name[len(name) - x])
    b = str(fav[len(fav) - y])
    c = str(pet_name[len(pet_name) - z])
    print()
    print(" %s-----> %s{}{}{}{}{}{}{} %sis your band name".format(a,b,c,n,m,l,rand) %(Y,B,Y))
else:
    print (" you've forgot to enter your inputs")

