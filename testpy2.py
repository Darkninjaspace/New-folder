import pandas as pd

# Create a DataFrame with columns 'Name' and 'Age'
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
print(df.loc[0, 'Name'])  # Accessing the first row and 'Name' column
print(df.iloc[0, 1])  # Accessing the first row and second column (Age) 