import streamlit as st

def show_causes_of_methane():
    st.write("### Major Sources of Methane Emissions")
    st.write("""
        Methane emissions arise from various human activities and natural processes. Some of the major sources include:
        - **Fossil Fuel Production (20-35%):** Extraction, processing, and transportation of fossil fuels such as coal, oil, and natural gas release methane.
        - **Livestock Farming (20-25%):** Ruminant animals like cattle, sheep, and goats produce methane during digestion, primarily through enteric fermentation.
        - **Landfills and Wastes (10-20%):** Organic waste decomposes anaerobically in landfills, producing methane as a byproduct. This includes municipal solid waste, agricultural residues, and sewage.
        - **Wetlands (15-20%):** Natural wetlands are significant sources of methane due to the anaerobic decomposition of organic matter in waterlogged soils.
        - **Rice Cultivation (5-10%):** Flooded rice paddies create anaerobic conditions conducive to methane production by methanogenic archaea in the soil.
        - **Energy Production (5-10%):** Methane emissions occur during the extraction, processing, and distribution of natural gas, as well as in coal mining and oil drilling operations.
        - **Biomass Burning (3-7%):** Combustion of biomass, such as forests and agricultural residues, releases methane and other greenhouse gases into the atmosphere.
        - **Wastewater Treatment (1-5%):** Anaerobic decomposition of organic matter in sewage treatment facilities generates methane.
        - **Industrial Processes (1-5%):** Various industrial activities, including chemical manufacturing, oil refining, and wastewater treatment, contribute to methane emissions through leaks, fugitive emissions, and chemical reactions.
    """)

show_causes_of_methane()
