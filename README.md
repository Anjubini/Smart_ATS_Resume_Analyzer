Smart ATS for Resumes 📄🔍
This Smart Application Tracking System (ATS) is designed to evaluate resumes against a given job description. It provides insights on match percentage, missing keywords, and profile summaries to assist in resume screening.

Features
✨ Streamlit Interface: User-friendly interface created using Streamlit for easy interaction.

🔍 GenerativeAI Integration: Utilizes Google's GenerativeAI API for analyzing resumes and providing feedback.

📄 PDF Resume Support: Supports uploading resumes in PDF format, processed using PyPDF2.

Setup
Install Dependencies: Ensure you have Python installed. Install required Python packages using pip:

Set up Google API Key: Obtain a Google API key and set it as an environment variable named GOOGLE_API_KEY. You can also directly set it in the script.

Run the Application: Start the Streamlit application by running:

Usage
Paste Job Description: Enter the job description in the provided text area.

Upload Resumes: Upload resumes in PDF format using the file uploader.

Submit: Click the submit button to evaluate the resumes against the job description.

Review Results: View the ranked resumes, match percentages, and descriptions in the table format.

