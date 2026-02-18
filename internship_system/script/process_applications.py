
import pandas as pd
import os
INPUT_FILE = 'application.csv'
OUTPUT_FOLDER = 'output/'
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
try:
    df = pd.read_csv(INPUT_FILE)
    print("Successfully loaded application data.")
except FileNotFoundError:
    print(f"Error: '{INPUT_FILE}' not found!")
initial_count = len(df)
df_unique = df.drop_duplicates(subset=['Email'], keep='first')
duplicate_count = initial_count - len(df_unique)
print(f"Removed {duplicate_count} duplicate applications.")
required_fields = ['Skills', 'Availability', 'CGPA']
incomplete_apps = df_unique[df_unique[required_fields].isnull().any(axis=1)]
valid_apps = df_unique.dropna(subset=required_fields)

print(f"Identified {len(incomplete_apps)} incomplete entries for follow-up.")
with pd.ExcelWriter(OUTPUT_FOLDER + 'processed_applications.xlsx') as writer:
    valid_apps.to_excel(writer, sheet_name='Ready_to_Shortlist', index=False)
    incomplete_apps.to_excel(writer, sheet_name='Incomplete_Follow_up', index=False)

print("Process Complete! Open 'output/processed_applications.xlsx' to see the results.")
