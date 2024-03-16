# Import pandas library
import pandas as pd
#import plotly.express as px

# Load the dataset
df = pd.read_csv('/Users/aivee/Desktop/Capstone_Infant_Mortality/Infant-Mortality-Rate-Project-Analysis/IMR_One_output_file.csv')
df2 = pd.read_csv('/Users/aivee/Desktop/Capstone_Infant_Mortality/Infant-Mortality-Rate-Project-Analysis/IMR_Two_output_file.csv')


# Concatenate the dataframes
combined_df = pd.concat([df, df2], ignore_index=True)
#combined_df = pd.concat([df, df2])
# (Optional) Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined.csv', index=False)
combined = pd.read_csv('combined.csv')
combined_df.head()


print(' ')
# Display first few rows of the combined_df
print('The first five lines of the combined_df is:')
print(' ')
combined_df.head(5)

print('')
#check for column names:
# df.columns
combined_df.columns
print('')

print(' ')
# Display the first few rows of the DataFrame
print(combined_df.head())
print(' ')


# Display the last few rows of the DataFrame
print(combined_df.tail())

# Get a concise summary of the DataFrame
print(combined_df.info())

# Get the number of rows and columns
print(combined_df.shape)

#Check for null values
print (combined_df.isnull().sum)

#Get a description of the data
print(combined_df.describe())

#Check for duplicates
print(combined_df.duplicated().sum)

#print(combined_df.columns)
#column_names = df.columns.tolist()
#print(output_file.csv)

# First, ensure the column exists to avoid KeyError:
#if 'Under-five mortality rate 2021' in combined_df.columns:
   # max_value = combined_df['Under-five mortality rate 2021'].max()
   # print(f"The maximum value in 'Under-five mortality rate 2021' is {max_value}")
#else:
  #  print("Column 'Under-five mortality rate 2021' does not exist in the DataFrame.")

#Check the maximum value for 2021
#df['column_name'].max()
max_value = combined_df['Under-five mortality rate 2021'].max()
print(('The Max value for the combined_df is:'), max_value)

# Delete a single column from the DataFrame
#df = df.drop(labels="", axis=1)

#df = df.dropna(axis=1, how='all')

#df = df.drop(df.index[[0]])

# Replace 'output_file.csv' with your desired file name
#df.to_csv('output_file.csv', index=False)

