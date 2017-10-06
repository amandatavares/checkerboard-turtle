# Checkerboard by Deilson Amaral and Amanda Tavares

import turtle as t
t.penup()
# Set position to better draw the Checkerboard
t.setpos(-258,-258)
t.pendown()
t.speed(0)

square_len = 66
pattern1_distance = -7
pattern2_distance = -9
square_num = 8

# The black squares with space to draw other
def square():
    t.color('black')
    t.begin_fill()
    for i in range(4):
        t.forward(square_len)
        t.left(90)
    t.end_fill()
    t.penup()
    t.forward(square_len)
    t.pendown()

# A row has 4 black squares, the space between them is the white square
def row():
    for j in range(4):
        t.penup()
        t.forward(square_len)
        t.pendown()
        square()

# The first pattern draw a row that starts with a white square
def pattern1():
    row()
    t.penup()
    t.forward(pattern1_distance * square_len)
    t.left(90)
    t.forward(square_len)
    t.right(90)
    t.pendown()

# The second pattern draw a row that starts with a black square
def pattern2():
    row()
    t.penup()
    t.forward(pattern2_distance * square_len)
    t.left(90)
    t.forward(square_len)
    t.right(90)
    t.pendown()

def board():
    # A board have 8 rows, so we put this in a range
    for k in range(8):
        # The even row has pattern2
        if k % 2 == 0:
            pattern2()
        # The odd row has pattern1
        else:
            pattern1()

# Here we draw the Checkerboard outline. It's the sum of square len
def outline():
    t.penup()
    t.forward(square_len)
    t.pendown()
    for h in range(4):
        t.forward(square_num * square_len)
        t.right(90)

board()
outline()

# Lists of Turtles, that here is the Checkerboard piece
list1 = []
list2 = []

# A Checkerboard has 12 pieces, so we add 12 circle Turtles to each list, one for red and other for yellow pieces
for i in range(12):
    list1.append(t.Turtle('circle'))
    list1[i].turtlesize(2, 2, 2)
    list1[i].penup()
    list1[i].color('red')
    list1[i].goto(0,-220)

    list2.append(t.Turtle('circle'))
    list2[i].turtlesize(2, 2, 2)
    list2[i].penup()
    list2[i].color('yellow')

# We place every piece into the square
list1[0].goto(223,-220)
list1[1].goto(93,-220)
list1[2].goto(-37,-220)
list1[3].goto(-167,-220)

list1[4].goto(-93,-160)
list1[5].goto(-223,-160)
list1[6].goto(37,-160)
list1[7].goto(167,-160)

list1[8].goto(93,-100)
list1[9].goto(223,-100)
list1[10].goto(-37,-100)
list1[11].goto(-167,-100)

list2[0].goto(-93,220)
list2[1].goto(-223,220)
list2[2].goto(37,220)
list2[3].goto(167,220)

list2[4].goto(93,160)
list2[5].goto(223,160)
list2[6].goto(-37,160)
list2[7].goto(-167,160)

list2[8].goto(-93,100)
list2[9].goto(-223,100)
list2[10].goto(37,100)
list2[11].goto(167,100)

# This code is to Window doesn't close!
t.done()
