h = "house"
e = "empty"
H = "hospital"

mapRow = 0
mapRowElement = 0

map =  [[e,e,e,e,h,e],
        [e,h,e,e,e,e],
        [e,e,e,e,h,e]]

def findHouses(mapRow,mapRowElement,map):
        places = []
        mapLength = len(map)
        for i in range (0,mapLength,1):
                rowLength = len(map[mapRow])
                for p in range (0,rowLength,1):
                        if "house" == map[mapRow][mapRowElement]:
                                startPosRowElement = mapRowElement
                                startPosRow = mapRow
                                #print (startPosRow,startPosRowElement)
                                group = (startPosRow),(startPosRowElement)
                                places.append(group)
                        mapRowElement += 1
                mapRow += 1
                mapRowElement = 0
        print(places)
        return places

def choosePostition(map):
        selecRow = len(map)
        for i in range (0,selecRow,1):
                selecSquare = len(map[i])
                for p in range (0,selecSquare,1):
                        return i,p

def findRange(map):
        range = 0
        hospitalX, hospitalY = choosePostition(map)
        houseAmt = len(findHouses(mapRow,mapRowElement,map))
        houseList = findHouses(mapRow,mapRowElement,map)
        for i in range (0,houseAmt,1):
                houseX, houseY = houseList[i]
                
        
#selecSquare and selecRow are actually lengths
def findPosition(map):
        placeholder

findHouses(mapRow,mapRowElement,map)