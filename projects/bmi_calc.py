G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white

def banner():
    print("""%s
     ____  __  __ ___             _      
    | __ )|  \/  |_ _|   ___ __ _| | ___ 
    |  _ \| |\/| || |   / __/ _` | |/ __|
    | |_) | |  | || |  | (_| (_| | | (__ 
    |____/|_|  |_|___|  \___\__,_|_|\___|     

        linkedin : https://www.linkedin.com/in/vijay-balaji-m/                            
    """ % (B))

banner()

h = input("%sEnter your height (ft) : %s" % (Y,W))
print("%s >>> The Height you've entered : %s{}\n".format(h) % (Y,W))
w = input("%sEnter your weight (Kg) in : %s" % (Y,W))
print("%s >>> The Weight you've entered : %s{}\n".format(w) % (Y,W))
print()

split_h = h.split(".")
feet = split_h[0]
inch = split_h[1]
meter_ft = int(feet) * 0.3048
meter_in = int(inch) * 0.0254
meter = float(meter_ft + meter_in)
print(f"%sYour Height in meter : %s{meter} m\n" % (Y,W))
print()
    
bmi_ = float(w) / (meter*meter)
bmi_ = float(round(bmi_,1))
print(f"%sYour BMI value : %s{bmi_}\n" % (Y,W))
print()

if bmi_ <= 18.5:
    print(" >>> 😕 %sbuddy, you should gain some weight" %(W))
elif bmi_ >= 25:
    print(" >>> 😑 %sbuddy, you should drop some weight" %(W))
else:
    print(" >>> 🤩 %sbuddy, you are fit !!!" %(G))


