def transform(x):
  return int(x)

def splitString(string):
  characters = []
  size = len(string)
  i = 0
  while(i < size):
    if string[i] not in characters:
      characters.append(string[i])
    i += 1
  return characters

def sumOfStages(alphabetMap, rocket):
  result = 0
  for stage in rocket:
    result += alphabetMap[stage]
  return result

def createAlphabetMap():
  alphabetMap = {}
  alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
  i = 1
  for letter in alphabet:
    alphabetMap[letter] = i
    i += 1
  return alphabetMap

(n, k) = tuple(map(transform, input().split()))
s = splitString(input())
alphabetMap = createAlphabetMap()
sortedS = sorted(s)

#nao pode pegar a proxima letra, tem que pegar a segunda na sequencia
#ou seja, se eu pego A, soh posso pegar C

rocket = []
for stage in sortedS:
  charactersArraySize = len(rocket)
  if charactersArraySize != 0 and charactersArraySize < k:
    if alphabetMap[stage] >= alphabetMap[rocket[charactersArraySize-1]] + 2:
      rocket.append(stage)
  else:
    if charactersArraySize < k:
      rocket.append(stage)

if len(rocket) < k:
  print(str(-1))
else:
  result = sumOfStages(alphabetMap,rocket)
  print(result)