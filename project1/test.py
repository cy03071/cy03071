import pandas as pd

#step1:Create a DataFrame
data = (
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['Neew York','Los Angeles','Chaicago']
)

df = pd.DataFrame(data)

#Step 2: Display the DataFrame
print("Original DataFrame:")
print(df)

