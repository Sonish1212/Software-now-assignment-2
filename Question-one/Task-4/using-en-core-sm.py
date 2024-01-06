import spacy

# Load the en_core_sci_sm model
nlp = spacy.load('en_core_sci_sm')

# Function to extract entities from a batch
def extract_entities(batch):
    docs = list(nlp.pipe(batch))
    diseases = [ent.text for doc in docs for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for doc in docs for ent in doc.ents if ent.label_ == 'DRUG']
    return diseases, drugs

# Process the text file in batches
file_path = 'all_csv_file.txt'  # Replace with the actual path to your text file
batch_size = 100  # Adjust the batch size as needed

diseases = []
drugs = []

with open(file_path, 'r', encoding='utf-8') as file:
    while True:
        batch = file.read(batch_size)
        if not batch:
            break  # Break if there's no more content
        diseases_batch, drugs_batch = extract_entities(batch)
        diseases.extend(diseases_batch)
        drugs.extend(drugs_batch)

# Print the final results
print("Diseases:", diseases)
print("Drugs:", drugs)