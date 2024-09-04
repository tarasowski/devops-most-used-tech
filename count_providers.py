import pickle
import pandas as pd

# Step 2: Load the pickle file
pickle_file_path = './descriptions.pkl'
with open(pickle_file_path, 'rb') as f:
    descriptions_list = pickle.load(f)

# Step 3: Define a list of DevOps providers to count
devops_providers = [
    'AWS', 'Azure', 'GCP', 'Git', 'Infrastructure',
    'Monitor', 'Pipeline', 'Python', 'Ansible', 'Terraform', 'Puppet', 'Chef', 'GitLab', 'GitHub Actions',
    'Docker', 'Kubernetes', 'Jenkins', 'Container', 'CLI', 'Pipeline', 'Agile', 'Scrum', 'Linux', 'Shell',
    'Jenkins', 'Certification', 'Software Development', 'Programming', 'Coding', 'Java', 'JavaScript',
    'API', 'Bash', 'Database', 'SQL', 'IAC', 'Orchestration', 'Containerization', 'Powershell', 'CloudFormation',
    'Microservices', 'Lambda', 'DevSecOps', 'Cloud Native', 'Continuous Delivery', 'Continuous Integration',
    'Continuous Deployment'
]

# Step 4: Count the occurrences of each provider in the descriptions
provider_counts = {provider: 0 for provider in devops_providers}
for description in descriptions_list:
    for provider in devops_providers:
        provider_counts[provider] += description.lower().count(provider.lower())

# Step 5: Convert the counts to a DataFrame
df = pd.DataFrame(list(provider_counts.items()), columns=['provider', 'count'])

# Step 6: Sort the DataFrame by the count column in descending order
df = df.sort_values(by='count', ascending=False)

# Step 7: Save the DataFrame to a CSV file
csv_file_path = './devops_provider_counts.csv'
df.to_csv(csv_file_path, index=False)

# Print the DataFrame
print(df)
