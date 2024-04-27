
import streamlit as st

def landfill_waste_info():
    st.write("### Landfill Waste Management")
    st.write("""
        Landfill waste refers to the disposal of garbage and debris in designated areas known as landfills. These sites are engineered to minimize environmental impact by isolating trash from surrounding environments, preventing contamination of water and air.

        #### Environmental Challenges:
        Despite engineering efforts, landfills can still pose significant environmental challenges, including:
        - **Methane Emissions:** Organic waste decomposes anaerobically in landfills, producing methane, a potent greenhouse gas.
        - **Leachate:** Toxic liquid known as leachate can seep from landfills, posing risks to groundwater and ecosystems.
        - **Land Degradation:** Landfills contribute to soil degradation and loss of biodiversity.

        #### Sustainable Waste Management:
        With rising waste production, sustainable waste management practices are crucial to reduce reliance on landfills. These practices include:
        - **Recycling:** Sorting and processing waste materials to create new products.
        - **Composting:** Decomposing organic waste into nutrient-rich soil amendments.

        By adopting sustainable waste management practices, we can mitigate the environmental impact of landfill waste and move towards a more sustainable future.
    """)

landfill_waste_info()

st.image("Streamlit/Methane/download (1).jpeg", caption="Image of Landfill-Waste")
st.image("Streamlit/Methane/14-Landfill-Methane-Emissions-by-World-Region-1970-2017.png", caption="1970-2017 Landfill Methane Emissions by World Region")
st.image("Streamlit/Methane/Greenhouse_gas_emissions_of_waste_management,_EU-28,_1990-2017(million_tonnes_of_CO2_equivalent).png", caption="1990-2017 Greenhouse_gas_emissions_of_waste_management")
