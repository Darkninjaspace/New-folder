import random

w = 1
e = 0
x = "start"
y = "end"
mapRow = 0
mapRowElement = 0
map =  [[w,w,w,w,w,w,w,w,w,w,w,w],
        [e,e,e,e,e,e,e,w,e,e,e,w],
        [e,w,e,w,e,w,e,w,e,w,e,w],
        [e,w,e,w,e,w,e,w,e,w,e,w],
        [e,e,e,w,e,w,e,w,e,w,e,w],
        [w,w,e,w,e,w,e,w,e,w,y,w],
        [x,e,e,w,w,w,e,e,e,w,w,w]]

frontier = []
explored = []

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

def look(x,y,map,frontier,explored):
    win = 0
    p=1
    a=0
    valueChange = 0
    while win == 0:
        print (frontier)
        win = checkPlace(x,y,map,frontier,explored,p)
        print ("iteration:",a)
        a += 1
        if a >= 100:
            print ("hit dead end")
            quit()
        
    print("you did it")
    quit()

def checkUp(yow,zelement,group,map,frontier,explored,p):
    if map [yow - p][zelement] == "end":
        print((yow - p,zelement),"yay")
        return 1
    if map[yow - p][zelement] == 0:
        group = (yow - p),(zelement)
        if group not in explored:
            frontier.append (group)
            a = frontier.pop(0)
            explored.append(a)
    return 0

def checkDown(yow,zelement,group,map,frontier,explored,p):
    if 0 <= yow+p != len(map):
        if map [yow + p][zelement] == "end":
            print((yow + p,zelement),"yay")
            return 1
        if map[yow + p][zelement] == 0:
            group = (yow + p),(zelement)
            if group not in explored:
                frontier.append (group)
                a = frontier.pop(0)
                explored.append(a)
    return 0                

def checkRight(yow,zelement,group,map,frontier,explored,p):
    if map [yow][zelement + p] == "end":
        print((yow,zelement + p),"yay")
        return 1
    if map[yow][zelement + p] == 0:
        group = (yow),(zelement + p)
        if group not in explored:
            frontier.append (group)
            a = frontier.pop(0)
            explored.append(a)
            #print (p,"yeh")
    return 0

def checkLeft(yow,zelement,group,map,frontier,explored,p):
    if map [yow][zelement - p] == "end":
        print((yow,zelement - p),"yay")
        return 1
    if map[yow][zelement - p] == 0:
        group = (yow),(zelement - p)
        if group not in explored:
            frontier.append (group)
            a = frontier.pop(0)
            explored.append(a)
            #print (p,"yehe")
    return 0

def checkPlace (r,e,map,frontier,explored,p):
    yow = frontier [0][0]
    zelement = frontier [0][1]
    condition = 0
    condition1 = 0

    choose = random.randint(0,1)
    
    print(choose)

    if choose == 0:
        condition = checkDown(yow,zelement,group,map,frontier,explored,p)
        condition = checkUp(yow,zelement,group,map,frontier,explored,p)
        if 0 <= zelement < len(map[0]):
            condition1 = checkRight(yow,zelement,group,map,frontier,explored,p)
            condition1 = checkLeft(yow,zelement,group,map,frontier,explored,p)
                        
    if choose == 1:
        condition = checkUp(yow,zelement,group,map,frontier,explored,p)
        condition = checkDown(yow,zelement,group,map,frontier,explored,p)
        if 0 <= zelement < len(map[0]):
            condition1 = checkLeft(yow,zelement,group,map,frontier,explored,p)
            condition1 = checkRight(yow,zelement,group,map,frontier,explored,p)
    
    if (condition or condition1) or (condition and condition) == 1:
        return 1
    
    print (frontier,explored)
    return 0


findStart(mapRow,mapRowElement,map)
row , element = findStart(mapRow,mapRowElement,map)
group = row, element
frontier.append (group)
look(row, element, map, frontier, explored)