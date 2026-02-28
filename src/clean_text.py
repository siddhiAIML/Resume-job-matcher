import re

def clean_text(text):
    # convert to lowercase
    text = text.lower()
    
    # remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


# Testing cleaning function
if __name__ == "__main__":
    sample_text = "Hello!!! AI/ML Engineer 2025."
    print(clean_text(sample_text))