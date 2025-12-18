import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from google import genai
import PyPDF2 as pdf
import json

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])


def get_gemini_repsonse(prompt):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text




def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in reader.pages:
        text += page.extract_text()
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response as per below structure
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
"""

## streamlit app

with st.sidebar:
    st.title("Smart ATS for Resumes")
    st.subheader("About")
    st.write("This sophisticated ATS project, developed with Gemini Pro and Streamlit, seamlessly incorporates advanced features including resume match percentage, keyword analysis to identify missing criteria, and the generation of comprehensive profile summaries, enhancing the efficiency and precision of the candidate evaluation process for discerning talent acquisition professionals.")
    
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
    - [makersuit API Key](https://makersuite.google.com/)
    - [Github](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro) Repository
                
    """)
    
    add_vertical_space(5)
    st.write("by Bindiya K R.")
    
    


st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        final_prompt = input_prompt.format(text=text, jd=jd)
        response = get_gemini_repsonse(final_prompt)
        st.subheader(response)
