import streamlit as st

def health_impacts_of_methane_emissions():
    # Set page title
    st.write("### Health Impacts of Methane Emissions")

    # Respiratory Diseases
    st.write("#### Respiratory Diseases:")
    st.write("""
    Indirectly, methane emissions contribute to air pollution, which can exacerbate respiratory conditions such as asthma, chronic obstructive pulmonary disease (COPD), and bronchitis.
    """)
    image_url_res = "https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20220628103427/ri/750/src/images/Article_Images/ImageForArticle_22740_16564268624824428.jpg"
    st.image(image_url_res, caption="Image Caption")

    

    # Cardiovascular Diseases
    st.write("#### Cardiovascular Diseases:")
    st.write("""
    Poor air quality resulting from methane emissions can increase the risk of cardiovascular diseases such as heart attacks and strokes.
    """)

    image_url_car = "https://www.endocrine.org/-/media/endocrine/images/patient-engagement-webpage/condition-page-images/cardiovascular-disease/cardio_disease_t2d_pe_1796x943.jpg?w=1290&hash=F78C844A6E1954DE6180CD04CEB9318D"
    st.image(image_url_car, caption="Image Caption")

    # Heat-Related Illnesses
    st.write("#### Heat-Related Illnesses:")
    st.write("""
    Methane emissions contribute to climate change, which leads to more frequent and intense heatwaves. Heatwaves can cause heat exhaustion, heatstroke, and other heat-related illnesses.
    """)

    # Vector-Borne Diseases
    st.write("#### Vector-Borne Diseases:")
    st.write("""
    Climate change, influenced by methane emissions, can alter the distribution and behavior of disease-carrying vectors such as mosquitoes and ticks, leading to increased transmission of diseases like malaria, dengue fever, and Lyme disease.
    """)

    # Food and Waterborne Illnesses
    st.write("#### Food and Waterborne Illnesses:")
    st.write("""
    Climate change impacts, influenced by methane emissions, can affect food and water security, leading to food shortages, malnutrition, and increased susceptibility to food and waterborne illnesses such as diarrhea and cholera.
    """)

    # Mental Health Issues
    st.write("#### Mental Health Issues:")
    st.write("""
    Climate change-related events, such as extreme weather events and environmental degradation, can lead to mental health issues such as anxiety, depression, post-traumatic stress disorder (PTSD), and other psychological disorders.
    """)

health_impacts_of_methane_emissions()
