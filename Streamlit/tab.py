import streamlit as st
import base64

def create_tabs(selected_tab):
    if selected_tab == "Dataset":
        st.markdown("### Download Dataset")
        # First file
        file_path_1 = "Streamlit/Methane.xlsx"
        with open(file_path_1, "rb") as f1:
            data1 = f1.read()
        st.markdown(
            """
            <style>
            .stButton1>button {
                background-color: #ffcc00 !important;
                color: #333 !important;
            }
            </style>
            """
            , unsafe_allow_html=True
        )
        if st.button("Download Methane Dataset", key="methane_button"):
            b64_data1 = base64.b64encode(data1).decode()
            href1 = f'<a href="data:application/octet-stream;base64,{b64_data1}" download="Methane.xlsx">Download Methane Dataset</a>'
            st.markdown(href1, unsafe_allow_html=True)
        
        # Second file
        file_path_2 = "Streamlit/Mortality rate.xlsx"
        with open(file_path_2, "rb") as f2:
            data2 = f2.read()
        st.markdown(
            """
            <style>
            .stButton2>button {
                background-color: #ffcc00 !important;
                color: #333 !important;
            }
            </style>
            """
            , unsafe_allow_html=True
        )
        if st.button("Download Mortality Rate Dataset", key="mortality_button"):
            b64_data2 = base64.b64encode(data2).decode()
            href2 = f'<a href="data:application/octet-stream;base64,{b64_data2}" download="Mortality rate.xlsx">Download Mortality Rate Dataset</a>'
            st.markdown(href2, unsafe_allow_html=True)
        
    elif selected_tab == "Information":
        st.write("#### Impact of Methane on Climate Change ")
        st.write("""
            Methane (CH4) is a key component of natural gas and a potent greenhouse gas (GHG). It traps heat in the atmosphere, acting like a blanket around the Earth. This natural process, known as the greenhouse effect, is essential for keeping our planet warm enough for life. However, human activities have led to an increase in greenhouse gas emissions, intensifying this effect and contributing to global warming.
        """)
        st.write("#### Causes of methane emission")
        st.write("""
            - Enteric fermentation
            - Agrifood systems waste disposal
            - On-farm energy use
            - Burning: Crop Residues
            - Food Processing and food packaging
            - Energy
            - Waste
            - Rice cultivation
            - Manure Management
            - IPPU (Industrial processes and product use)
            - Food household consumption
            - Forest fires and Savanna fires
            - Food transport and food Retail
            - Pesticides manufacturing
            - Fires in humid tropical forests
            - Fires in organic soils
        """)
        
        st.write("#### The Severity of Methane: Its Impact on Climate Change")
        st.write("""
            "Methane: A Potent Greenhouse Gas Amplifying Climate Change Methane, over 28 times more effective than carbon dioxide at trapping heat, has witnessed a staggering increase in atmospheric concentrations, doubling in the past two centuries primarily due to human activities."
        """)

        st.write("#### Countries of Highest Methane Emission")
        st.image("Streamlit/Emission vs Country.png", caption="Top 10 countries with the highest methane emissions from 1990 to 2021.")
        st.image("Streamlit/Causes of methane emission in China.png", caption="Top 5 contributors to methane emissions in China from 1990 to 2021", width=400)

    elif selected_tab == "References":
        st.write("#### References:")
        st.write("""
            1. Methane Gas : Emission Analysis. (n.d.). Kaggle.com. https://www.kaggle.com/code/zsinghrahulk/methane-gas-emission-analysis/input?select=FAOSTAT_data_en_11-14-2023.csv

‌
            2. Bridger photonics. (n.d.). How Does Methane Affect the Environment? | Bridger Photonics. Www.bridgerphotonics.com.  https://www.bridgerphotonics.com/blog/how-does-methane-affect-environment#:~:text=Methane%20also%20contributes%20to%20the
                 
        """)

