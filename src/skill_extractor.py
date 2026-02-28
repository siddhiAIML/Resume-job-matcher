# Central skill database
SKILLS_DB = [
    "python",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit learn",
    "data analysis",
    "artificial intelligence",
    "neural network",
    "nlp",
    "sql",
    "power bi",
    "excel"
]
def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

if __name__ == "__main__":
    sample_text = "I have experience in Python, Machine Learning and TensorFlow."
    skills = extract_skills(sample_text)
    print("Extracted Skills:", skills)