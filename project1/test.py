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

#step3:Access specific columns
print("\nAccess the 'Name' column:")
print(df.('Name'))

#step4: Access specific rows using iloc
print("\nAccess the second row using iloc:")
print(df.iloc[1])

#step5:Add a new column
df('Salary') = (70000,80000,90000)
print("\nDataFrame after adding a new  column 'Salary':")
print(df)

#step6: Filter rows based on a condition
filtered_df = df(df('Age') > 28)
print("\nFiltered DateFrame where Age > 28:")
print(filtered_df)

#step7: Calulate the average salary
average_salary = df ('Salary').mean()
print(f"\nAverage Salary: {average_salary}")