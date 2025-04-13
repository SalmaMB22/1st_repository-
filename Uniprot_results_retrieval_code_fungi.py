# Import the tool to fetch data from UniProt
import requests

# Your API URL (uncompressed FASTA)
api_url = "https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=%28%28taxonomy_id%3A4751%29+AND+%28gene%3A%28egt1%29+OR+egt2%29%29"

# Send the request to UniProt
response = requests.get(api_url)

# Check if it worked
if response.status_code == 200:
    # Save the response to a FASTA file
    with open("uniprot_results_fungi.fa", "w", encoding="utf-8") as file:
        file.write(response.text)
    
    # Show the first few lines on screen
    print("First few lines of the FASTA file:")
    print(response.text[:500])
    print("Done! Check 'uniprot_results_fungi.fa' for the full FASTA file.")
else:
    print(f"Oops! Something went wrong. Error code: {response.status_code}")