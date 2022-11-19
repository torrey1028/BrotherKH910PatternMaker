import pattern_generator as gen
import visualize_pattern as vis

# leaf pattern
pattern = []

row0 = []
gen.insert(row0, gen.Knit, 1)
row0.append(gen.KnitTogetherLeft())
gen.insert(row0, gen.Knit, 4)
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 3)
row0.append(gen.YarnOver())
gen.insert(row0, gen.Knit, 2)
row0.append(gen.KnitTogetherRight())
pattern.append(row0)

row1 = []
row1.append(gen.KnitTogetherLeft())
gen.insert(row1, gen.Knit, 4)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 5)
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 1)
row1.append(gen.KnitTogetherRight())
pattern.append(row1)

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
pattern.append(row2)

row3 = []
row3.append(gen.KnitTogetherLeft())
gen.insert(row3, gen.Knit, 2)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 3)
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 4)
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 1)
pattern.append(row3)

row4 = []
row4.append(gen.KnitTogetherLeft())
gen.insert(row4, gen.Knit, 1)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 5)
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 4)
row4.append(gen.KnitTogetherRight())
pattern.append(row4)

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
pattern.append(row5)

vis.createPattern(pattern)