import re
import PyPDF2
import sys
import os
import pandas as pd


def find_programming_languages_in_resume(resume_text):
    # Define a list of programming languages
    programming_languages = [
        'JavaScript',
        'Python',
        'Java',
        'C',
        'Swift',
        'Ruby',
        'C#',
        'PHP',
        'Kotlin',
        'Rust',
        'Ruby on Rails',
        'Go',
        'TypeScript',
        'Perl',
        'Dart',
        'R',
    ]

    # Create a regular expression pattern to match variations of programming languages
    pattern = r'\b(?:' + '|'.join(re.escape(lang) for lang in programming_languages) + r')\b'

    # Use the regular expression to find matches in the resume text
    matches = re.findall(pattern, resume_text, re.IGNORECASE)  # Case-insensitive matching

    # Remove duplicates by converting the list to a set and then back to a list
    unique_matches = list(set(matches))

    return unique_matches

# Open the PDF file and extract text
pdf_file_path = "CV.pdf"
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    resume_text = ''
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

# Use the find_programming_languages_in_resume function to find matches
programming_language_matches = find_programming_languages_in_resume(resume_text)

# Pass programming_language_matches to calculate_domain_sums from score_counter

domains = [
        "Frontend",
        "Backend",
        "Mobile Dev",
        "Game Dev",
        "Data Science",
        "AI",
        "QA",
        "DevOps",
        "Cybersecurity",
        "DB Admin",
        "Networking",
        "Embedded",
    ]


def calculate_domain_sums(languages):
    # Load the Excel file
    file_path = "programming_languages.xlsx"  # Replace with the path to your Excel file
    df = pd.read_excel(file_path)

    # Group by domain and calculate the sum
    

    domain_sums = {domain: 0 for domain in domains}

    for language in languages:
        if language in df['Programming Language'].tolist():
            selected_language = df[df['Programming Language'] == language]
            for domain in domains:
                domain_sums[domain] += selected_language[domain].values[0]

    return [domain_sums[domain] for domain in domains]

# Example usage:
domain_scores = calculate_domain_sums(programming_language_matches)

print(domains)
print("Domain Scores:", domain_scores)

print (programming_language_matches)