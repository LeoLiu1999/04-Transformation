from display import *
from matrix import *
from draw import *

"""
Goes through the file named fname and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:

     line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)

	 ident: set the transform matrix to the identity matrix - 

	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)

	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)

	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z

	 apply: apply the current transformation matrix to the 
	    edge matrix

	 display: draw the lines of the edge matrix to the screen
	    display the screen

	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)

	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname,"r")
    while True:
        command = file.readline()[:-1] #Reads next line and trims off ending newline
        if command == "":
            break
        if command == "line":
            input = file.readline()[:-1].split(" ")
            add_edge(points, input[0], input[1], input[2], input[3], input[4], input[5])
        if command == "ident":
            ident(transform)
        if command == "scale"
            input = file.readline()[:-1].split(" ")
            transform = make_scale(input[0], input[1], input[2])
        if command == "move":
            input = file.readline()[:-1].split(" ")
            transform = make_translate(input[0], input[1], input[2])
        if command == "rotate":
            input = file.readline()[:-1].split(" ")
            if input[0] == "x":
                transform = make_rotX(input[1])
            if input[0] == "y":
                transform = make_rotY(input[1])
            if input[0] == "z":
                transform = make_rotZ(input[1])
        if command == "apply":
            matrix_mult(transform, points)
        if command == "display":
            pass
        if command == "save":
            pass
        if command == "quit":
            return
        
        
