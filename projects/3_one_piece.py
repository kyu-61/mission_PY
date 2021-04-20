from time import sleep
import ascii_magic

def pic_roger():
    out = ascii_magic.from_image_file("/home/kyubi/python/practice/projects/roger.jpeg",columns = 150, char = "#")
    ascii_magic.to_terminal(out)
    
pic_roger()    

def luffy():
    out2 = ascii_magic.from_image_file("/home/kyubi/python/practice/projects/luffy.jpeg",columns = 150, char = "#")
    ascii_magic.to_terminal(out2)
    
def intro():
    line_1 = "wealth , fame , power . Gol D. Roger , the king of pirates, attained everything this world has to offer.\n"
    line_2 = "The words he uttered just before his death drove people to the seas.\n"
    line_3 = "My treasure? If you want it, you can have it!\n"
    line_4 = "find it! I left everything that world has to offer there!\n"
    for x in (line_1,line_2,line_3,line_4):
        print (x,end = "")
        sleep(1.3)

intro()

def banner():
    print("""
          ___               ____  _               
         / _ \ _ __   ___  |  _ \(_) ___  ___ ___ 
        | | | | '_ \ / _ \ | |_) | |/ _ \/ __/ _ \\
        | |_| | | | |  __/ |  __/| |  __/ (_|  __/
         \___/|_| |_|\___| |_|   |_|\___|\___\___|

        """)

banner()

print("""
Hi, Monkey D. Luffy.
you want to become Pirate King , right?
""")

if input("[y/n]") == 'y':
    print("Great, your are reckless young brat!! ")
    if input("Go to Alabasta. [y/n]") == 'y':
        print("Shit!, Crocodile is here.")
        if input("Do you want to fight him. [y/n]") == 'y':
            print("You\'ve won the fight.\n Your Bounty is 100,000,000 berries")
            if input("Go to Water Seven. [y/n]") == 'y':
                print("Nico Robin is in danger!\n Declare war against world government and fight CP9.")
                if input("[y/n] ?") =='y':
                    print("You made pretty good name ,luffy. you are not a mere pirate anymore, you a super nova.\n your bounty is 300,000,000 berries.")
                    if input("Ace is in Danger! Do want to save Ace? [y/n]") == 'y':
                        print("its too late to save Ace.")
                        if input("Do you want to train harder?") =='y' and input("call the crew after 2 years") =='y':
                            print("You and your crew is on next level.")
                            if input("Do you to enter into New world?") == 'y':
                                if input("Big Mom wants to take you down! Do you want to take her down? [y/n]") == 'y':
                                    print("Great!!!")
                                    print("They say that fifth yonko emerged!")
                                    print("your bounty is 1.5 billion berries")
                                    if input("go to Wano") == 'y':
                                        if input("Kaido goes rampage, take him down!") == 'y':
                                            print("he kicked your ass")
                                            if input("Train much more harder!!") == 'y':
                                                if input("Fight kaido again ?") == 'y':
                                                    print("you've won")
                                                    if input("fight Black Beard ?") == 'y':
                                                        print("you won")
                                                        if input("go to laughtale?") == 'y':
                                                            print("Congrats!!!")
                                                            luffy()
                                                            line_5 = "The New Pirate King, Monkey D. Luffy"
                                                            for x in (line_5):
                                                                print (x,end = "")
                                                                sleep(0.1)
                                                    else:
                                                        print("You are scared of a yonko")
                                                else:
                                                    print("You are scared of a yonko")
                                            else:
                                                print("You are scared of a yonko")
                                        else:
                                            print("You are scared of a yonko")
                                    else:
                                        print("you've lost on your path")
                                else:
                                    print("You are scared of a yonko")
                            else:
                                print("You are scared of a yonko")
                        else:
                            print("You are not going to the pirate king!")
                    else:
                        print("You are such a loser")
                else:
                    print("You are not a good pirate any more . you've lost")
            else:
                print("You\'ve lost on the way!")
        else:
            print("you scaredy cat !!")
    else:
        print("You\'ve lost")
else:
    print("You don't inherit Roger's will")
    
