    '''
    moves robot turns 90 degrees after 10 steps forward
    '''
def move_square(size,degrees):
    print("Moving in a square of size "+str(size))
    for i in range(4): 
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

    '''
    moves forward by the length and turns 90 degrees
    '''
def move_rectangle(length, width) :
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

    '''
    moves 1 degree and 1 step at time
    '''
def move_circle():
    degrees = 1
    length = 1
    print("Moving in a circle")
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def Square_dancing() :
    size = 10
    size2 =20
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        degrees = 90
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")
    '''
    itll create circles close together but never on the same spot
    '''
def crop_circles():
    length_c = 1    
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        degrees = 1
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        for k in range(360):
            print("* Move Forward " + str(length_c))
            print("* Turn Right " + str(degrees) + " degrees")
# TODO: Decompose into functions
def move():
    size = 10
    length = 20
    width = 10 
    degrees = 90
    move_square(size,degrees)
    move_rectangle(length, width)
    move_circle()
    Square_dancing()
    crop_circles()





def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
