from PIL import Image

import numpy
import pattern_generator as gen

# row = [
#   gen.Knit(),
#   gen.Knit(),
#   gen.YarnOver(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.YarnOver(),
#   gen.KnitTogetherRight(),
#   gen.KnitTogetherRight(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.YarnOver(),
#   gen.KnitTogetherRight(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.Knit(),
#   gen.KnitTogetherRight(),
#   gen.Knit(),
#   gen.Knit(), 
#   gen.YarnOver(),

# ]

pattern = []

# row 0
row = []
gen.insert(row, gen.Knit, 2)
row.append(gen.YarnOver())
gen.insert(row, gen.Knit, 4)
row.append(gen.YarnOver())
gen.insert(row, gen.KnitTogetherRight, 2)
gen.insert(row, gen.Knit, 2)
row.append(gen.YarnOver())
row.append(gen.KnitTogetherRight())
gen.insert(row, gen.Knit, 4)
row.append(gen.KnitTogetherRight())
gen.insert(row, gen.Knit, 2)
row.append(gen.YarnOver())
gen.insert(row, gen.Knit, 8)
row.append(gen.KnitTogetherRight())
gen.insert(row, gen.Knit, 2)
row.append(gen.YarnOver())
gen.insert(row, gen.Knit, 6)
pattern.append(row)

# row 1
row1 = []
gen.insert(row1, gen.Knit, 2)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 5)
row1.append(gen.YarnOver())
row1.append(gen.KnitThreeTogether())
gen.insert(row1, gen.Knit, 2)
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 3)
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 2)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 8)
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 2)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 7)
pattern.append(row1)

# row 2
row2 = []
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 5)
row2.append(gen.YarnOver())
row2.append(gen.KnitThreeTogether())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 3)
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 8)
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 7)
pattern.append(row2)




def imageAddRow(img_row, img, start) -> int:
  for item in img_row:
    img[start, item] = [255,0,0]
  return start - 1
  

def main():
  y_max = 150
  data = numpy.zeros((y_max, len(row), 3), dtype=numpy.uint8)
  offset = y_max - 1
  for r in pattern:
    valid = gen.validRow(r)
    if (valid):
      passes = gen.processRow(r)
      for p in passes:
        print(p)
        offset = imageAddRow(p, data, offset)
    else:
      exit(1)

  image = Image.fromarray(data)
  image.show()
    
  

if __name__ == "__main__":
  main()