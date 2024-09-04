import pandas as pd
import pickle

# Step 2: Read the CSV file
file_path = "./jobs_rows.csv"
df = pd.read_csv(file_path)

# Step 3: Extract the 'description' column
descriptions = df['description']

# Step 4: Convert the 'description' column to a list of strings
descriptions_list = descriptions.tolist()

# Step 5: Save the list of strings to a pickle file
pickle_file_path = "./descriptions.pkl"
with open(pickle_file_path, 'wb') as f:
    pickle.dump(descriptions_list, f)
