import re

puzzleInputFile = "puzzleInput.txt"

def readFile(fileName):
  with open(fileName, "r") as file:
    return file.read().splitlines()
  
puzzleInput = readFile(puzzleInputFile)

seeds = []
maps = {}
phase = 0

for idx, line in enumerate(puzzleInput):
  if idx == 0:
    seeds = [int(x) for x in line.split(': ')[1].split(' ')]
    # print("seeds: " + str(seeds))
    continue

  if line == '':
    continue
  
  if re.search('[a-zA-Z]', line):
    phase += 1
    maps[phase] = []
    continue

  phaseInfo = line.split(' ')
  # print("phase: " + str(phase) + ". ", phaseInfo)

  source = int(phaseInfo[1])
  destination = int(phaseInfo[0])
  rangeInfo = int(phaseInfo[2])-1

  maps[phase].append([[source, source+rangeInfo], [destination, destination+rangeInfo]])

phaseValues = {}
for seed in seeds:
  phaseValues[seed] = seed
  for phase, values in maps.items():
    for phaseRanges in values:
      
      if phaseRanges[0][0] <= phaseValues[seed] <= phaseRanges[0][1]:
        index = phaseValues[seed] - phaseRanges[0][0]
        phaseValues[seed] = phaseRanges[1][0] + index
        break

lowestValue = 0
for seed, value in phaseValues.items():
  if lowestValue == 0 or value < lowestValue:
    lowestValue = value

print("part 1: " + str(lowestValue))



#----- PART 2




seeds = []
seedsRanges = []
maps = {}
phase = 0

for idx, line in enumerate(puzzleInput):
  if idx == 0:
    seeds = [int(x) for x in line.split(': ')[1].split(' ')]
    for idx, seed in enumerate(seeds):
      if idx % 2:
        pass
      else:
        seedsRanges.append([seed, seeds[idx+1]])
    continue

  if line == '':
    continue
  
  if re.search('[a-zA-Z]', line):
    phase += 1
    maps[phase] = []
    continue

  phaseInfo = line.split(' ')

  source = int(phaseInfo[1])
  destination = int(phaseInfo[0])
  rangeInfo = int(phaseInfo[2])-1

  maps[phase].append([[source, source+rangeInfo], [destination, destination+rangeInfo]])

phaseValues = {}
lowestValue = 0
for seedRange in seedsRanges:
  seed = seedRange[0]
  while seed <= seedRange[0]+seedRange[1]:
    phaseValues[seed] = seed
    for phase, values in maps.items():
      for phaseRanges in values:
        if phaseRanges[0][0] <= phaseValues[seed] <= phaseRanges[0][1]:
          index = phaseValues[seed] - phaseRanges[0][0]
          phaseValues[seed] = phaseRanges[1][0] + index
          break
    if lowestValue == 0 or phaseValues[seed] < lowestValue:
      lowestValue = phaseValues[seed]
    seed += 1



print("part 2: " + str(lowestValue))