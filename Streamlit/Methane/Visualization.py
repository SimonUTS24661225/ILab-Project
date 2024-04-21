import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('Streamlit/Methane/IHME-GBD_2019_DATA-571d49cc-1_combined.csv')

# Filter the data
df_number = df[df['metric_name'] == 'Number']
pivot_table = df_number.pivot_table(values='val', index='year', columns='cause_name', aggfunc='sum')

# Plot using Plotly
fig = go.Figure()
for col in pivot_table.columns:
    fig.add_trace(go.Scatter(x=pivot_table.index, y=pivot_table[col], mode='lines', name=col))

# Update layout
fig.update_layout(title='Death Rate by Cause Over Years',
                  xaxis_title='Year',
                  yaxis_title='Death Rate',
                  legend_title='Cause Name')

# Display the plot
st.plotly_chart(fig)
