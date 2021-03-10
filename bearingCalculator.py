import math
def mils_to_rads(mils):
    return (45*math.pi*mils)/144000

def rads_to_mils(rads):
    return (rads*1440)/(45*math.pi)

def get_bearing(a, b):
    ax = int(a[0:4])
    ay = int(a[4:])
    bx = int(b[0:4])
    by = int(b[4:])
    #Imaginary point P
    px = ax
    py = ay + 1000

    lengthA = math.sqrt((bx-ax)**2 + (by-py)**2)
    lengthB = 1000
    lengthP = math.sqrt((bx-ax)**2 + (by-ay)**2)

    theta = math.acos((lengthB**2 + lengthP**2 - lengthA**2) / (2*lengthB*lengthP))
    #convert to mils
    theta = rads_to_mils(theta)
    if bx < ax:
        theta = 6400-theta
    
    return str(round(theta*100)).zfill(4)

def get_distance(a, b):
    ax = int(a[0:4])
    ay = int(a[4:])
    bx = int(b[0:4])
    by = int(b[4:])

    distance = math.sqrt((bx-ax)**2 + (by-ay)**2)
    
    return round(distance/100, 2)


class color:
   PURPLE = '\033[1m\033[95m'
   CYAN = '\033[1m\033[96m'
   DARKCYAN = '\033[1m\033[36m'
   BLUE = '\033[1m\033[94m'
   GREEN = '\033[1m\033[92m'
   YELLOW = '\033[1m\033[93m'
   RED = '\033[1m\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

greeterString = color.PURPLE + "Press A" + color.END + """ for a bearing and distance between two points
""" + color.CYAN + "Press B" + color.END + """ for a coordinate from a bearing and distance
""" + color.RED  + "Press C" + color.END + """ to calculate FFG bearings

Enter: """


while True:
    program = input(greeterString).upper()
    print("\n\n")
    if program == "A":
        a = input("Enter 8 figure grid for point a: ").replace(" ", "")        
        b = input("Enter 8 figure grid for point b: ").replace(" ", "")
        
        
        print("Bearing: " + get_bearing(a, b) + "mils")
        print("Distance: " + str(get_distance(a, b))  + "km")
        
    elif program == "B":
        a = input("Enter 8 figure grid for point a: ").replace(" ", "")
        ax = int(a[0:4])
        ay = int(a[4:])
        
        bearing = float(input("Enter bearing (in mils): "))
        distance = float(input("Enter distance (in KM): "))*100
        
        #pythagoras theorum
        if bearing <= 1600:
            deltax = math.sin(mils_to_rads(bearing))*distance
            deltay = math.cos(mils_to_rads(bearing))*distance
        elif bearing <= 3200:
            deltax = math.cos(mils_to_rads(bearing-1600))*distance
            deltay = -math.sin(mils_to_rads(bearing-1600))*distance
        elif bearing <= 4800:
            deltax = -math.cos(mils_to_rads(4800-bearing))*distance
            deltay = -math.sin(mils_to_rads(4800-bearing))*distance
        elif bearing <= 6400:
            deltax = -math.sin(mils_to_rads(6400-bearing))*distance
            deltay = math.cos(mils_to_rads(6400-bearing))*distance
        else: 
            print("invalid input")
            break
        
        bx = round(ax + deltax)
        by = round(ay + deltay)
        
        
        
        
        print("Grid for point b: " + str(bx).zfill(4) + " " + str(by).zfill(4))
    
    
    elif program == "C":
        a = input("Enter 8 figure grid for the Flank Firing Gun: ").replace(" ", "")
        b = input("Enter 8 figure grid for the Limit of Troops: ").replace(" ", "")
        leftOrRight = input("Leftmost or Rightmost limit of Troops? [L/r]: ").upper()

    else:
        print("Invalid input")
        
        
    
    print("\n"*5)
