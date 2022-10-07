from PIL import Image

import numpy
import pattern_generator as gen

row = [
  gen.Knit(),
  gen.Knit(),
  gen.YarnOver(),
  gen.Knit(),
  gen.Knit(),
  gen.Knit(),
  gen.YarnOver(),
  gen.KnitTogetherRight(),
  gen.KnitTogetherRight(),
  gen.Knit(),
  gen.Knit(),
  gen.YarnOver(),
  gen.KnitTogetherRight(),
  gen.Knit(),
  gen.Knit(),
  gen.Knit(),
  gen.Knit(),
]

def imageAddRow(img_row, img, start) -> int:
  for item in img_row:
    img[start, item] = [255,0,0]
  return start - 1
  

def main():
  y_max = 150
  data = numpy.zeros((y_max, len(row), 3), dtype=numpy.uint8)
  valid = gen.validRow(row)
  if (valid):
    passes = gen.processRow(row)
    offset = y_max - 1
    for p in passes:
      print(p)
      offset = imageAddRow(p, data, offset)

    image = Image.fromarray(data)
    image.show()
    
  else:
    exit(1)

if __name__ == "__main__":
  main()