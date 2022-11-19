import pattern_generator as gen
import visualize_pattern as vis

pattern = []

row0 = []
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
row0.append(gen.KnitTogetherLeft())
row0.append(gen.YarnOver())
row0.append(gen.Knit())
row0.append(gen.Knit())
pattern.append(row0)

row1 = []
row1.append(gen.KnitTogetherLeft())
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherLeft())
row1.append(gen.Knit())
row1.append(gen.YarnOver())
row1.append(gen.Knit())
pattern.append(row1)

row2 = []
row2.append(gen.KnitTogetherLeft())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.Knit())
row2.append(gen.YarnOver())
pattern.append(row2)

row3 = []
row3.append(gen.KnitTogetherLeft())
row3.append(gen.Knit())
row3.append(gen.Knit())
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherLeft())
row3.append(gen.YarnOver())
pattern.append(row3)

row4 = []
row4.append(gen.KnitTogetherLeft())
row4.append(gen.Knit())
row4.append(gen.YarnOver())
row4.append(gen.Knit())
row4.append(gen.KnitTogetherLeft())
row4.append(gen.YarnOver())
pattern.append(row4)

row5 = []
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
row5.append(gen.Knit())
row5.append(gen.Knit())
row5.append(gen.Knit())
row5.append(gen.Knit())
pattern.append(row5)

vis.createPattern(pattern)