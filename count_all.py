import pickle
from bs4 import BeautifulSoup
import n_gram
import pandas as pd

# Step 2: Define the path to the pickle file
pickle_file_path = './descriptions.pkl'

# Step 3: Open the pickle file in read-binary mode
with open(pickle_file_path, 'rb') as f:
    # Step 4: Load the contents of the pickle file
    descriptions_list = pickle.load(f)

# Step 2: Define a function to clean a single HTML string


def clean_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    return soup.get_text()


# Step 3: Apply the function to each string in the array
cleaned_descriptions = [clean_html(description)
                        for description in descriptions_list]

# Extract n-grams
n_grams = n_gram.keyword_extractor(cleaned_descriptions)

# Define a filtering function


def filter_n_grams(n_grams):
    return {k: v for k, v in n_grams.items() if len(k) > 2}


# Apply the filtering function
filtered_n_grams = filter_n_grams(n_grams)

# Print or process the filtered n-grams
print(filtered_n_grams)

df = pd.DataFrame(list(filtered_n_grams.items()),
                  columns=['keyword', 'appearance'])

# Save the DataFrame to a CSV file
csv_file_path = './filtered_n_grams.csv'
df.to_csv(csv_file_path, index=False)

# Print or process the filtered n-grams
print(filtered_n_grams)
