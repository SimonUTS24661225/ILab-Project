import streamlit as st


st.title("References")

references = {
    "Methane Gas: Emission Analysis": "https://www.kaggle.com/code/zsinghrahulk/methane-gas-emission-analysis/input?select=FAOSTAT_data_en_11-14-2023.csv",
    "Air Pollution - Our World in Data": "https://ourworldindata.org/air-pollution",
    "Global Health Data Exchange (GHDx)": "https://vizhub.healthdata.org/gbdresults/",
    "Main sources of methane emissions": "https://whatsyourimpact.org/greenhouse-gases/methane-emissions",
    "Reducing the Carbon Footprint of Cattle Operations through Diet": "https://water.unl.edu/article/manure-nutrient-management/reducing-carbon-footprint-cattle-operations-through-diet",
    "Importance of Methane - US EPA": "https://www.epa.gov/gmi/importancemethane#:~:text=Methane%20is%20the%20second%20most",
    "Methane’s links to respiratory diseases strengthens the case for its rapid reduction": "https://www.ccacoalition.org/news/methanes-links-respiratory-diseases-strengthens-case-its-rapid-reduction",
    "Diseases dataset caused by the Pollutants": "https://vizhub.healthdata.org/gbdresults/?params=gbd-api-2019-public/571d49cc2be3c07e33b856d5997bc32a",
    "Impact of Air Pollution on Human Health": "https://www.kaggle.com/code/abmsayem/impact-of-air-pollution-on-human-health/input?select=absolute-number-of-deaths-from-ambient-particulate-air-pollution.csv",
    "Indoor and Outdoor Air pollution datasets": "https://ourworldindata.org/air-pollution"
}

for title, link in references.items():
    st.markdown(f"{title}. [{link}]({link})")
