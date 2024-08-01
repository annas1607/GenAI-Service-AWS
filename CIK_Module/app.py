#print('Hello, World!')
#def greet(name='World'):
    #print(f'Hello, {name}!')
#greet('Alice')

import requests

# Step 3: Private helper methods
def _construct_url(cik, year, form_type, quarter=None):
    if form_type == "10-K":
        return f"https://www.sec.gov/Archives/edgar/data/{cik}/{year}/10-K"
    elif form_type == "10-Q" and quarter:
        return f"https://www.sec.gov/Archives/edgar/data/{cik}/{year}/10-Q{quarter}"
    else:
        raise ValueError("Invalid form type or missing quarter for 10-Q")

def _get_filing_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Step 1: Create the `annual_filing` method
def annual_filing(cik, year):
    url = _construct_url(cik, year, "10-K")
    return _get_filing_data(url)

# Step 2: Create the `quarterly_filing` method
def quarterly_filing(cik, year, quarter):
    url = _construct_url(cik, year, "10-Q", quarter)
    return _get_filing_data(url)

# Existing methods
def get_document_url(cik, accession_number, primary_document):
    base_url = "https://www.sec.gov/Archives/edgar/data"
    document_url = f"{base_url}/{cik}/{accession_number}/{primary_document}"
    return document_url

def download_document(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve document: {response.status_code}")
        return None

def main():
    cik = "320193"  # Example CIK number
    accession_number = "000032019324000069"  # Example accession number
    primary_document = "aapl-20240330.htm"  # Example primary document name

    headers = {
        "User-Agent": "Anna Sanchez asa1607@wgu.edu"
    }

    document_url = get_document_url(cik, accession_number, primary_document)
    document_content = download_document(document_url, headers)

    if document_content:
        with open("document.html", "wb") as file:
            file.write(document_content)
        print("Document downloaded successfully.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
    # Test annual_filing
    annual_data = annual_filing("320193", "2023")
    print(annual_data)
    
    # Test quarterly_filing
    quarterly_data = quarterly_filing("320193", "2023", "Q1")
    print(quarterly_data)
