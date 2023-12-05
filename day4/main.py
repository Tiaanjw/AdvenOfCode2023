puzzleInputFile = "puzzleInput.txt"

def readFile(fileName):
  with open(fileName, "r") as file:
    return file.read()

puzzleInput = readFile(puzzleInputFile).splitlines()

rightWinningNumberCardsList = []
leftWinningNumberCardsList = []

for line in puzzleInput:
  rightWinningNumberCardsList.append(line.split('|')[1].strip().split())
  leftWinningNumberCardsList.append(line.split('|')[0].split(':')[1].strip().split())

pointsList = []
for idx, numberList in enumerate(leftWinningNumberCardsList):
  points = 0
  for number in numberList:
    if(number in rightWinningNumberCardsList[idx]):
      if(points == 0):
        points = 1
      else:
        points *= 2
  pointsList.append(points)

total = sum(pointsList)
print("Part 1: " + str(total))



#----- part 2

rightWinningNumberCardsList = []
leftWinningNumberCardsList = []
cardsList = {}

for idx, line in enumerate(puzzleInput):
  rightWinningNumberCardsList.append(line.split('|')[1].strip().split())
  leftWinningNumberCardsList.append(line.split('|')[0].split(':')[1].strip().split())
  cardsList[idx+1] = {"matches": 0, "copies": 0}

# loop through list of winning numbers
for idx, numberList in enumerate(leftWinningNumberCardsList):
  mainCardIdx = idx+1
  matches = 0
  for number in numberList:
    if(number in rightWinningNumberCardsList[idx]):
      matches += 1
    cardsList[mainCardIdx]["matches"] = matches
  
  if matches > 0:
    nextCardIdx = mainCardIdx + 1
    if idx <= len(cardsList):
      cardMatches = int(cardsList[mainCardIdx]["matches"])
      cardAmount = int(cardsList[mainCardIdx]["copies"])+1
      for copy in range(0, cardAmount):
        for cardIdx in range(nextCardIdx, nextCardIdx + cardMatches):
          if cardIdx <= len(leftWinningNumberCardsList):
            cardsList[cardIdx]["copies"] += 1

total = 0
cardCount = 0
for card, info in cardsList.items():
  cardCount += 1
  total += info["copies"]

print("Part 2: " + str(total + cardCount))