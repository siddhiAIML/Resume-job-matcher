from pdfminer.high_level import extract_text
import os
from clean_text import clean_text
from skill_extractor import extract_skills

resume_folder = "data/raw/resumes"

files = os.listdir(resume_folder)
print("Files inside resumes folder:", files)

if len(files) == 0:
    print("No resume files found!")
else:
    resume_path = os.path.join(resume_folder, files[0])
    
    # Extract raw text
    raw_text = extract_text(resume_path)
    
    # Clean text
    cleaned_text = clean_text(raw_text)

    print("\n----- CLEANED RESUME TEXT -----\n")
    print(cleaned_text)
    
    # Extract skills
    skills = extract_skills(cleaned_text)
    print("\n----- EXTRACTED SKILLS -----\n")
    print(skills)

    # --------- JOB DESCRIPTION SKILLS ---------
job_folder = "data/raw/jobs"
job_files = os.listdir(job_folder)
print("\nFiles inside jobs folder:", job_files)

if len(job_files) == 0:
    print("No job description files found!")
else:
    job_path = os.path.join(job_folder, job_files[0])
    with open(job_path, "r", encoding="utf-8") as f:
        job_text = f.read()

    cleaned_job_text = clean_text(job_text)
    job_skills = extract_skills(cleaned_job_text)

    print("\n----- JOB DESCRIPTION SKILLS -----\n")
    print(job_skills)

    # --------- SKILL MATCHING ---------
resume_set = set(skills)
job_set = set(job_skills)

common_skills = resume_set.intersection(job_set)
all_skills = resume_set.union(job_set)

match_score = len(common_skills) / len(all_skills) * 100

print("\n----- SKILL MATCH REPORT -----")
print(f"Matching Skills: {list(common_skills)}")
print(f"Match Score: {match_score:.2f}%")