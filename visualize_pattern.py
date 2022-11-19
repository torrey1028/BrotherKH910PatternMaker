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


pattern2 = []

row0 = []
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
row0.append(gen.Knit())
row0.append(gen.Knit())
pattern2.append(row0)

row1 = []
row1.append(gen.KnitTogetherLeft())
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherLeft())
row1.append(gen.Knit())
row1.append(gen.YarnOver())
row1.append(gen.Knit())
pattern2.append(row1)

row2 = []
row2.append(gen.KnitTogetherLeft())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.YarnOver())
pattern2.append(row2)

row3 = []
row3.append(gen.KnitTogetherLeft())
row3.append(gen.Knit())
row3.append(gen.Knit())
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherLeft())
row3.append(gen.YarnOver())
pattern2.append(row3)

row4 = []
row4.append(gen.KnitTogetherLeft())
row4.append(gen.Knit())
row4.append(gen.YarnOver())
row4.append(gen.Knit())
row4.append(gen.KnitTogetherLeft())
row4.append(gen.YarnOver())
pattern2.append(row4)

row5 = []
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
row5.append(gen.Knit())
row5.append(gen.Knit())
row5.append(gen.Knit())
row5.append(gen.Knit())
pattern2.append(row5)

pattern3 = []
row1 = []
row1.append(gen.Knit())
row1.append(gen.Knit())
row1.append(gen.KnitTogetherRight())
row1.append(gen.YarnOver())
row1.append(gen.Knit())
row1.append(gen.Knit())
pattern3.append(row1)

row2 = []
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
pattern3.append(row2)

row3 = []
row3.append(gen.Knit())
row3.append(gen.Knit())
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherLeft())
row3.append(gen.Knit())
row3.append(gen.Knit())
pattern3.append(row3)

row4 = []
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
pattern3.append(row4)

pattern4 = []

row0 = []
gen.insert(row0, gen.Knit, 5)
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 3)
row0.append(gen.YarnOver())
row0.append(gen.KnitTogetherRight())
gen.insert(row0, gen.Knit, 2)
pattern4.append(row0)

row1 = []
gen.insert(row1, gen.Knit, 4)
row1.append(gen.KnitTogetherLeft())
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 5)
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 1)
pattern4.append(row1)

row2 = []
gen.insert(row2, gen.Knit, 3)
row2.append(gen.KnitTogetherLeft())
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 1)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 4)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
pattern4.append(row2)

row3 = []
gen.insert(row3, gen.Knit, 2)
row3.append(gen.KnitTogetherLeft())
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 3)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 5)
pattern4.append(row3)

row4 = []
gen.insert(row4, gen.Knit, 1)
row4.append(gen.KnitTogetherLeft())
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 5)
row4.append(gen.YarnOver())
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 4)
pattern4.append(row4)

row5 = []
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 4)
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 1)
row5.append(gen.YarnOver())
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 3)
pattern4.append(row5)

# leaf pattern
pattern5 = []

row0 = []
gen.insert(row0, gen.Knit, 1)
row0.append(gen.KnitTogetherLeft())
gen.insert(row0, gen.Knit, 4)
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 3)
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 2)
row0.append(gen.KnitTogetherRight())
pattern5.append(row0)

row1 = []
row1.append(gen.KnitTogetherLeft())
gen.insert(row1, gen.Knit, 4)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 5)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 1)
row1.append(gen.KnitTogetherRight())
pattern5.append(row1)

row2 = []
row2.append(gen.KnitTogetherLeft())
gen.insert(row2, gen.Knit, 3)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 1)
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 4)
row2.append(gen.KnitTogetherRight())
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
pattern5.append(row2)

row3 = []
row3.append(gen.KnitTogetherLeft())
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 3)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 4)
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 1)
pattern5.append(row3)

row4 = []
row4.append(gen.KnitTogetherLeft())
gen.insert(row4, gen.Knit, 1)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 5)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 4)
row4.append(gen.KnitTogetherRight())
pattern5.append(row4)

row5 = []
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
row5.append(gen.KnitTogetherLeft())
gen.insert(row5, gen.Knit, 4)
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 1)
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 3)
row5.append(gen.KnitTogetherRight())
pattern5.append(row5)

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
  

def main():
  y_max = 150
  data = numpy.zeros((y_max, len(row), 3), dtype=numpy.uint8)
  offset = y_max - 1
  for r in pattern6:
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
  main()