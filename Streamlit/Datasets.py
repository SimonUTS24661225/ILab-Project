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
