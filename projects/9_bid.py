def banner():
    print(
        '''
    _              _   _             
   / \  _   _  ___| |_(_) ___  _ __  
  / _ \| | | |/ __| __| |/ _ \| '_ \ 
 / ___ \ |_| | (__| |_| | (_) | | | |
/_/   \_\__,_|\___|\__|_|\___/|_| |_|
                                     

'''
        )

banner()
auction = {}

def dict_(b_name,b_amt):
    auction[b_name] = b_amt

def details():
    name = input("Enter bidder Name : ")
    amt = int(input("Enter bid : "))
    dict_(name,amt)
    again = input("Is there any other bidder : [y/n]")
    if again == 'y':
        from replit import clear
        clear()
        details()
    else:
        key_list = list(auction.keys())
        val_list = list(auction.values())        
        start = 0
        for high in range(0,len(val_list)):
            if val_list[high] > start:
                start = val_list[high]
        position = val_list.index(start)
        winner = key_list[position]
        print(f"The Highest Bidder is {winner}")
        
details()