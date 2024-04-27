import streamlit as st

def animal_waste_management_info():
    st.write("### Animal Waste Management")
    st.write("""
        Animal waste management encompasses the procedures and activities needed to collect, store, handle, and use manure—whether liquid, slurry, or solid—from farm animals until it is disposed of. Proper waste management is crucial for supplying vital agricultural nutrients and preventing environmental pollution.

        #### Types of Animal Waste:
        Animal waste can be categorized into three main types: solid, slurry, and wastewater. Solid wastes can be composted or dried for disposal.

        #### Final Removal:
        The appropriate disposal of animal excrement is essential to minimize environmental impacts. Here are some suggestions for waste disposal:

        1. **Land Application:** Ideally, productive agricultural land should be located adjacent to animal activity areas to accept liquid and/or solid wastes. Manure should be promptly incorporated into the soil to reduce runoff and enhance crop nutrient uptake.

        2. **Regulatory Considerations:** Avoid spreading manure near drainage or water bodies, as regulations may restrict the distance based on soil type, climate, and slope.

        3. **Weather Conditions:** Avoid spreading manure on frozen or wet soil to prevent runoff.

        4. **Nutrient Management:** Calculate the amount of land needed to accept liquid manure waste based on the nutrient content. Apply only as much manure as the soil-crop system can handle to avoid overapplication.

        Proper animal waste management practices help minimize environmental pollution and maximize agricultural productivity, ensuring sustainable farming practices.
    """)

animal_waste_management_info()

st.image("Streamlit/Methane/Enteric_fermentation_process_in_cows.png", caption="Image of Fermentation Process in Cows")
st.image("Streamlit/Methane/image.png", caption="Piechart of Methane Emission from Livestock")
