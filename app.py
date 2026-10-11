import os
import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai

# Load API key

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)



st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(
        135deg, #0b1020 0%, #15152e 55%, #21153d 100%
    );
    color: #f3f4f6;
}

/* Page spacing */
.block-container {
    max-width: 1000px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Main title */
h1 {
    color: #c4b5fd !important;
    font-size: 2.7rem !important;
    font-weight: 800 !important;
}

/* Section headings */
h2, h3 {
    color: #ddd6fe !important;
}

/* General text */
p, label, li {
    color: #e5e7eb;
}

/* Resume upload panel */
div[data-testid="stFileUploader"] {
    background: rgba(139, 92, 246, 0.10);
    border: 1px solid #6d5bd0;
    border-radius: 16px;
    padding: 18px;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #6366f1);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.4rem;
    font-weight: 700;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #8b5cf6, #818cf8);
    border: none;
    transform: translateY(-2px);
}

/* Extracted resume text */
div[data-testid="stTextArea"] textarea {
    background: #111827;
    color: #e5e7eb;
    border: 1px solid #49406b;
    border-radius: 10px;
}

/* Success and warning messages */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Subtle separators */
hr {
    border-color: #383052;
}
</style>
""", unsafe_allow_html=True)


# App Title & Description
st.title("CareerPilot AI")
st.write("AI-Powered Resume Analysis & Career Guidance")

st.header("Upload Your Resume")
resume = st.file_uploader("Upload your resume in PDF format", type=["pdf"])

if resume is not None:
    st.success("Resume uploaded successfully!")
    st.write("File name:", resume.name)

    # Extract text from PDF
    reader = PdfReader(resume)
    resume_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + "\n"

    # Display extracted text area
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=300)

    # Analyze Button - Always visible once a file is uploaded
    
    if st.button("Analyze Resume"):
        if not resume_text.strip():
            st.warning(
                "No text could be extracted from this PDF. "
                "Please try a text-based PDF."
            )
        else:
            prompt = f"""
Analyze the following resume and provide:

1. Resume Summary
2. Skills Identified
3. Suitable Career Roles
4. Missing or Recommended Skills
5. Resume Improvement Suggestions

Give clear, practical suggestions suitable for a student.
Use only information supported by the resume. Clearly label
recommendations as suggestions, not existing qualifications.

Resume:
{resume_text}
"""

            try:
                with st.spinner("Analyzing your resume..."):
                    interaction = client.interactions.create(
                        model="gemini-3.8-flash",
                        input=prompt,
                        generation_config={
                            "thinking_level": "low",
                            "max_output_tokens": 1500
                        }
                    )

                response_text = interaction.output_text

                st.subheader("CareerPilot AI Analysis")
                st.markdown(response_text)

            except Exception as e:
                error_message = str(e)

                if "429" in error_message or "quota" in error_message.lower():
                    st.warning(
                        "The AI service has reached its current usage limit. "
                        "Please try again after the quota resets."
                    )
                elif "503" in error_message or "unavailable" in error_message.lower():
                    st.warning(
                        "The AI service is temporarily busy. "
                        "Please try again shortly."
                    )
                else:
                    st.error(
                        "Analysis could not be completed. "
                        "Please check your API configuration and try again."
                    )
