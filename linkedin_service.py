import requests
from config import LINKEDIN_API_KEY

def get_linkedin_company_data(company_name):
    """
    Dynamically fetches raw company data using LinkedIn's API.
    This example uses a typical endpoint for fetching organization details.
    Replace the endpoint, parameters, and data extraction logic as per LinkedIn's API documentation.
    """
    endpoint = f"https://api.linkedin.com/v2/organizations?q=universalName&universalName={company_name}"
    headers = {"Authorization": f"Bearer {LINKEDIN_API_KEY}"}
    
    try:
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": f"LinkedIn API returned status {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}
