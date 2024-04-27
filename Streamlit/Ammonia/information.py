import streamlit as st

# Title
st.write("### Impact of Ammonia on Human Health")

# Introduction
st.write("""
Ammonia is a colorless gas with a pungent odor and is commonly used in agricultural and industrial processes. Although not considered toxic in low concentrations, exposure to high levels of ammonia can have adverse effects on human health through various mechanisms.
""")

# Major Sources of Ammonia Emissions
st.write("#### Major Sources of Ammonia Emissions")
st.write("""
- Agricultural activities, including livestock farming and fertilizer application
- Industrial processes, such as chemical manufacturing and wastewater treatment
- Household cleaning products and certain consumer goods
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
- Respiratory issues, such as coughing, wheezing, and shortness of breath
- Eye irritation and damage, including blurred vision and corneal burns
- Skin irritation and burns upon contact
- Gastrointestinal discomfort, such as nausea, vomiting, and abdominal pain
- Neurological symptoms, including headaches, dizziness, and confusion

Long-term exposure to ammonia may increase the risk of chronic respiratory conditions and exacerbate pre-existing respiratory diseases, such as asthma and chronic obstructive pulmonary disease (COPD). Additionally, ammonia emissions can contribute to air pollution and environmental degradation, affecting both human health and ecosystems.
""")

image_url = "https://www.openaccessgovernment.org/wp-content/uploads/2018/07/dreamstime_s_114372506.jpg"
st.image(image_url, caption="Image Caption")
st.image("Streamlit/Ammonia/Country-breakdown-of-global-ammonia-production-2021-Source-6.png", caption="2021 Country Breakdown of Global Ammonia Production")

