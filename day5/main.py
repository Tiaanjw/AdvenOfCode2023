import re
import time
import multiprocessing

def readFile(fileName):
  with open(fileName, "r") as file:
    return file.read()
  
def parsePuzzleInput(puzzleInputFile):
  seeds = []
  seedsRanges = []
  maps = {}
  phase = 0

  for idx, line in enumerate(readFile(puzzleInputFile).splitlines()):
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

  return {"maps": maps, "seeds": seeds, "seedsRanges": seedsRanges}

def partOne(puzzleInput):
  seeds = puzzleInput["seeds"]
  maps = puzzleInput["maps"]
  phaseValues = {}
  lowestValue = 0

  for seed in seeds:
    phaseValues[seed] = seed
    for phase, values in maps.items():
      for phaseRanges in values:
        if phaseRanges[0][0] <= phaseValues[seed] <= phaseRanges[0][1]:
          index = phaseValues[seed] - phaseRanges[0][0]
          phaseValues[seed] = phaseRanges[1][0] + index
          break
  
  for seed, value in phaseValues.items():
    if lowestValue == 0 or value < lowestValue:
      lowestValue = value

  return lowestValue


#----- PART 2

def get_lowest_from_range(seedRange, lvs, maps):
  phaseValues = {}
  seed = seedRange[0]
  lowestValue = 0
  while seed <= seedRange[1]:
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

  lvs.append(lowestValue)


def partTwo(puzzleInput):
  maps = puzzleInput["maps"]
  seedsRanges = puzzleInput["seedsRanges"]
  procs = {}
  manager = multiprocessing.Manager()
  lowestValues = manager.list()

  for seedRange in seedsRanges:
    start = seedRange[0]
    end = seedRange[0] + seedRange[1] - 1 
    batch = 1000000
    idx = 0

    while start < end:
      idx += 1
      nextRange = start + batch
      if start + batch > end:
        nextRange = end
      rangeToCheck = [start, nextRange]

      p = multiprocessing.Process(target=get_lowest_from_range, args=[rangeToCheck, lowestValues, maps])
      procs[idx] = p
      p.start()
      start += batch

    for idx, proc in procs.items():
      while proc.is_alive():
        # print("Procs: " + str(len(procs)))
        time.sleep(0.5)

  return min(lowestValues)

if __name__ == "__main__":
  puzzleInput = parsePuzzleInput("puzzleInput.txt")
  print("Part 1: " + str(partOne(puzzleInput)))
  print("Part 2: " + str(partTwo(puzzleInput)))