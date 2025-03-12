from collections import defaultdict
import pandas as pd
import time

start_time = time.time()

# Load UMLS database into a hash map (dictionary)
umls_pathway = "MRCONSO.RRF"
umls_dict = {}

with open(umls_pathway, 'r') as umls_database:
    for row in umls_database:
        columns = row.strip().split('|')
        if len(columns) > 14:
            disease_column = columns[14].lower()
            umls_dict[disease_column] = columns[0]  # Storing concept ID

# Load unmapped diseases from TSV file
file_path = "new_unmapped_diseases.tsv"
unmapped_diseases_df = pd.read_csv(file_path, sep='\t')

# Process disease names
mapped_data = []
total_diseases = 0
mapped_count = 0

for index, row in unmapped_diseases_df.iterrows():
    disease_list = eval(row["unmapped_diseases"])  # Convert string list to actual list
    total_diseases += len(disease_list)
    
    for disease in disease_list:
        disease = disease.lower().strip()
        umls_id = umls_dict.get(disease, "")
        if umls_id:
            mapped_count += 1
        mapped_data.append([row["pmcid"], disease, umls_id])

# Save results to TSV file
output_file = "new_mapped_diseases.tsv"
pd.DataFrame(mapped_data, columns=["pmcid", "unmapped_disease", "id"]).to_csv(output_file, sep='\t', index=False)

# Display summary
print(f"Total unmapped diseases processed: {total_diseases}")
print(f"Mapped diseases: {mapped_count}")
print(f"Time taken: {time.time() - start_time:.2f} seconds")
