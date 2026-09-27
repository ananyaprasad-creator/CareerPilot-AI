import streamlit as st
from pypdf import PdfReader

st.title("CareerPilot AI")

st.write("AI-Powered Resume Analysis & Career Guidance")

st.header("Upload Your Resume")

resume = st.file_uploader(
    "Upload your resume in PDF format",
    type=["pdf"]
)

if resume is not None:
    st.success("Resume uploaded successfully!")
    st.write("File name:", resume.name)

    # Read the PDF
    reader = PdfReader(resume)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + "\n"

    st.subheader("Extracted Resume Text")

    if resume_text.strip():
        st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )
    else:
        st.warning("No text could be extracted from this PDF.")