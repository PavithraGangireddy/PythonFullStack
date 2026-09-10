#series
import pandas as pd
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

#creating series with index
import pandas as pd
data = [90, 85, 95]
s = pd.Series(data, index=["Python", "Pandas", "SQL"])
print(s)


#dataframe
import pandas as pd
data = [90, 85, 95]
s = pd.Series(data, index=["Python", "Pandas", "SQL"])
print(s)

#acess column values
import pandas as pd
data = {
    "Name": ["Ravi", "Sita", "John"],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
print(df["Name"])

#acessing multiple values
import pandas as pd
data = {
    "Name": ["Rudra", "Ram", "vikram"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
print(df[["Name", "Marks"]])

#add new column
import pandas as pd
data = {
    "Name": ["Ramya", "Sam", "karthik"],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
df["Grade"] = ["B", "A", "B"]
print(df)

#remove column
import pandas as pd
data = {
    "Name": ["dhana", "kavya", "divya"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}
df = pd.DataFrame(data)
df = df.drop("Age", axis=1)
print(df)

#filter data
import pandas as pd
data = {
    "Name": ["lakshmi", "rani", "akash"],
    "Marks": [85, 90, 55]
}
df = pd.DataFrame(data)
result = df[df["Marks"] >= 80]
print(result)

#