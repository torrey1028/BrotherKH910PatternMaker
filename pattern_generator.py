class Stitch():
  def __init__(self) -> None:
    self.inStitchIDs = []
    self.outStitchID = None
    self.stitchesIn = None
    self.stitchesOut = None
    self.currentNeedle = None

class Knit(Stitch):
  def __init__(self) -> None:
    super().__init__()
    self.stitchesIn = 1
    self.stitchesOut = 1

class KnitTogetherRight(Stitch):
  def __init__(self) -> None:
    super().__init__()
    self.stitchesIn = 2
    self.stitchesOut = 1

class KnitTogetherLeft(Stitch):
  def __init__(self) -> None:
    super().__init__()
    self.stitchesIn = 2
    self.stitchesOut = 1

class YarnOver(Stitch):
  def __init__(self) -> None:
    super().__init__()
    self.stitchesIn = 0
    self.stitchesOut = 1

class KnitThreeTogether(Stitch):
  def __init__(self) -> None:
    super().__init__()
    self.stitchesIn = 3
    self.stitchesOut = 1

def validRow(row) -> bool:
  stitches_in = 0
  stitches_out = 0
  for item in row:
    print('stitches in: %d, stitches out: %d' % (item.stitchesIn, item.stitchesOut))
    stitches_in = stitches_in + item.stitchesIn
    stitches_out = stitches_out + item.stitchesOut
  return stitches_in == stitches_out

row = [
  Knit(),
  Knit(),
  YarnOver(),
  Knit(),
  Knit(),
  Knit(),
  YarnOver(),
  KnitTogetherRight(),
  KnitTogetherRight(),
  Knit(),
  Knit(),
  YarnOver(),
  KnitTogetherRight(),
  Knit(),
  Knit(),
  Knit(),
  Knit(),
]

passes = []

# stitch 0 is on left and stitch n in on right as you face the machine

def passLeftToRightPattern(stitches, row):
  needles = []
  for i in range(0, len(row)):
    item = row[i]
    if isinstance(item, KnitTogetherRight) or isinstance(item, KnitThreeTogether):
      # lower number needle will be pushed out to pass stitch right 
      stitch = min(item.inStitchIDs)
      needles.append(stitch)
      stitches[stitch + 1] = stitches[stitch] + stitches[stitch + 1]
      stitches[stitch] = 0
      item.currentNeedle = stitch + 1
  passes.append(needles)

def passRightToLeftPattern(stitches, row):
  needles = []
  for i in range(0, len(row)):
    item = row[i]
    if isinstance(item, KnitTogetherRight) or isinstance(item, KnitThreeTogether):
      # lower number needle will be pushed out to pass stitch right 
      stitch = max(item.inStitchIDs)
      needles.append(stitch)
      stitches[stitch - 1] = stitches[stitch] + stitches[stitch - 1]
      stitches[stitch] = 0 
      item.currentNeedle = stitch - 1
  passes.append(needles)

def parseNonPatternStitches(row):
  for i in range(0, len(row)):
    item = row[i]
    if isinstance(item, Knit):
      pass

def passLefttoRightMoveStitches(stitches, row):
  needles = []
  for item in row:
    if item.currentNeedle == None:
      continue
    if(item.currentNeedle < item.outStitchID):
      if(stitches[item.currentNeedle + 1] == 0):
        needles.append(item.currentNeedle)
        stitches[item.currentNeedle + 1] = stitches[item.currentNeedle] + stitches[item.currentNeedle + 1]
        stitches[item.currentNeedle] = 0
        item.currentNeedle = item.currentNeedle + 1
  passes.append(needles)

def passRighttoLeftMoveStitches(stitches, row):
  needles = []
  for item in row:
    if item.currentNeedle == None:
      continue
    if(item.currentNeedle > item.outStitchID):
      if(stitches[item.currentNeedle - 1] == 0):
        needles.append(item.currentNeedle)
        stitches[item.currentNeedle - 1] = stitches[item.currentNeedle] + stitches[item.currentNeedle - 1]
        stitches[item.currentNeedle] = 0
        item.currentNeedle = item.currentNeedle - 1
  passes.append(needles)


def checkRow(row) -> bool:
  for item in row:
    if (item.currentNeedle != item.outStitchID):
      return False
  return True

def processRow(row):
  stitches = []
  for _ in row:
    stitches.append(1)
  print(stitches)

  i = 0
  j = 0
  for item in row:
    if isinstance(item, YarnOver):
      j = j + 1
      continue
    item.outStitchID = j
    if isinstance(item, KnitTogetherLeft) or isinstance(item, KnitTogetherRight):
      item.inStitchIDs.append(i)
      item.inStitchIDs.append(i + 1)
      i = i + 2
    elif isinstance(item, KnitThreeTogether):
      item.inStitchIDs.append(i)
      item.inStitchIDs.append(i + 1)
      item.inStitchIDs.append(i + 2)
      i = i + 3
    elif isinstance(item, Knit):
      item.inStitchIDs.append(i)
      item.currentNeedle = i
      i = i + 1  
    j = j + 1  

  passRightToLeftPattern(stitches, row)
  passLeftToRightPattern(stitches, row)

  while(not checkRow(row)):
     passRighttoLeftMoveStitches(stitches, row)
     passLefttoRightMoveStitches(stitches, row)

  return passes
      

def main():
  if(validRow(row)):
    processRow(row)
    print('done!')
  else:
    print('Invalid row!')
  

if __name__ == "__main__":
  main()

