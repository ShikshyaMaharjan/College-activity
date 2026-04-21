import pandas as pd
import numpy as np

data = {
    "ID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Marks": [80, 90, 70, 85, 60, 75, 88, 92, 55, 78],
    "Salary": [1000.5, 1200.0, 1100.5, 1300.0, 900.0, 1150.5, 1250.0, 1400.0, 950.0, 1050.0]
}

df = pd.DataFrame(data)

print(df)

#a
series_marks = df["Marks"]
print(series_marks)