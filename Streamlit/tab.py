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
        st.write("#### Impact of Methane on Human Health ")
        st.write("""
             Methane is a colorless, odorless gas that is the primary component of natural gas. While it is not considered toxic, methane can affect human health indirectly and through various mechanisms.
        """)
        st.write("#### Major Sources of Methane Emissions")
        st.write("""
            - Fossil fuel production
            - Livestock farming
            - Landfills and wastes
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
        

    elif selected_tab == "References":
        st.write("#### References:")
        st.write("""
            1. [Methane Gas: Emission Analysis](https://www.kaggle.com/code/zsinghrahulk/methane-gas-emission-analysis/input?select=FAOSTAT_data_en_11-14-2023.csv)
            2. [How Does Methane Affect the Environment?](https://www.bridgerphotonics.com/blog/how-does-methane-affect-environment#:~:text=Methane%20also%20contributes%20to%20the)
        """)
        
        


