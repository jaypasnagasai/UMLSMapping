# EXTERNAL DATABASE MAPPING - DISEASES AND DRUGS [UMLS]

## OVERVIEW
These scripts map the unmapped diseases and drugs to UMLS Concept Unique Identifiers (CUIs) using the `MRCONSO.RRF` database file. They take a list of unmapped diseases or drugs and attempt to find corresponding UMLS IDs, saving the results in a TSV file.

## SCRIPTS
### 1. [map_diseases.py](code/map_diseases.py)
- Reads a **UMLS database file** (`MRCONSO.RRF`) to create a mapping of disease names to UMLS CUIs.
- Reads a **TSV file** ([new_unmapped_diseases.tsv](input/new_unmapped_diseases.tsv)) containing a list of unmapped diseases.
- Attempts to map diseases to their UMLS Concept IDs.
- Saves the mapped data to `new_mapped_diseases.tsv`.
- Prints a summary of total processed and mapped diseases.

### 2. [map_drugs.py](code/map_drugs.py)
- Reads a **UMLS database file** (`MRCONSO.RRF`) to create a mapping of drug names to UMLS CUIs.
- Reads a **TSV file** ([new_unmapped_drugs.tsv](input/new_unmapped_drugs.tsv)) containing a list of unmapped drugs.
- Attempts to map drugs to their UMLS Concept IDs.
- Saves the mapped data to `new_mapped_drugs.tsv`.
- Prints a summary of total processed and mapped drugs.

## INPUTS/OUTPUTS

### Input Files
- `MRCONSO.RRF`: UMLS concept file used for mapping.
- [new_unmapped_diseases.tsv](input/new_unmapped_diseases.tsv): TSV file containing unmapped diseases.
- [new_unmapped_drugs.tsv](input/new_unmapped_drugs.tsv): TSV file containing unmapped drugs.

### Output Files
- `new_mapped_diseases.tsv`: Output file containing mapped disease names with UMLS CUIs.
- `new_mapped_drugs.tsv`: Output file containing mapped drug names with UMLS CUIs.

## Usage
1. Ensure that `MRCONSO.RRF`, [new_unmapped_diseases.tsv](input/new_unmapped_diseases.tsv), and [new_unmapped_drugs.tsv](input/new_unmapped_drugs.tsv) are in the same directory as the scripts.
2. Run the scripts:
   ```bash
   python map_diseases.py
   python map_drugs.py
   ```
3. Check the output files (`new_mapped_diseases.tsv` and `new_mapped_drugs.tsv`) for results.

## DEPENDENCIES
- Python 3
- `pandas` library

## PERFORMANCE
- The scripts use a dictionary (hash map) for fast lookups.
- They process the entire dataset in a single iteration for efficiency.

## RESULTS
| File Name               | Total Rows | Unresolved Terms        | Resolved Terms     |
|-------------------------|-----------|----------------------|----------------------|
| new_mapped_diseases.tsv | 35,465    | 21,813 (61.5%)      | 13,652 (38.5%)      |
| new_mapped_drugs.tsv    | 118,594   | 99,023 (83.5%)      | 19,571 (16.5%)      |

## NOTES
- Click On [MRCONSO.RRF](https://drive.google.com/file/d/1Mlxzq2SFChJc3UyR7F90VBSEEdbptbl3/view?usp=sharing) for downloading the UMLS database
- The scripts assume disease and drug names are **case-insensitive** and **stripped of whitespace**.
- The following script does not use any **LLMs**.
