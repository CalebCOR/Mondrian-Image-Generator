# File: Corlett_p2.py
# Author: Caleb Corlett
# Date: 4-19-2023
# Section: 1502
# E-mail: caleb.corlett@maine.edu
# Description:
""" Use recursion to generate Mondrian style art. """
# Collaboration:
"""                             just me                            """

import timeit
import threading as T
from queue import Queue
import graphics as G
from random import randrange

WINDOW_TITLE = 'Corlett_p2.py'
STARTING_WIDTH = 500
STARTING_HEIGHT = 500
FRAMERATE_CAP = 2                # FRAMERATE_CAP isn't used anywhere in code, but FRAMERATE 
FRAMERATE = int(1000/FRAMERATE_CAP)
PIXEL_MIN = 90
WITHHOLD_PROBABILITY = 1.5       # Higher is less probable to split
SPLIT_PERCENT_LBOUNDS = 0.38
SPLIT_PERCENT_HBOUNDS = 0.61
YELLOW_RATE = 0.09
BLUE_RATE = 0.15
RED_RATE = 0.25


def createWindow():
    workWindow = G.GraphWin(WINDOW_TITLE, STARTING_WIDTH, STARTING_HEIGHT, autoflush=False)
    workWindow.setBackground('#FFFFFF')

    return workWindow


def randColor():
    var = randrange(0,100)/100
    if(var < YELLOW_RATE):
        return 'yellow'
    if(var < BLUE_RATE):
        return 'blue'
    if(var < RED_RATE):
        return 'red'
    else:
        return 'white'
    

def mondrian(pTopLeft, pWidth, pHeight, pQueue):
    
     # Recursively cuts a rectangle (topleft corner == pTopLeft (G.Point), width ==
     # pWidth and height == pHeight) into 4 rectangles and recursively splits those


    xSplitCheck = randrange(PIXEL_MIN, int(pWidth * WITHHOLD_PROBABILITY))
    ySplitCheck = randrange(PIXEL_MIN, int(pHeight * WITHHOLD_PROBABILITY))

 # Divider Assignment
    if(xSplitCheck < pWidth):
        xDivider = randrange(int(pWidth * SPLIT_PERCENT_LBOUNDS), int(pWidth * SPLIT_PERCENT_HBOUNDS)) + pTopLeft.x
    else:
        xDivider = pWidth + pTopLeft.x
    if(ySplitCheck < pHeight):
        yDivider = randrange(int(pHeight * SPLIT_PERCENT_LBOUNDS), int(pHeight * SPLIT_PERCENT_HBOUNDS)) + pTopLeft.y
    else:
        yDivider = pHeight + pTopLeft.y

 # Rectangle creation and recursion
     # quadrant 1
    quad1Rect = G.Rectangle(pTopLeft, G.Point(xDivider, yDivider))
    width = quad1Rect.p2.x-quad1Rect.p1.x
    height = quad1Rect.p2.y-quad1Rect.p1.y
    if(width > 90 and height > 90):
        q1Thread = T.Thread(target=mondrian, args=(quad1Rect.p1, width, height, pQueue))
        q1Thread.start()
    else:
        quad1Rect.setFill(randColor())
        pQueue.put(quad1Rect)
    
     # quadrant 2
    if(xDivider != pWidth + pTopLeft.x):
        quad2Rect = G.Rectangle(G.Point(xDivider, pTopLeft.y), G.Point(pWidth + pTopLeft.x, yDivider))
        width = quad2Rect.p2.x-quad2Rect.p1.x
        height = quad2Rect.p2.y-quad2Rect.p1.y
        if(width > 90 and height > 90):
            q2Thread = T.Thread(target=mondrian, args=(quad2Rect.p1, width, height, pQueue))
            q2Thread.start()
        else:
            quad2Rect.setFill(randColor())
            pQueue.put(quad2Rect)
    
     # quadrant 3
    quad3Rect = G.Rectangle(G.Point(pTopLeft.x, yDivider), G.Point(xDivider, pHeight + pTopLeft.y))
    width = quad3Rect.p2.x-quad3Rect.p1.x
    height = quad3Rect.p2.y-quad3Rect.p1.y
    if(width > 90 and height > 90):
        q3Thread = T.Thread(target=mondrian, args=(quad3Rect.p1, width, height, pQueue))
        q3Thread.start()
    else:
        quad3Rect.setFill(randColor())
        pQueue.put(quad3Rect)
    
     # quadrant 4
    if(yDivider != pWidth + pTopLeft.y):
        quad4Rect = G.Rectangle(G.Point(xDivider, yDivider), G.Point(pWidth + pTopLeft.x, pHeight + pTopLeft.y))
        width = quad4Rect.p2.x-quad4Rect.p1.x
        height = quad4Rect.p2.y-quad4Rect.p1.y
        if(width > 90 and height > 90):
            q4Thread = T.Thread(target=mondrian, args=(quad4Rect.p1, width, height, pQueue))
            q4Thread.start()
        else:
            quad4Rect.setFill(randColor())
            pQueue.put(quad4Rect)

    try:
        q1Thread.join()
    except UnboundLocalError:
        pass
    try:
        q2Thread.join()
    except UnboundLocalError:
        pass
    try:
        q3Thread.join()
    except UnboundLocalError:
        pass
    try:
        q4Thread.join()
    except UnboundLocalError:
        pass

###############################################################################################################
def mondrian2(pTopLeft, pWidth, pHeight, pWindow):
    
     # Recursively cuts a rectangle (topleft corner == pTopLeft (G.Point), width ==
     # pWidth and height == pHeight) into 4 rectangles and recursively splits those


    xSplitCheck = randrange(PIXEL_MIN, int(pWidth * WITHHOLD_PROBABILITY))
    ySplitCheck = randrange(PIXEL_MIN, int(pHeight * WITHHOLD_PROBABILITY))

 # Divider Assignment
    if(xSplitCheck < pWidth):
        xDivider = randrange(int(pWidth * SPLIT_PERCENT_LBOUNDS), int(pWidth * SPLIT_PERCENT_HBOUNDS)) + pTopLeft.x
    else:
        xDivider = pWidth + pTopLeft.x
    if(ySplitCheck < pHeight):
        yDivider = randrange(int(pHeight * SPLIT_PERCENT_LBOUNDS), int(pHeight * SPLIT_PERCENT_HBOUNDS)) + pTopLeft.y
    else:
        yDivider = pHeight + pTopLeft.y

 # Rectangle creation and recursion
     # quadrant 1
    quad1Rect = G.Rectangle(pTopLeft, G.Point(xDivider, yDivider))
    width = quad1Rect.p2.x-quad1Rect.p1.x
    height = quad1Rect.p2.y-quad1Rect.p1.y
    if(width > 90 and height > 90):
        mondrian2(quad1Rect.p1, width, height, pWindow)
    else:
        quad1Rect.setFill(randColor())
        quad1Rect.draw(pWindow)
    
     # quadrant 2
    if(xDivider != pWidth + pTopLeft.x):
        quad2Rect = G.Rectangle(G.Point(xDivider, pTopLeft.y), G.Point(pWidth + pTopLeft.x, yDivider))
        width = quad2Rect.p2.x-quad2Rect.p1.x
        height = quad2Rect.p2.y-quad2Rect.p1.y
        if(width > 90 and height > 90):
            mondrian2(quad2Rect.p1, width, height, pWindow)
        else:
            quad2Rect.setFill(randColor())
            quad2Rect.draw(pWindow)
    
     # quadrant 3
    quad3Rect = G.Rectangle(G.Point(pTopLeft.x, yDivider), G.Point(xDivider, pHeight + pTopLeft.y))
    width = quad3Rect.p2.x-quad3Rect.p1.x
    height = quad3Rect.p2.y-quad3Rect.p1.y
    if(width > 90 and height > 90):
        mondrian2(quad3Rect.p1, width, height, pWindow)
    else:
        quad3Rect.setFill(randColor())
        quad3Rect.draw(pWindow)
    
     # quadrant 4
    if(yDivider != pWidth + pTopLeft.y):
        quad4Rect = G.Rectangle(G.Point(xDivider, yDivider), G.Point(pWidth + pTopLeft.x, pHeight + pTopLeft.y))
        width = quad4Rect.p2.x-quad4Rect.p1.x
        height = quad4Rect.p2.y-quad4Rect.p1.y
        if(width > 90 and height > 90):
            mondrian2(quad4Rect.p1, width, height, pWindow)
        else:
            quad4Rect.setFill(randColor())
            quad4Rect.draw(pWindow)

###############################################################################################################3333


def main():
    global window
    window = createWindow()
    global qoo 
    qoo = Queue()

    print(timeit.timeit('mondrian(G.Point(0,0), STARTING_WIDTH, STARTING_HEIGHT, qoo)', 'from __main__ import mondrian\nfrom __main__ import STARTING_WIDTH\nfrom __main__ import STARTING_HEIGHT\nfrom __main__ import qoo\nimport threading as T\nfrom queue import Queue\nimport graphics as G\nfrom random import randrange', number=50))
    print(timeit.timeit('mondrian2(G.Point(0,0), STARTING_WIDTH, STARTING_HEIGHT, window)', 'from __main__ import mondrian2\nfrom __main__ import STARTING_WIDTH\nfrom __main__ import STARTING_HEIGHT\nfrom __main__ import window\nimport threading as T\nfrom queue import Queue\nimport graphics as G\nfrom random import randrange', number=50))

    """while window.closed == False:
        mondrian(G.Point(0,0), STARTING_WIDTH, STARTING_HEIGHT, qoo)
        for _ in range(qoo.qsize()):
            qoo.get().draw(window)
        window.after(FRAMERATE, window.update())"""

main()
