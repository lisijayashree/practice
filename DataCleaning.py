import pandas as pd
import numpy as np
import csv

#uploading the data
df=pd.read_csv("Assignment -13 dataset - Sheet1.csv")
#printing first 5 rows of the data
df.head(5)

#to drop any uncessary colum
df.drop("column", inplace= True, axis=1)
df.head(5)

#to rename a column name
df.rename(column="new_name",inplace= True)

#to replace values of a column
replace_value={"Pass":1,"Fail":0}
df=df.replace({"column": replace_value})

