from LangchainGeminiUC import classify_patient
import pandas as pd
import json

# Load the Excel file
df = pd.read_excel("./Data/patient_records.xlsx")

for row in df.itertuples(index=True):
    print(row.id, row.name, row.age)

for row in df.itertuples(index=True):
    row_dict = row._asdict()
    row_json = json.dumps(row_dict)
    print(row_json)
    result = classify_patient(row_json)
    print("Classification Result:")
    print(result)
