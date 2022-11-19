import pattern_generator as gen
import visualize_pattern as vis

pattern = []
row1 = []
row1.append(gen.Knit())
row1.append(gen.Knit())
row1.append(gen.KnitTogetherRight())
row1.append(gen.YarnOver())
row1.append(gen.Knit())
row1.append(gen.Knit())
pattern.append(row1)

row2 = []
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
pattern.append(row2)

row3 = []
row3.append(gen.Knit())
row3.append(gen.Knit())
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherLeft())
row3.append(gen.Knit())
row3.append(gen.Knit())
pattern.append(row3)

row4 = []
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
row4.append(gen.Knit())
pattern.append(row4)

vis.createPattern(pattern)