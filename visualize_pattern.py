from PIL import Image

import numpy
import pattern_generator as gen

# Geometric pattern
pattern6 = []

row0 = []
gen.insert(row0, gen.Knit, 1)
row0.append(gen.YarnOver())
row0.append(gen.KnitTogetherRight())
gen.insert(row0, gen.Knit, 4)
row0.append(gen.YarnOver())
row0.append(gen.KnitTogetherRight())
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 4)
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 1)
pattern6.append(row0)
pattern6.append(row0)
pattern6.append(row0)
pattern6.append(row0)

row1 = []
gen.insert(row1, gen.Knit, 1)
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 12)
row1.append(gen.KnitTogetherLeft())
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 1)
pattern6.append(row1)

row2 = []
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 10)
row2.append(gen.KnitTogetherLeft())
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 2)
pattern6.append(row2)

row3 = []
gen.insert(row3, gen.Knit, 3)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 8)
row3.append(gen.KnitTogetherLeft())
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 3)
pattern6.append(row3)

row4 = []
gen.insert(row4, gen.Knit, 4)
row4.append(gen.YarnOver())
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 6)
row4.append(gen.KnitTogetherLeft())
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 4)
pattern6.append(row4)

row5 = []
gen.insert(row5, gen.Knit, 5)
row5.append(gen.YarnOver())
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 4)
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 5)
pattern6.append(row5)

row6 = []
gen.insert(row6, gen.Knit, 6)
row6.append(gen.YarnOver())
row6.append(gen.KnitTogetherRight())
gen.insert(row6, gen.Knit, 2)
row6.append(gen.KnitTogetherLeft())
row6.append(gen.YarnOver())
gen.insert(row6, gen.Knit, 6)
pattern6.append(row6)

row7 = []
gen.insert(row7, gen.Knit, 7)
row7.append(gen.YarnOver())
row7.append(gen.KnitTogetherRight())
row7.append(gen.KnitTogetherLeft())
row7.append(gen.YarnOver())
gen.insert(row7, gen.Knit, 7)
pattern6.append(row7)

row8 = []
gen.insert(row8, gen.Knit, 1)
row8.append(gen.YarnOver())
row8.append(gen.KnitTogetherRight())
gen.insert(row8, gen.Knit, 4)
row8.append(gen.YarnOver())
row8.append(gen.KnitTogetherRight())
row8.append(gen.KnitTogetherLeft())
row8.append(gen.YarnOver())
gen.insert(row8, gen.Knit, 4)
row8.append(gen.KnitTogetherLeft())
row8.append(gen.YarnOver())
gen.insert(row8, gen.Knit, 1)
pattern6.append(row8)

def imageAddRow(img_row, img, start) -> int:
  for item in img_row:
    img[start, item] = [255,0,0]
  return start - 1
  

def createPattern(pattern):
  y_max = 150
  data = numpy.zeros((y_max, len(pattern[0]), 3), dtype=numpy.uint8)
  offset = y_max - 1
  for r in pattern:
    valid = gen.validRow(r)
    if (valid):
      passes = gen.processRow(r)
      for p in passes:
        print(p)
        offset = imageAddRow(p, data, offset)
      print("knit")
    else:
      print("not valid")
      exit(1)

  image = Image.fromarray(data)
  image.show()
  

if __name__ == "__main__":
  createPattern(pattern5)