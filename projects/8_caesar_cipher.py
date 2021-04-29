def banner():
    print('''
                                       _       _               
  ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                        |_|                    


''')

def cipher(message,opr,shift):
    if opr == 'encode':       
        enc = []
        for i in msg:
            enc.append(i)
        enc_ = []
        conv = []
        for letter in enc:
            keyed = ord(letter) + shift
            enc_.append(keyed)
        for char in enc_:
            conn = chr(char)
            conv.append(conn)
        encrypt = ""
        for joint in conv:
            encrypt += joint
        print(f"your encoded message {encrypt}")
    elif opr == 'decode':
        dec = []
        conv = []
        for i in msg:
            dec.append(i)
        dec_ = []
        for letter in dec:
            keyed = ord(letter) - shift
            dec_.append(keyed)
        for char in dec_:
            conn = chr(char)
            conv.append(conn)
        decrypt = ""
        for joint in conv:
            decrypt += joint
        print(f"your encoded message {decrypt}")
    else:
        pass

banner()
msg = input("Enter the message : ")
operation = input("Encode / Decode : ")
key = int(input("Enter the shift factor : "))
cipher(message = msg,opr = operation, shift = key)