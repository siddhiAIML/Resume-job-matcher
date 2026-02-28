import streamlit as st
from clean_text import clean_text
from skill_extractor import extract_skills
from pdfminer.high_level import extract_text

# ----------------- Page Config -----------------
st.set_page_config(page_title="Resume & Job Skill Matcher", layout="wide")

# ----------------- Title -----------------
st.title("📄 Resume & Job Skill Matcher")
st.markdown(
    """
    Upload your **Resume (PDF)** and **Job Description (TXT)** to see:
    - Cleaned resume text  
    - Skills extracted from resume and job description  
    - Matching skills  
    - Overall skill match score
    """
)
st.markdown("---")

# ----------------- Upload Files -----------------
resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_file = st.file_uploader("Upload Job Description (.txt)", type=["txt"])

if resume_file and job_file:
    # ----------------- Extract and Clean Resume -----------------
    resume_text = extract_text(resume_file)
    cleaned_resume = clean_text(resume_text)
    resume_skills = extract_skills(cleaned_resume)

    # ----------------- Extract and Clean Job -----------------
    job_text = job_file.read().decode("utf-8")
    cleaned_job = clean_text(job_text)
    job_skills = extract_skills(cleaned_job)

    # ----------------- Skill Matching -----------------
    resume_set = set(resume_skills)
    job_set = set(job_skills)
    common_skills = resume_set.intersection(job_set)
    all_skills = resume_set.union(job_set)
    match_score = len(common_skills) / len(all_skills) * 100

    # ----------------- Display Cleaned Resume -----------------
    with st.container():
        st.subheader("📄 Cleaned Resume Text")
        st.text_area("Resume Content", cleaned_resume, height=200)

    st.markdown("---")

    # ----------------- Display Skills Side by Side -----------------
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📝 Resume Skills")
        if resume_skills:
            st.write(resume_skills)
        else:
            st.write("No skills detected.")
    with col2:
        st.subheader("💼 Job Description Skills")
        if job_skills:
            st.write(job_skills)
        else:
            st.write("No skills detected.")

    st.markdown("---")

    # ----------------- Display Matching Skills -----------------
    with st.container():
        st.subheader("✅ Matching Skills")
        if common_skills:
            for skill in common_skills:
                st.markdown(f"<span style='color:green'>✔ {skill}</span>", unsafe_allow_html=True)
        else:
            st.write("No matching skills found.")

    st.markdown("---")

    # ----------------- Display Match Score -----------------
    with st.container():
        st.subheader("📊 Overall Skill Match")
        st.metric(label="Match Score", value=f"{match_score:.2f}%")
        st.progress(int(match_score))