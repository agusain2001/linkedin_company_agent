# app.py
from flask import Flask, request, jsonify
from utils import extract_company_name, validate_input
from linkedin_service import get_linkedin_company_data
from gemini_service import (
    analyze_linkedin_data,
    analyze_hiring_trends,
    analyze_upcoming_projects,
    analyze_company_overview
)

app = Flask(__name__)

@app.route('/get_details', methods=['POST'])
def get_details():
    """
    Endpoint to retrieve company data from LinkedIn and analyze it using Google Gemini.
    Expects a JSON payload with a 'company' field that is either a company name or a LinkedIn URL.
    """
    data = request.get_json()
    company_input = data.get("company")

    if not validate_input(company_input):
        return jsonify({"error": "Invalid input. Please provide a valid company name or LinkedIn URL."}), 400

    # Extract company name if a LinkedIn URL is provided, otherwise use the input directly.
    company_name = extract_company_name(company_input) or company_input

    # Fetch dynamic company data from LinkedIn's API
    linkedin_data = get_linkedin_company_data(company_name)

    # Analyze the fetched data using various functions from gemini_service
    overall_analysis = analyze_linkedin_data(linkedin_data)
    hiring_analysis = analyze_hiring_trends(linkedin_data)
    projects_analysis = analyze_upcoming_projects(linkedin_data)
    overview_analysis = analyze_company_overview(linkedin_data)

    # Construct the response
    response = {
        "overall_analysis": overall_analysis,
        "hiring_analysis": hiring_analysis,
        "projects_analysis": projects_analysis,
        "overview_analysis": overview_analysis,
        "raw_linkedin_data": linkedin_data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
