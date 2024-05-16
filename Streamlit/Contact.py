import streamlit as st



st.title("Student Details")

students = [
    {"name": "Asmita Sheshrao Kamble", "degree": "B.E. E&TC, MS Data Science & Innovation", "experience": "Process analyst (3yrs)", "email": "Asmita.S.Kamble@student.uts.edu.au"},
    {"name": "Simon Lim", "degree": "B.E. Psychology, MS Data Science & Innovation", "experience": "System Analyst (6 months)", "email": "Seeyon.lim@student.uts.edu.au"},
    {"name": "Tarun Gupta", "degree": "MS in Data Science", "experience": "7 years in software development", "email": "Tarun.gupta-1@student.uts.edu.au"},
    {"name": "Somayeh Amraee", "degree": "MS in Data Science", "experience": "", "email": "Somayeh.amraee@student.uts.edu.au"},
    {"name": "Hareesh Balasundaram", "degree": "MS in Data Science", "experience": "", "email": "Hareesh.balasundaram@student.uts.edu.au"}
]

for student in students:
    st.markdown(f"**Name:** {student['name']}")
    st.markdown(f"**Degree:** {student['degree']}")
    st.markdown(f"**Experience:** {student['experience']}")
    st.markdown(f"**Email:** {student['email']}")
    st.markdown("---")
