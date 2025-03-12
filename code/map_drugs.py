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
            drug_column = columns[14].lower()
            umls_dict[drug_column] = columns[0]  # Storing concept ID

# Load unmapped drugs from TSV file
file_path = "new_unmapped_drugs.tsv"
unmapped_drugs_df = pd.read_csv(file_path, sep='\t')

# Process drug names
mapped_data = []
total_drugs = 0
mapped_count = 0

for index, row in unmapped_drugs_df.iterrows():
    drug_list = eval(row["unmapped_drugs"])  # Convert string list to actual list
    total_drugs += len(drug_list)
    
    for drug in drug_list:
        drug = drug.lower().strip()
        umls_id = umls_dict.get(drug, "")
        if umls_id:
            mapped_count += 1
        mapped_data.append([row["pmcid"], drug, umls_id])

# Save results to TSV file
output_file = "new_mapped_drugs.tsv"
pd.DataFrame(mapped_data, columns=["pmcid", "unmapped_drug", "id"]).to_csv(output_file, sep='\t', index=False)

# Display summary
print(f"Total unmapped drugs processed: {total_drugs}")
print(f"Mapped drugs: {mapped_count}")
print(f"Time taken: {time.time() - start_time:.2f} seconds")
