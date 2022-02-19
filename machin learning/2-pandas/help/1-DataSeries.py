example = {'row1' : 1,
           'row2' : 2,
           'row3' : 3,
           'row4' : 4,
           'row5' : 5,
           'row6' : 6,
           'row7' : 7,
           'row8' : 8,
           'row9' : 9,
           'row10': 10,}

import numpy as np
import pandas as pd

mySeries = pd.Series([1,2,3,4,5,6,7,8,9,10],index=['row1','row2','row3','row4','row5','row6','row7','row8','row9','row10'])

print(mySeries)

print()

print(mySeries.values)

print()

print(mySeries.index)

print()

print(mySeries.row2) # or mySeries['row2']
print(mySeries['row2'])
print()

print(mySeries[mySeries>7])

print()

mySeries = mySeries.rename({'row1':'r1','row2' : 'r2','row3':'r3','row4' : 'r4','row5':'r5','row6' : 'r6','row7':'r7','row8' : 'r8','row9':'r9','row10' : 'r10'})



print(mySeries.index)
