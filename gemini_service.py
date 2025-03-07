# gemini_service.py
import google.generativeai as genai
from config import GENAI_API_KEY

# Configure Google Gemini API
genai.configure(api_key=GENAI_API_KEY)

def analyze_linkedin_data(linkedin_data):
    """
    Uses Google Gemini to analyze raw LinkedIn data and generate a detailed report.
    The prompt is constructed dynamically using the data fetched from LinkedIn.
    """
    if 'error' in linkedin_data:
        return f"Error fetching LinkedIn data: {linkedin_data['error']}"
    
    element = linkedin_data.get('elements', [{}])[0]
    name = element.get('name', 'N/A')
    industry = element.get('industries', ['N/A'])[0] if element.get('industries') else 'N/A'
    headquarters = element.get('headquarters', 'N/A')
    website = element.get('website', 'N/A')
    description = element.get('description', 'N/A')
    
    prompt = f"""
    Analyze the following LinkedIn company data and provide a detailed report:
    
    Company Name: {name}
    Industry: {industry}
    Headquarters: {headquarters}
    Website: {website}
    Description: {description}
    
    Provide insights on the company's operations, current hiring trends, potential upcoming projects, and any other notable information.
    """
    
    response = genai.generate_text(model="gemini-pro", prompt=prompt)
    return response.text if response else "No analysis available."

def analyze_hiring_trends(linkedin_data):
    """
    Uses Google Gemini to analyze the company's hiring trends from the LinkedIn data.
    """
    if 'error' in linkedin_data:
        return f"Error fetching LinkedIn data: {linkedin_data['error']}"
    
    element = linkedin_data.get('elements', [{}])[0]
    hiring_status = element.get('hiring_status', 'N/A')
    
    prompt = f"""
    Analyze the following hiring information and provide insights on current recruitment trends and future strategies:
    
    Hiring Status: {hiring_status}
    """
    
    response = genai.generate_text(model="gemini-pro", prompt=prompt)
    return response.text if response else "No hiring analysis available."

def analyze_upcoming_projects(linkedin_data):
    """
    Uses Google Gemini to analyze the company's upcoming projects from the LinkedIn data.
    """
    if 'error' in linkedin_data:
        return f"Error fetching LinkedIn data: {linkedin_data['error']}"
    
    element = linkedin_data.get('elements', [{}])[0]
    upcoming_projects = element.get('upcoming_projects', 'N/A')
    
    prompt = f"""
    Analyze the following upcoming projects information and provide insights on potential business impact, project timelines, and strategic value:
    
    Upcoming Projects: {upcoming_projects}
    """
    
    response = genai.generate_text(model="gemini-pro", prompt=prompt)
    return response.text if response else "No upcoming projects analysis available."

def analyze_company_overview(linkedin_data):
    """
    Uses Google Gemini to generate a comprehensive overview of the company based on LinkedIn data.
    """
    if 'error' in linkedin_data:
        return f"Error fetching LinkedIn data: {linkedin_data['error']}"
    
    element = linkedin_data.get('elements', [{}])[0]
    name = element.get('name', 'N/A')
    industry = element.get('industries', ['N/A'])[0] if element.get('industries') else 'N/A'
    headquarters = element.get('headquarters', 'N/A')
    website = element.get('website', 'N/A')
    description = element.get('description', 'N/A')
    hiring_status = element.get('hiring_status', 'N/A')
    upcoming_projects = element.get('upcoming_projects', 'N/A')
    
    prompt = f"""
    Provide a comprehensive overview of the company with the following details:
    
    Company Name: {name}
    Industry: {industry}
    Headquarters: {headquarters}
    Website: {website}
    Description: {description}
    Hiring Status: {hiring_status}
    Upcoming Projects: {upcoming_projects}
    
    Summarize the company's overall strategy, market position, and future outlook.
    """
    
    response = genai.generate_text(model="gemini-pro", prompt=prompt)
    return response.text if response else "No overview available."
