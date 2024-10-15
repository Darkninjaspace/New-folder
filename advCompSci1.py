import math

# input your values here
arwwidth = 13       #with of the arrow
totallength= 30     #length of the arrow




x = "A"
arwcounter = arwwidth
space = ' '
spcamt = 0
spaceamtmain = math.floor(arwwidth/2)

for count1 in range (0,totallength,1):
    for count3 in range (0,spaceamtmain,1): 
        print (space,end="")
    print (x)
    

    if count1 > totallength-arwwidth-2:
        for i in range (0,spcamt,1):
            print (space,end="")
        for count2 in range (0,arwcounter,1):
            print (x,end="")
        arwcounter -= 2
        arwwidth -= 1
        spcamt += 1
        
        if arwcounter < 3:
            print ("")
            for count3 in range (0,spaceamtmain,1): 
                print (space,end="")
            print (x)
            break

        if count2 >= 2:
            print ("")