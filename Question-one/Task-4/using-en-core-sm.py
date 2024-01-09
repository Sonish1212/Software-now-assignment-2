import spacy

# Load the 'en_core_sci_sm' model
nlp = spacy.load('en_core_sci_sm')

def extract_entities_from_file(file_path):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Process the text using spaCy
    doc = nlp(text)

    # Extract 'diseases' and 'drugs' entities separately
    diseases = []
    drugs = []

    for ent in doc.ents:
        if ent.label_ == 'DISEASE':
            diseases.append(ent.text)
        elif ent.label_ == 'DRUG':
            drugs.append(ent.text)

    return diseases, drugs

# Give the file path and run the function
file_path = 'all_csv_file.txt'
diseases, drugs = extract_entities_from_file(file_path)

# Print the extracted entities
print("Diseases:", diseases)
print("Drugs:", drugs)