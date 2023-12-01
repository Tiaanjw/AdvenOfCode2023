puzzleInputFile = "puzzleInput.txt"

def readFile(fileName):
  with open(fileName, "r") as file:
    return file.read()


#PART 1
total = 0
for line in readFile(puzzleInputFile).splitlines():
  res = list(filter(lambda x: x.isdigit(), line))
  firstAndLastDigits = int(res[0] + res[-1])
  total += firstAndLastDigits
  
print(f'Part 1 answer: {total}')


# PART 2
total = 0
def findMatches(inputString, dict):
  matches = []
  i = 0
  while i < len(inputString):
    for key, value in dict.items():
      if (inputString[i:i+len(value)] == value or inputString[i] == str(key)):
        matches.append(str(key))
        i += 1
        break
    else:
      i += 1
  return matches

completeList = []
digitDictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
for line in readFile(puzzleInputFile).splitlines():
  res = findMatches(line, digitDictionary)
  firstAndLastDigits = int(res[0] + res[-1])
  total += firstAndLastDigits
  
print(f'Part 2 answer: {total}')