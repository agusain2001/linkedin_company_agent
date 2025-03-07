# utils.py
import re

def extract_company_name(linkedin_url):
    """
    Extracts company name from a LinkedIn URL if provided.
    Example: 'https://www.linkedin.com/company/openai/' -> 'openai'
    """
    match = re.search(r"linkedin\.com/company/([a-zA-Z0-9-]+)", linkedin_url)
    return match.group(1) if match else None

def validate_input(input_text):
    """
    Validates user input to ensure it's a company name or LinkedIn URL.
    """
    return bool(input_text and len(input_text) > 2)
