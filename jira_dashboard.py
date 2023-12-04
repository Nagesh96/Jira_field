import requests
import json

# Jira API endpoint for searching issues
url = "https://your-jira-instance.atlassian.net/rest/api/2/search"

# Headers with authentication details
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic YOUR_BASE64_ENCODED_CREDENTIALS"
}

# Version name manipulation for JQL query
version_name = "1.0"  # Example version name
formatted_version_name = f'"{version_name}"'  # Format version name for JQL query

# JQL query with version field manipulation
jql_query = f'project = MYPROJECT AND fixVersion = {formatted_version_name}'

# Data for the search request
search_data = {
    "jql": jql_query,
    "maxResults": 10  # Adjust the number of results as needed
}

# Convert search data to JSON
data_json = json.dumps(search_data)

# Make the POST request to search for issues
response = requests.post(url, headers=headers, data=data_json)

# Check the response
if response.status_code == 200:
    print("Search successful!")
    search_results = response.json()
    # Process the retrieved issues
    for issue in search_results['issues']:
        print(f"Issue: {issue['key']} - Summary: {issue['fields']['summary']}")
else:
    print(f"Search failed. Status code: {response.status_code}")
    print(response.text)
