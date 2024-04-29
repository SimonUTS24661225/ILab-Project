import streamlit as st


def agricultural_ammonia_emissions():
    # Set page title
    st.write("### Agricultural Activities")

    # Introduction
    st.write("""
    Agricultural activities are significant contributors to ammonia emissions, which arise primarily from livestock farming and fertilizer application. Ammonia (NH3) is a colorless gas with a pungent odor that is produced during the decomposition of organic matter containing nitrogen. In agriculture, ammonia emissions occur mainly from livestock waste, fertilizer application, and soil management practices.
    """)

    # Sources of Ammonia Emissions
    st.write("### Sources of Ammonia Emissions")
    st.write("#### Livestock Farming:")
    st.write("""
    Ruminant animals, such as cattle, sheep, and goats, produce ammonia as a byproduct of digestion through enteric fermentation. Animal waste and urine also contribute to ammonia emissions.
    """)
    st.write(" #### Fertilizer Application:")
    st.write("""
    Nitrogen-based fertilizers, including ammonium nitrate, urea, and ammonium sulfate, are commonly used in agriculture to supply essential nutrients to crops. When these fertilizers are applied to soil, ammonia can volatilize into the atmosphere.
    """)
    st.write("#### Manure Management:")
    st.write("""
    Improper handling and storage of animal manure can lead to ammonia emissions as the manure decomposes. Anaerobic conditions in manure storage facilities can promote the production of ammonia.
    """)

    

    # Types of Ammonia Emissions
    st.write("### Types of Ammonia Emissions")
    st.write("#### Direct Emissions:")
    st.write("""
    Direct ammonia emissions occur when ammonia is released directly into the atmosphere from sources such as livestock waste, fertilizer application, and manure management practices.
    """)
    st.write("#### Indirect Emissions:")
    st.write("""
    Indirect ammonia emissions occur when ammonia reacts with other compounds in the environment to form secondary pollutants, such as fine particulate matter (PM2.5) and ammonium aerosols. These secondary pollutants can contribute to air pollution and have adverse effects on human health and the environment.
    """)
    
    image_url = "https://www.openaccessgovernment.org/wp-content/uploads/2018/07/dreamstime_s_114372506.jpg"
    st.image(image_url, caption="Image Caption")
    
    # Preventive Measures
    st.write("### Preventive Measures to Reduce Ammonia Emissions")
    st.write("#### Improved Manure Management:")
    st.write("""
    Implementing proper manure management practices, such as composting, anaerobic digestion, and manure injection, can reduce ammonia emissions from livestock waste.
    """)
    st.write("#### Optimized Fertilizer Application:")
    st.write("""
    Use precision agriculture techniques to apply fertilizers more efficiently, reducing the amount of ammonia volatilization from the soil.
    """)
    st.write("#### Nutrient Management Planning:")
    st.write("""
    Develop nutrient management plans to optimize fertilizer use, minimize nutrient runoff, and protect water quality.
    """)
    st.write("#### Alternative Farming Methods:")
    st.write("""
    Consider adopting alternative farming methods, such as organic farming, agroforestry, and cover cropping, which can help reduce reliance on synthetic fertilizers and minimize ammonia emissions.
    """)
    st.write("#### Technological Solutions:")
    st.write("""
    Explore technological solutions, such as ammonia scrubbers, biofilters, and anaerobic digesters, to capture and mitigate ammonia emissions from agricultural sources.
    """)

agricultural_ammonia_emissions()
