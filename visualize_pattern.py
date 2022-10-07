from PIL import Image

import numpy
import pattern_generator as gen

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
gen.insert(row2, gen.Knit, 6)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 6)
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 8)
pattern.append(row2)

# row 3
row3 = []
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 7)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 1)
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 5)
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 9)
pattern.append(row3)

# row 4
row4 = []
gen.insert(row4, gen.Knit, 1)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 8)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 4)
row4.append(gen.YarnOver())
row4.append(gen.KnitTogetherRight())
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 2)
row4.append(gen.YarnOver())
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 4)
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 2)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 8)
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 1)
pattern.append(row4)

# row 5
row5 = []
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 9)
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 5)
row5.append(gen.YarnOver())
row5.append(gen.KnitThreeTogether())
gen.insert(row5, gen.Knit, 2)
row5.append(gen.YarnOver())
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 3)
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 2)
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 8)
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 2)
pattern.append(row5)




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