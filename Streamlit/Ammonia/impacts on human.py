import streamlit as st

def health_impacts_of_ammonia_toxicity():
    # Set page title
    st.write("### Health Impacts of Ammonia Toxicity")

    # Liver Disease
    st.write("#### Liver Disease:")
    st.write("""
    Ammonia metabolism primarily occurs in the liver. In individuals with liver disease, such as cirrhosis or hepatitis, the liver may be less efficient at processing and detoxifying ammonia. Elevated levels of ammonia in the blood can exacerbate liver damage and contribute to the progression of liver disease.
    """)
    image_url_liv = "https://www.metropolisindia.com/upgrade/blog/upload/23/12/Liver-Failure1703930383.webp"
    st.image(image_url_liv, caption="Image Caption")


    # Hepatic Encephalopathy
    st.write("#### Hepatic Encephalopathy:")
    st.write("""
    Hepatic encephalopathy is a condition characterized by cognitive dysfunction and neurological symptoms resulting from liver dysfunction and the accumulation of toxic substances, including ammonia, in the bloodstream. High levels of ammonia can impair brain function and contribute to symptoms such as confusion, disorientation, impaired concentration, and personality changes.
    """)
    image_url_hep = "https://www.alcimed.com/wp-content/uploads/2021/09/encephalopathie-hepatique-1.jpg"
    st.image(image_url_hep, caption="Image Caption")

    # Reye's Syndrome
    st.write("#### Reye's Syndrome:")
    st.write("""
    Reye's syndrome is a rare but serious condition that primarily affects children and teenagers recovering from viral infections, such as influenza or chickenpox. While the exact cause of Reye's syndrome is not fully understood, it has been linked to the use of aspirin during viral illnesses. Ammonia toxicity has been proposed as one of the contributing factors in the development of Reye's syndrome, although the exact mechanism remains unclear.
    """)
    image_url_rey = "https://scontent.fsyd3-1.fna.fbcdn.net/v/t39.30808-6/300004745_1123123021932847_3742562859581901997_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=XKCWg1tdJAQAb6neU3J&_nc_ht=scontent.fsyd3-1.fna&oh=00_AfDT6zlp9VZLB8SJbHNL-_Z3An-TRlyINTnNZf2o_QqVPQ&oe=6634D50B"
    st.image(image_url_rey, caption="Image Caption")

    

    # Decreased Blood Flow to Liver
    st.write("#### Decreased Blood Flow to Liver:")
    st.write("""
    Ammonia can contribute to the constriction of blood vessels (vasoconstriction), including those supplying blood to the liver. Decreased blood flow to the liver can impair its ability to function properly and exacerbate liver damage in individuals with liver disease.
    """)

    # Confusion and Disorientation
    st.write("#### Confusion and Disorientation:")
    st.write("""
    Elevated levels of ammonia in the blood can impair brain function, leading to symptoms such as confusion, disorientation, and impaired cognitive function. These symptoms are characteristic of hepatic encephalopathy, a condition associated with liver dysfunction and ammonia toxicity.
    """)

    # Coma and Mood Swings
    st.write("#### Coma and Mood Swings:")
    st.write("""
    In severe cases of hepatic encephalopathy, where ammonia levels in the blood are significantly elevated, individuals may experience coma or loss of consciousness. Mood swings, personality changes, irritability, and agitation are also common manifestations of hepatic encephalopathy.
    """)

health_impacts_of_ammonia_toxicity()



