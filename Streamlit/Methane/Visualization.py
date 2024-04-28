import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Title
st.write("### Mortality Rate Caused by Three Main Diseases of Methane Emission")

# Load the data from the CSV file
df = pd.read_csv('Streamlit/Methane/IHME-GBD_2019_DATA-571d49cc-1_combined.csv')

# Ensure that only rows with 'Number' in the 'metric_name' column are considered
df_number = df[df['metric_name'] == 'Number']

# Pivot the data to get 'cause_name' as columns, 'year' as rows, and 'val' as values
pivot_table = df_number.pivot_table(values='val', index='year', columns='cause_name', aggfunc='sum')

# Plotting the pivot table; each cause will automatically get a different line color
fig, ax = plt.subplots(figsize=(12, 6))
pivot_table.plot(kind='line', marker='o', ax=ax)

# Adding title and labels
ax.set_title('Death Rate by Cause Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Death Rate')

# If you have a large number of causes and the legend is overwhelming, you can move it outside the plot
ax.legend(title='Cause Name', bbox_to_anchor=(1.04, 0.5), loc="center left")

# Showing a grid for better readability
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)


st.write("""
The chart presents the trend of death rates from 1990 to just before 2019 due to air pollution, focusing on three specific causes of death: cardiovascular diseases, chronic respiratory diseases, and neurological disorders.

From the visualization, it is apparent that the death rate from cardiovascular diseases has shown a significant upward trend, indicating an increasing number of deaths over the years. This contrasts with chronic respiratory diseases and neurological disorders, both of which have remained relatively stable throughout the same period.

The data suggests that while there have been substantial gains in managing chronic respiratory and neurological health issues, or at least keeping their death rates constant, cardiovascular diseases continue to be a growing challenge.

The visualization highlights the need for an increased focus on cardiovascular health in future healthcare strategies and policies.
""")


st.write("### Methane Emission Dashboard")

looker_url = "https://lookerstudio.google.com/embed/u/0/reporting/5a025395-e733-4370-8a0a-925c58a51539/page/JbRxD"
st.components.v1.iframe(looker_url, height=600)
