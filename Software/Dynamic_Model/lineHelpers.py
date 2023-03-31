import cv2
import copy
import math

#line (x1,y1) to (x2, y2)
def displayLine(frame, line):
	cv2.line(frame, line[0], line[1], color=(0,0,255), thickness=2)

def calcSideOfLine(centerX, centerY, line):
	x1 = line[0][0]
	x2 = line[1][0]
	y1 = line[0][1]
	y2 = line[1][1]
	d = (centerX-x1)*(y2-y1)-(centerY-y1)*(x2-x1)
	return d

def pointIsWithinLine(pt, line, frame):
	lineSlope = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])

	dist = math.sqrt(math.pow(line[1][1] - line[0][1], 2) + math.pow(line[1][0] - line[0][0], 2))
	perpAng = math.pi/2

	sideLines = []
	for side in line:
		newLine = (int(1 * (dist/2)), int(lineSlope * (dist/2)))
		newLine = (newLine[0] * math.cos(perpAng) - newLine[1] * math.sin(perpAng), newLine[1] * math.cos(perpAng) + newLine[0] * math.sin(perpAng))
		newLine = (int(newLine[0] + side[0]), int(newLine[1] + side[1]))

		newLine2 = (int(1 * (dist/2)), int(lineSlope * (dist/2)))
		newLine2 = (newLine2[0] * math.cos(perpAng - math.pi) - newLine2[1] * math.sin(perpAng - math.pi), newLine2[1] * math.cos(perpAng - math.pi) + newLine2[0] * math.sin(perpAng - math.pi))
		newLine2 = (int(newLine2[0] + side[0]), int(newLine2[1] + side[1]))

		sideLines.append((newLine,newLine2))
		cv2.line(frame, newLine, newLine2, color=(0,255,0), thickness=2)

	side1 = calcSideOfLine(pt[0], pt[1], sideLines[0]) >= 0
	side2 = calcSideOfLine(pt[0], pt[1], sideLines[1]) >= 0

	if side1 == side2:
		return False

	return True

def crossLine(currentDetections, prevLineSides, frame, lines):
	newLineSides = copy.deepcopy(prevLineSides)

	for l in newLineSides.keys():
		for carIndex in range(len(newLineSides[l].keys())-1, -1, -1):
			carId = list(newLineSides[l].keys())[carIndex]
			if carId not in currentDetections.values():
				newLineSides[l].pop(carId)

	#bufferFrames = 1 means as soon at the dot crosses, it will register as the car crossing
	#bufferFrames = 5 means there must be 5 consecutive frames on the opposite side to register it crossing the line
	bufferFrames = 1
	crosses = {}

	for lineI in range(len(lines)):
		if lineI not in newLineSides.keys():
			newLineSides[lineI] = {}
		for detect in currentDetections.keys():
			centerX = detect[0]
			centerY = detect[1]

			d = calcSideOfLine(centerX, centerY, lines[lineI])

			id = currentDetections[detect]
			#print(id, (centerX, centerY), d)

			if id not in newLineSides[lineI]:
				newLineSides[lineI][id] = {'cnt': bufferFrames+2, 'side':(d >= 0), 'crossedBothLines':0}

			if newLineSides[lineI][id]['side'] == (d >= 0):
				newLineSides[lineI][id]['cnt'] += 1
			else:
				newLineSides[lineI][id]['cnt'] = 0
				newLineSides[lineI][id]['side'] = (d >= 0)

			if lineI not in prevLineSides:
				continue
			if id in prevLineSides[lineI].keys():
				if newLineSides[lineI][id]['cnt'] >= bufferFrames and prevLineSides[lineI][id]['cnt'] < bufferFrames and pointIsWithinLine((centerX, centerY), lines[lineI], frame):
					if not newLineSides[lineI][id]['side']:
						newLineSides[lineI][id]['crossedBothLines'] = 1;
					crosses[id] = {'line':lineI, 'from': not newLineSides[lineI][id]['side'], 'to': newLineSides[lineI][id]['side'], 'crossedBothLines': newLineSides[lineI][id]['crossedBothLines']}

	return newLineSides, crosses
