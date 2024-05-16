import streamlit as st

st.title("Frequently Asked Questions about Air Pollution and Human Health")

faqs = [
    {
        "1️⃣" "question": "How can data visualization techniques help in understanding the impact of air pollution on human health?",
        "answer": "Data visualization can effectively illustrate trends and correlations between air pollutant levels and health outcomes over time and across different regions. It enables the identification of pollution hotspots and vulnerable populations, aiding policymakers in targeting interventions. Interactive visualizations allow stakeholders to explore complex datasets, fostering public awareness and engagement."
    },
    {
        "question": "What role does AI and machine learning play in analyzing air pollution data and its effects on human health?",
        "answer": "AI algorithms can process large volumes of heterogeneous data from various sources, including satellite imagery, sensor networks, and health records. Machine learning models can predict air quality levels and health risks, enabling early warning systems and adaptive interventions. AI-powered tools, such as image recognition and natural language processing, facilitate the automated analysis of pollution-related images and textual data."
    },
    {
        "question": "How can AI-driven predictive modeling assist in mitigating the health impacts of air pollution?",
        "answer": "Predictive models can forecast future air quality conditions and associated health risks, allowing preemptive measures to be taken. Machine learning algorithms can identify patterns in historical data to predict pollutant concentrations and their effects on vulnerable populations. Real-time monitoring coupled with AI enables dynamic adjustments in pollution control measures, optimizing resource allocation and response strategies."
    },
    {
        "question": "What are some examples of data-driven initiatives addressing air pollution and public health concerns?",
        "answer": "Collaborative platforms integrate environmental monitoring data, health statistics, and citizen science contributions to generate actionable insights. Data-driven public health campaigns leverage social media analytics and geospatial visualization to raise awareness and promote behavioral changes. AI-powered pollution monitoring devices and wearable sensors provide individuals with personalized exposure information, empowering them to make informed decisions."
    },
    {
        "question": "How can stakeholders utilize data visualization and AI techniques to advocate for policy changes addressing air pollution?",
        "answer": "Compelling visualizations illustrating the health impacts of air pollution can be used to lobby for stricter environmental regulations and emission standards. AI-driven policy simulations and scenario analyses help policymakers assess the potential outcomes of different intervention strategies and prioritize resource allocation. Collaborative platforms facilitate knowledge sharing and stakeholder engagement, fostering a data-driven approach to policy formulation and implementation."
    }
]

for faq in faqs:
    st.subheader(faq["question"])
    st.write(faq["answer"])
