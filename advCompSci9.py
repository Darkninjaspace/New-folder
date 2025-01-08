h = "house"
e = "empty"
H = "hospital"
x = 0
y = 0

mapRow = 0
mapRowElement = 0

map = [[e, e, e, e, e, h, e, h, e, e, e, e, e, e, e, e, e, e, e,e],
      [e, h, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, h, e, h],
      [e, e, e, e, e, e, e, e, e, e, e, e, h, e, e, e, e, e, e, e],
      [e, e, e, e, e, e, e, e, e, e, e, e, e, e, h, e, e, e, h, e],
      [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, h, e],
      [e, e, e, e, e, h, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
      [e, h, h, H, e, e, e, e, e, e, e, H, e, e, e, e, e, e, h, e],
      [e, e, e, e, e, e, e, e, e, e, e, e, e, h, e, e, e, e, e, e],
      [e, e, e, e, e, e, h, e, e, e, e, e, e, e, e, e, e, e, e, e],
      [e, e, e, e, e, H, e, e, e, e, e, e, e, e, e, e, e, e, e, e]]
      

def findPlaces(mapRow,mapRowElement,map,row,col):
   housePlaces = []
   hospitalPlaces = []
   for i in range (0,row,1):
      col = len(map[mapRow])
      for p in range (0,col,1):
         if "house" == map[mapRow][mapRowElement]:
            startPosRowElement = mapRowElement
            startPosRow = mapRow
            group = (startPosRow),(startPosRowElement)
            housePlaces.append(group)
         if "hospital" == map[mapRow][mapRowElement]:
            startPosRowElement = mapRowElement
            startPosRow = mapRow
            group = (startPosRow),(startPosRowElement)
            hospitalPlaces.append(group)
         mapRowElement += 1
      mapRow += 1
      mapRowElement = 0
   return housePlaces, hospitalPlaces

def expand_circles(housePlaces, mapSize):
   circlePoints = {}
   for i in housePlaces:
      radius = 0
      while True:
            radius += 1
            inCircle = findPointsInCircle(i, radius, mapSize)
            if any(p in housePlaces for p in inCircle if p != i):
               break
            for p in inCircle:
               circlePoints[p] = circlePoints.get(p, 0) +1
   return circlePoints

def findPointsInCircle(center, radius, mapSize):
   circleX, circleY = center
   points = []
   for x in range(circleX-radius,circleX+radius+1,1):
      for y in range(circleY-radius,circleY+radius+1,1):
            if checkIncluded(x,circleX,y,circleY,radius)<= radius:
               points.append((x,y))
   return points

def checkIncluded (x,circleX,y,circleY,radius):
   distance = ((x-circleX)**2 + (y-circleY)**2) ** 0.5 
   return distance

def sortPoints(circlePoints):
   chosenPoints = []
   sortedPoints = sorted(circlePoints.items(), key=lambda x: x[1], reverse=True)
   for point,trash in sortedPoints:
      chosenPoints.append(point)
   return chosenPoints

def checkHouseCost(houseList, hospitalList):
   totalCost = 0
   for house in houseList:
      houseX, houseY = house
      smallestDist = 100000000
      for hospital in hospitalList:
            hospitalX, hospitalY = hospital
            distance = abs(houseX-hospitalX)+abs(houseY-hospitalY)
            smallestDist = min(smallestDist, distance)
      totalCost += smallestDist
   return totalCost

def findHospital(map, hospitalAmt):
   circlePoints = expand_circles(houseList, mapSize)
   possiblePoints = sortPoints(circlePoints)

   finalPoints = []
   
   finalCost = 10000000000

   for i in range(0,len(possiblePoints)-hospitalAmt+1,1):
      hospital_combination = possiblePoints[i:i+hospitalAmt]
      totalCost = checkHouseCost(houseList, hospital_combination)
      if totalCost < finalCost:
            finalCost = totalCost
            finalPoints = hospital_combination

   return finalPoints, finalCost

row = len(map)
col = len(map[0])
mapSize = (row, col)
houseList, hospitalList = findPlaces(mapRow, mapRowElement, map, row, col)   
hospitalAmt = len(hospitalList)
finalPoints, finalCost = findHospital(map, hospitalAmt)
print("hospital locations:",finalPoints,"total cost = ",finalCost)
#heheheheh HAR HAR HAR o(*￣▽￣*)ブ
