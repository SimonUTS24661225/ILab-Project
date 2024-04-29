import streamlit as st

# Title
st.write("### Impact of Ammonia on Human Health")

# Introduction
st.write("""
Ammonia is a colorless gas with a pungent odor and is commonly used in agricultural and industrial processes. Although not considered toxic in low concentrations, exposure to high levels of ammonia can have adverse effects on human health through various mechanisms.
""")

image_url = "https://www.openaccessgovernment.org/wp-content/uploads/2018/07/dreamstime_s_114372506.jpg"

# Major Sources of Ammonia Emissions
st.write("#### Major Sources of Ammonia Emissions")
st.write("""
- Agricultural activities, including livestock farming and fertilizer application (70%)
st.image(image_url, caption="Image Caption")
- Natural Processing in Ocean (15%)
- Wildfires (10%)
- Industrial processes, such as chemical manufacturing and wastewater treatment (1-2%)
""")

# How Ammonia Generates and Impacts Health
st.write("#### How Ammonia (NH3) Generates and Impacts Health")
st.write("""
Ammonia is released into the atmosphere from agricultural activities, particularly during the decomposition of animal waste and the application of nitrogen-based fertilizers. Industrial processes also contribute to ammonia emissions through emissions from chemical plants and other facilities.
""")

# Health Impact due to Ammonia Emission
st.write("#### Health Impact due to Ammonia Emission")
st.write("""
Exposure to high levels of ammonia can lead to various health problems, including:
- Liver disease
- Hepatic Encephalopathy
- Reye's syndrome
- Decreased blood flow to liver
- Coma, mood swings and excessive sleepiness
- Kidney failure


Long-term exposure to ammonia may increase the risk of chronic respiratory conditions and exacerbate pre-existing respiratory diseases, such as asthma and chronic obstructive pulmonary disease (COPD). Additionally, ammonia emissions can contribute to air pollution and environmental degradation, affecting both human health and ecosystems.
""")



st.write("#### Countries of Highest Ammonia Emission")
st.image("Streamlit/Ammonia/Country-breakdown-of-global-ammonia-production-2021-Source-6.png", caption="2021 Country Breakdown of Global Ammonia Production")

