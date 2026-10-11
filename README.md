# CareerPilot-AI
AI-powered resume analysis and career guidance using Streamlit


CareerPilot AI is a beginner-friendly AI application that analyzes resumes and provides personalized career guidance. Users can upload their resumes in PDF format and receive suggestions to improve their resumes and identify suitable career paths.

## Features

- **PDF Resume Upload:** Upload a resume in PDF format.
- **Text Extraction:** Extracts readable text from the uploaded resume.
- **AI Resume Analysis:** Uses Google's Gemini AI to analyze resume content.
- **Skills Identification:** Identifies skills mentioned in the resume.
- **Career Recommendations:** Suggests suitable career roles based on the resume.
- **Skill Improvement:** Recommends additional skills to develop.
- **Resume Improvement Tips:** Provides practical suggestions for improving resume quality.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF
- Python-dotenv

## How to Run the Project

1. Clone this repository:
   `git clone https://github.com/ananyaprasad-creator/CareerPilot-AI.git`

2. Open the project folder and install the required packages:
   `pip install streamlit pypdf python-dotenv google-genai`

3. Create a `.env` file in the project folder and add your Gemini API key:
   `GEMINI_API_KEY=your_api_key_here`

4. Run the application:
   `python -m streamlit run app.py`

## Security

Keep your API key private. Never upload your `.env` file or expose your API key publicly.

## Project Goal

The goal of CareerPilot AI is to help students understand their existing skills, explore suitable career opportunities, and identify areas for professional development.
