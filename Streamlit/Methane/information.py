import streamlit as st
import base64

st.write("#### Impact of Methane on Human Health ")
st.write("""
    Methane is a colorless, odorless gas that is the primary component of natural gas. While it is not considered toxic, methane can affect human health indirectly and through various mechanisms.
""")

st.write("#### Major Sources of Methane Emissions")
st.write("""
    - Fossil fuel production (33%)
    - Livestock farming (27%)
    - Landfills and wastes (16%)
""")

st.write("#### How Methane (CH4) generates from livestock and impacted on health")
st.write("""
    Methane is produced during the digestion process in cattle and other livestock. As the animals break down and ferment their food, methane is released as a byproduct. This methane production is a significant contributor to overall methane emissions globally.
    In addition to livestock, methane is also generated through various industrial processes. Leaks, venting, and other activities in the oil and gas industry, as well as waste management and agriculture, can all lead to the release of methane into the atmosphere.
""")

st.write("#### Health Impact due to Methane emission")
st.write("""
    List of common diseases occur due to methane emission from all the sources
    - Cardiovascular, respiratory, and neurological problems
    - Mood changes
    - slurred speech
    - vision problem
    - memory loss
    - nausea, vomiting
    - facial flushing and headache.
""")

st.write("#### Countries of Highest Methane Emission")
st.image("Streamlit/Emission vs Country.png", caption="Top 10 countries with the highest methane emissions from 1990 to 2021.")
st.image("Streamlit/Causes of methane emission in China.png", caption="Top 5 contributors to methane emissions in China from 1990 to 2021")
