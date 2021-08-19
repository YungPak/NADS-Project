import sys 
import random

# Hard Coded Car 
VehicleBrand = "Audi"
VehicleWidth = 6.17
VehicleLength = 16.52
VehicleColors = 5 

newList = []

newList.append(VehicleBrand)
newList.append(str(VehicleWidth))
newList.append(str(VehicleLength))
newList.append(str(VehicleColors))

userinput = input("Enter the Name of The File You Want to Read: ")
my_file = userinput

try:
    with open(my_file) as f:
        content = [line.rstrip('\n') for line in f]

except:
    print ("Error: Unable to open file", my_file)
    exit()

try:
    with open(my_file) as f:
        content = [line.rstrip('\n') for line in f]
           
except:
    print ("Unable to open file", my_file)
    sys.exit()

def check_for_floats(point):
    for item in point:
        if '.' not in item:
            return 'FALSE'
        else:
            pass      
    return 'TRUE'

def implode_list(input): # decompress list of lists
    imploded_list = [x for sublist in '''m''' for x in sublist]

    return imploded_list    

proc_rec = ''
road_start = 'LONGCURVE'
end_rec = '}'
end_roads = 'INTERSECTIONS'
all_road_points = []
road_points = []
road_count = 0
new_string=''

newValueList = []
xValList = []
yValList = []

ranNumList = []

xListIndex = []

zz = 0

def lengthCalcFix():

    # Removes Blank Spots from List 
    while '' in valueList:
        valueList.remove('')

    global zz 
    
    while zz < len(valueList):

        tempValuelist = valueList[zz]
        xx = tempValuelist.split(' ')
        newValueList.append(xx) 

        (xVal , yVal , zVal) = xx # Seperates the Tuple 
        
        xValList.append(xVal) #Adds The Values to the list 
        yValList.append(yVal)
        
        zz += 1


    # Takes the string and converts to floats 
    for countXVal in range(0, len(xValList)):
        xValList[countXVal] = abs(float(xValList[countXVal]))

    for countYVal in range(0, len(yValList)):
        yValList[countYVal] = abs(float(yValList[countYVal]))

# for each road, construct XYZ list until end of road
# then push road points into all_roads list

valueList = []

for x in content:
    data_line = x.split()
    data_len = len(data_line)

    if road_start in data_line: # New road
        road_count += 1
        road_points.append(data_line[2:5]) 

    elif (data_len == 6): # robust error check required here; all items in line must contain a decimal;

        my_flag = check_for_floats(data_line[0:3])
        if my_flag == 'TRUE':
            road_points.append(data_line[0:3])
        else:
            pass

    elif (end_rec in data_line) and (data_len == 7) and ('n' not in data_line): # n exclusion for BORDER
        my_flag = check_for_floats(data_line[0:3])
        if my_flag == 'TRUE':
            road_points.append(data_line[0:3])

# list of all road points

            all_road_points.append(road_points)

            lengthCalcFix()
            xValList.append(road_count)

            xListIndex.append(len(xValList))

            
            yValList.append(road_count)

            print()
            print ("Road #"  , road_count)

            for rp in road_points:
                new_string=' '.join(rp)
                valueList.append(new_string) #Adds Roadpoints to List
                print (new_string) # print road points

            road_points = []
        else:
            pass
        
    elif (data_len == 1) and (end_roads in data_line):
        break
    else:
        continue

v_count,last_v_count,p_count = 0,0,0

for i in all_road_points:
    p_count = (len(i)/3)

    for x in i:
        if len(x) >0:
            v_count += 1
            coord_list = str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2])
            valueList.append(coord_list)
            lengthCalcFix()
            print (coord_list) #Helps Print Road 7 

print("")
print ('Total road count is:', road_count)
print("")

xValListCount = []

xValList.append(road_count + 1)

def xlengthCalc(): #Calulates Length of the X & Y lists 
    xValListCopy = xValList
    yValListCopy = yValList
    xCounter = 1
    xEle = 0

    while(xCounter <= road_count): #interation for each specfic road 

        xValListIndex = xValListCopy.index(xCounter)

        del xValListCopy[xValListIndex] # Removes Variable Place Holder
        del yValListCopy[xValListIndex]

        xValListIndex = xValListCopy.index(xCounter + 1) # Helps recognize second index value

        # Calculates the Random Number for RoadPos 
        ranNum = random.randrange(2 , xValListIndex - 2 )
        ranNumList.append(ranNum)
        
        xDiff = 0
        yDiff = 0
        xTotal = 0
        yTotal = 0

        while (xEle  < xValListIndex): # Iterates through the list for calulcations 

            xDiff = xValListCopy[xEle] - xValListCopy[xEle - 1 ]
            yDiff = yValListCopy[xEle] - yValListCopy[xEle - 1]

            xTotal = xTotal + abs(xDiff)
            yTotal = yTotal + abs(yDiff)

            xEle = xEle + 1
        print ("Total Value for road #", xCounter , "X-Value",  int(xTotal), "Y-Value" , int(yTotal))
        xCounter = xCounter + 1
    print("")
xlengthCalc()


def carPlacement(): # Finds The Correct RoadNumber for the IndexValue of the Car
    ranNumChoice = random.choice(ranNumList)

    xIndexCount = 0
    global roadID
    roadID = 0
    ListIndexLen = len(xListIndex) - 1

    while (xIndexCount <= ListIndexLen):
        if (xListIndex[xIndexCount] < ranNumChoice): # Identifies values that are less than then RanNum Index Value tells us road number
            roadID = roadID + 1 
        xIndexCount = xIndexCount + 1

    global xRoadPos
    global yRoadPos

    xRoadPos = str(xValList[ranNumChoice])
    yRoadPos = str(yValList[ranNumChoice])
 
carPlacement()

roadNumber = str(roadID) 
print("---------------------------------------------")
print("Road Number: ", roadNumber) 
print("Road Postion: " , xRoadPos , " : " , yRoadPos)
print("---------------------------------------------")

# Output Print to File

outF = open("myOutFile.txt", "w")

outF.write("LRI File: ")
outF.write(my_file)
outF.write("\n")

outF.write("VehicleBrand: ")
outF.write(VehicleBrand)
outF.write("\n")  

outF.write("VehicleWidth: ")
outF.write(newList[1])
outF.write("\n")

outF.write("VehicleLength: ")
outF.write(newList[2])
outF.write("\n")

outF.write("VehicleColor: ")
outF.write(newList[3])
outF.write("\n")

outF.write("Road Number: " )
outF.write(roadNumber)
outF.write("\n")

outF.write("Road Postion: " )
outF.write(xRoadPos)
outF.write(" : ")
outF.write(yRoadPos)

outF.close()

print("")
exit()
