import re
import threading
import time
import multiprocessing

seeds = []
seedsRanges = []
maps = {}
phase = 0

puzzleInputFile = "puzzleInput.txt"

def readFile(fileName):
  with open(fileName, "r") as file:
    return file.read().splitlines()
  
puzzleInput = readFile(puzzleInputFile)

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



# # print(puzzleInput)
# seeds = []
# maps = {}
# phase = 0

# for idx, line in enumerate(puzzleInput):
#   if idx == 0:
#     seeds = [int(x) for x in line.split(': ')[1].split(' ')]
#     # print("seeds: " + str(seeds))
#     continue

#   if line == '':
#     continue
  
#   if re.search('[a-zA-Z]', line):
#     phase += 1
#     maps[phase] = []
#     continue

#   phaseInfo = line.split(' ')
#   # print("phase: " + str(phase) + ". ", phaseInfo)

#   source = int(phaseInfo[1])
#   destination = int(phaseInfo[0])
#   rangeInfo = int(phaseInfo[2])-1

#   maps[phase].append([[source, source+rangeInfo], [destination, destination+rangeInfo]])

# phaseValues = {}
# for seed in seeds:
#   phaseValues[seed] = seed
#   for phase, values in maps.items():
#     for phaseRanges in values:
      
#       if phaseRanges[0][0] <= phaseValues[seed] <= phaseRanges[0][1]:
#         index = phaseValues[seed] - phaseRanges[0][0]
#         phaseValues[seed] = phaseRanges[1][0] + index
#         break

# lowestValue = 0
# for seed, value in phaseValues.items():
#   if lowestValue == 0 or value < lowestValue:
#     lowestValue = value

# print("part 1: " + str(lowestValue))



#----- PART 2




def get_lowest_from_range(seedRange, lvs):
  # print(maps)
  # print(seedRange)
  seed = seedRange[0]
  lowestValue = 0
  while seed <= seedRange[1]:
    # print("seed: " + str(seed))
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
  # print("lowest: " + str(lowestValue))
  lvs.append(lowestValue)




phaseValues = {}
lowestValue = 0
threads = {}
tidx = 0

if __name__ == "__main__":
  manager = multiprocessing.Manager()
  lowestValues = manager.list()
  


  for seedRange in seedsRanges:
    # print(seedRange)
    start = seedRange[0]
    end = seedRange[0] + seedRange[1] - 1 
    batch = 1000000
    idx = 0
    # print([start, end], start+batch)
    while start < end: # 99 < 92
      idx += 1
      nextRange = start + batch # 89 + 10 = 99
      
      if start + batch > end: # 89 + 10 = 99 > 92
        nextRange = end # 92
      rangeToCheck = [start, nextRange] # 89,92
      # print("range to check: " + str(rangeToCheck))
      p = multiprocessing.Process(target=get_lowest_from_range, args=[rangeToCheck, lowestValues])
      threads[idx] = p
      p.start()
      # print("starting thread: " + str(idx))
      start += batch # 99
      # break
    # break

    # print(threads)
    for idx, proc in threads.items():
      while proc.is_alive():
        print("threads: " + str(len(threads)))
        time.sleep(1)



  # print(lowestValues)
  lowestValue = min(lowestValues)

  print("part 2: " + str(lowestValue))