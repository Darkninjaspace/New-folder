import random

w = 1
e = 0
x = "start"
y = "end"
mapRow = 0
mapRowElement = 0
win = 0
map =  [[w,w,w,w,w,w,w,w,w,w,w,w],
        [e,e,e,e,e,e,e,w,e,e,e,w],
        [e,w,e,w,e,w,e,w,e,w,e,w],
        [e,w,e,w,e,w,e,w,e,w,e,w],
        [e,e,e,w,e,w,e,w,e,w,e,w],
        [w,w,e,w,e,w,e,w,e,w,y,w],
        [x,e,e,w,w,w,e,e,e,w,w,w]]



def findStart (mapRow,mapRowElement,map):
    mapLength = len(map)
    for i in range (0,mapLength,1):
        rowLength = len(map[mapRow])
        for p in range (0,rowLength,1):
            if "start" == map[mapRow][mapRowElement]:
                startPosRowElement = mapRowElement
                startPosRow = mapRow
                print (startPosRow,startPosRowElement)
                group = (startPosRow),(startPosRowElement)
                
                return startPosRow, startPosRowElement
            mapRowElement += 1
        mapRow += 1
        mapRowElement = 0

startPosRow, startPosRowElement = findStart(mapRow,mapRowElement,map)
frontier = [(startPosRow,startPosRowElement)]
explored = []
lookValElement = 1
lookVal = 1

while win == 0:
    x = frontier.pop(-1)
    explored.append(x)
    for i in range (0,4,1):
        if i%2 == 0:
            lookValElement = -1
        else:
            lookValElement = 1
        if i > 2:
            lookVal = -1
        else:
            lookVal = 1
        if frontier [(startPosRow,startPosRowElement-lookValElement)] == 0:
            print("blah")
