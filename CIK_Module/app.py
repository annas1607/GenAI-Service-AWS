#print('Hello, World!')
#def greet(name='World'):
    #print(f'Hello, {name}!')
#greet('Alice')

import requests

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
        "User-Agent": "MLT GS gspivey@mlt.org"
    }

    document_url = get_document_url(cik, accession_number, primary_document)
    document_content = download_document(document_url, headers)

    if document_content:
        with open("document.html", "wb") as file:
            file.write(document_content)
        print("Document downloaded successfully.")

if __name__ == "__main__":
    main()
