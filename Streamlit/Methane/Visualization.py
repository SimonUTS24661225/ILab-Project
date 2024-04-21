import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data from the Excel file
df = pd.read_csv('Streamlit/Methane/IHME-GBD_2019_DATA-571d49cc-1_combined.csv')

# Ensure that only rows with 'Number' in the 'metric_name' column are considered
df_number = df[df['metric_name'] == 'Number']

# Pivot the data to get 'cause_name' as columns, 'year' as rows, and 'val' as values
pivot_table = df_number.pivot_table(values='val', index='year', columns='cause_name', aggfunc='sum')

# Plotting the pivot table; each cause will automatically get a different line color
plt.figure(figsize=(12, 6))
pivot_table.plot(kind='line', marker='o')

# Adding title and labels
plt.title('Death Rate by Cause Over Years')
plt.xlabel('Year')
plt.ylabel('Death Rate ')

# If you have a large number of causes and the legend is overwhelming, you can move it outside the plot
plt.legend(title='Cause Name', bbox_to_anchor=(1.04,0.5), loc="center left")

# Showing a grid for better readability
plt.grid(True)

# Display the plot in Streamlit
st.pyplot()
