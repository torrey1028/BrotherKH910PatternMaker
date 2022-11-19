import pattern_generator as gen
import visualize_pattern as vis

# Geometric pattern
pattern = []

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
pattern.append(row0)
pattern.append(row0)
pattern.append(row0)
pattern.append(row0)

row1 = []
gen.insert(row1, gen.Knit, 1)
row1.append(gen.YarnOver())
row1.append(gen.KnitTogetherRight())
gen.insert(row1, gen.Knit, 12)
row1.append(gen.KnitTogetherLeft())
row1.append(gen.YarnOver())
gen.insert(row1, gen.Knit, 1)
pattern.append(row1)

row2 = []
gen.insert(row2, gen.Knit, 2)
row2.append(gen.YarnOver())
row2.append(gen.KnitTogetherRight())
gen.insert(row2, gen.Knit, 10)
row2.append(gen.KnitTogetherLeft())
row2.append(gen.YarnOver())
gen.insert(row2, gen.Knit, 2)
pattern.append(row2)

row3 = []
gen.insert(row3, gen.Knit, 3)
row3.append(gen.YarnOver())
row3.append(gen.KnitTogetherRight())
gen.insert(row3, gen.Knit, 8)
row3.append(gen.KnitTogetherLeft())
row3.append(gen.YarnOver())
gen.insert(row3, gen.Knit, 3)
pattern.append(row3)

row4 = []
gen.insert(row4, gen.Knit, 4)
row4.append(gen.YarnOver())
row4.append(gen.KnitTogetherRight())
gen.insert(row4, gen.Knit, 6)
row4.append(gen.KnitTogetherLeft())
row4.append(gen.YarnOver())
gen.insert(row4, gen.Knit, 4)
pattern.append(row4)

row5 = []
gen.insert(row5, gen.Knit, 5)
row5.append(gen.YarnOver())
row5.append(gen.KnitTogetherRight())
gen.insert(row5, gen.Knit, 4)
row5.append(gen.KnitTogetherLeft())
row5.append(gen.YarnOver())
gen.insert(row5, gen.Knit, 5)
pattern.append(row5)

row6 = []
gen.insert(row6, gen.Knit, 6)
row6.append(gen.YarnOver())
row6.append(gen.KnitTogetherRight())
gen.insert(row6, gen.Knit, 2)
row6.append(gen.KnitTogetherLeft())
row6.append(gen.YarnOver())
gen.insert(row6, gen.Knit, 6)
pattern.append(row6)

row7 = []
gen.insert(row7, gen.Knit, 7)
row7.append(gen.YarnOver())
row7.append(gen.KnitTogetherRight())
row7.append(gen.KnitTogetherLeft())
row7.append(gen.YarnOver())
gen.insert(row7, gen.Knit, 7)
pattern.append(row7)

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
pattern.append(row8)

vis.createPattern(pattern)