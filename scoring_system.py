import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('punkt_tab')
# Predefined list of relevant skills/keywords
skill_keywords = [
    "python", "django", "flask", "rest", "api", "sql", "database", "aws", "cloud",
    "docker", "postgreSQL", "microservices", "react", "javascript", "node", "devops"
]

def preprocess_text(text):
    """
    Function to preprocess the input text by:
    - Converting to lowercase
    - Removing special characters
    - Tokenizing
    - Removing stopwords
    - Lemmatizing
    """
    # Lowercase the text
    text = text.lower()

    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the tokens (convert words to base form)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Return the cleaned text as a string
    return ' '.join(tokens)

def extract_skills(text, skill_keywords):
    """
    Function to extract skills from preprocessed text by matching predefined skill keywords.
    """
    # Tokenize the preprocessed text
    words = text.split()

    # Find the intersection of words and skill keywords
    extracted_skills = [word for word in words if word in skill_keywords]

    return set(extracted_skills)  # Return unique skills as a set

def preprocess_and_extract_skills(text, skill_keywords):
    """
    Combines the preprocessing and skill extraction into one function.
    - Cleans the input text
    - Extracts the relevant skills from predefined skill keywords
    """
    cleaned_text = preprocess_text(text)
    extracted_skills = extract_skills(cleaned_text, skill_keywords)
    return extracted_skills

# Example job description and resume
job_description = """
We are looking for a Python Developer with experience in Django and Flask. 
The candidate should have knowledge of REST APIs, SQL databases, and cloud platforms like AWS.
"""

resume = """
I am an experienced developer specializing in Python. I have worked with Django, Flask, and developed 
RESTful APIs. My expertise includes working with AWS, PostgreSQL, and containerization tools like Docker.
"""

# Preprocess and extract skills from both the job description and resume
jd_skills = preprocess_and_extract_skills(job_description, skill_keywords)
resume_skills = preprocess_and_extract_skills(resume, skill_keywords)

# Output the extracted skills for both job description and resume
print(jd_skills, resume_skills)
