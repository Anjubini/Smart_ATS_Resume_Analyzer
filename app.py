import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import PyPDF2 as pdf
import json

# =============================
# MOCK MODE (NO API REQUIRED)
# =============================
USE_MOCK = True   # 🔥 Keep this TRUE (no payment)

def get_gemini_response(prompt):
    if USE_MOCK:
        return """
        {
          "JD Match": "82%",
          "MissingKeywords": ["Docker", "AWS", "CI/CD"],
          "Profile Summary": "Strong Python and AI background with good problem-solving skills. Resume aligns well with core requirements but needs improvement in cloud and DevOps tools."
        }
        """
    else:
        # Future real API integration
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

# =============================
# PDF Text Extraction
# =============================
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text
# ================= AGENTIC AI ADD-ON (NO CORE CHANGE) =================

def resume_improvement_agent():
    return [
        "Add cloud technologies such as AWS or GCP",
        "Quantify project achievements using metrics",
        "Improve action verbs in experience section",
        "Include CI/CD or DevOps exposure",
        "Tailor resume summary based on job description"
    ]

def explainable_score():
    return {
        "Skills Match": "60%",
        "Experience Match": "15%",
        "Education Match": "7%",
        "Projects Match": "10%"
    }


# =============================
# Prompt Template
# =============================
input_prompt = """
Act as an advanced ATS (Application Tracking System).
Evaluate the resume against the job description and return ATS score.

Resume:
{text}

Job Description:
{jd}

Return response in JSON format:
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

# =============================
# Sidebar
# =============================
with st.sidebar:
    st.title("Smart ATS for Resumes")
    st.subheader("About")
    st.write(
        "This sophisticated ATS project, developed with Gemini Pro and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision " \
        "of the candidate evaluation process for discerning talent acquisition professionals.")
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
    - [makersuit API Key](https://makersuite.google.com/)
    - [Github](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro) Repository
                
    """)

    
    add_vertical_space(5)
    st.write("Developed by Bindiya K R")

# =============================
# Main UI
# =============================
st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS Score")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type="pdf"
)

if st.button("Submit", key="submit_btn"):
    if uploaded_file and jd:
        resume_text = input_pdf_text(uploaded_file)
        final_prompt = input_prompt.format(text=resume_text, jd=jd)

        # ATS Analysis
        ats_result = get_gemini_response(final_prompt)

        st.subheader("ATS Analysis Result")
        st.write(ats_result)

        st.subheader("Explainable AI – Score Breakdown")

        st.progress(0.60)
        st.write("Skills Match – 60%")

        st.progress(0.15)
        st.write("Experience Match – 15%")

        st.progress(0.07)
        st.write("Education Match – 7%")

        st.progress(0.10)
        st.write("Projects Match – 10%")


        # Explainable AI
        st.subheader("Explainable AI – Score Breakdown")
        st.json(explainable_score())

        # Resume Improvement Agent
        st.subheader("Resume Improvement Suggestions (Agentic AI)")
        for tip in resume_improvement_agent():
            st.write("•", tip)
        #else:
            #st.warning("Please upload resume and paste job description.")
def extract_keywords(text):
    keywords = ["Python", "AI", "Machine Learning", "AWS", "Docker", "SQL"]
    return [k for k in keywords if k.lower() in text.lower()]

def resume_strength(score):
    score = int(score.replace('%',''))
    if score >= 80:
        return "🔥 Strong Resume"
    elif score >= 60:
        return "⚡ Moderate Resume"
    else:
        return "⚠ Needs Improvement"


