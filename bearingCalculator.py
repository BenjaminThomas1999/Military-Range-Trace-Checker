import math
def mils_to_rads(mils): #inputs an angle measured in miltary mils and returns angle in radians
    return (45*math.pi*mils)/144000

def rads_to_mils(rads): #inputs an angle measured in radians and returns angle in military mils
    return (rads*1440)/(45*math.pi)

def get_bearing(a, b):
    ax = int(a[0:4])
    ay = int(a[4:])
    bx = int(b[0:4])
    by = int(b[4:])
    #Create an imaginary point to cconstruct a triangle from which an angle can be calcuated 
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

def create_line(a, bearing, distance):#creates a line from point a
    ax = int(a[0:4])
    ay = int(a[4:])
    
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
        return "invalid input"
        
    
    bx = round(ax + deltax)
    by = round(ay + deltay)
        
    return str(bx).zfill(4) + " " + str(by).zfill(4)
    
def input_grid(name):
    return input("Enter 6 figure grid reference for point " + name + ": ").replace(" ", "")

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
        a = input_grid("a")        
        b = input_grid("b")
        
        
        print("Bearing: " + get_bearing(a, b) + "mils")
        print("Distance: " + str(get_distance(a, b))  + "km")
        
    elif program == "B":
                
        print(create_line(input_grid("b"),
        int(input("Enter bearing from point a (mils): ")),
        int(input("Enter distance from point a (KM): "))))
    
    
    elif program == "C":
        FFG = input_grid("Flank Firing Gun")
        LoT = input_grid("Limit of Troops")
        leftOrRight = input("Leftmost or Rightmost limit of Troops? [L/r]: ").upper()
        axis = get_bearing(FFG, LoT)
        print("Axis: " + axis)
        if leftOrRight == "L":
            axis -= 200
        elif leftOrRight == "R":
            axis += 200
        
        print("Axis (adjusted for 200mils safety): " + axis)
        
    else:
        print("Invalid input")
        
        
    
    print("\n"*5)
