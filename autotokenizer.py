from transformers import BertTokenizer, BertModel, BertConfig
from collections import Counter
import pandas as pd
import concurrent.futures

def tokenize_and_count(tokens):
    return Counter(tokens)

def count_and_get_top_words(file_path, model_name, max_seq_length=512, top_n=30, batch_size=8):
    # Load the tokenizer
    tokenizer = BertTokenizer.from_pretrained(model_name, config=BertConfig.from_json_file('/Users/nandukhanal/Documents/Classworks/Semester-1/Software Now/biobert_v1.1_pubmed/bert_config.json'))

    # Read text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split text into chunks of max_seq_length
    chunks = [text[i:i + max_seq_length] for i in range(0, len(text), max_seq_length)]

    # Tokenize chunks in batches
    tokenized_batches = [tokenizer.encode(chunk) for chunk in chunks]

    # Flatten the list of batches into a single list of tokens
    all_tokens = [token for batch in tokenized_batches for token in batch]

    # Use ThreadPoolExecutor for parallel token counting
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Batch tokens for parallel processing
        token_batches = [all_tokens[i:i + batch_size] for i in range(0, len(all_tokens), batch_size)]

        # Submit batches to the executor for parallel processing
        futures = [executor.submit(tokenize_and_count, tokens) for tokens in token_batches]

        # Initialize an empty Counter for token counts
        total_token_counts = Counter()

        # Collect results as they become available
        for future in concurrent.futures.as_completed(futures):
            token_counts = future.result()
            total_token_counts += token_counts

    # Get the top 30 tokens
    top_tokens = total_token_counts.most_common(top_n)

    # Create a DataFrame for visualization
    df = pd.DataFrame(top_tokens, columns=['Token', 'Count'])

    return df

# Replace 'your_text_file.txt' and 'bert-base-uncased' with your file path and model name
file_path = 'all_csv_file.txt'
model_path = '/Users/nandukhanal/Documents/Classworks/Semester-1/Software Now/biobert_v1.1_pubmed'

result_df = count_and_get_top_words(file_path, model_path)

# Display the top 30 words
print(result_df)
