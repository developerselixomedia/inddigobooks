import pandas as pd

df = pd.read_excel('Updated_Catalog.xlsx')
print('Columns:', df.columns.tolist())

# Check for Jaag Piyari
jaag = df[df['Title'].astype(str).str.contains('Jaag Piyari', case=False, na=False)]
print('\n--- Jaag Piyari rows ---')
for idx, row in jaag.iterrows():
    print(dict(row[['Title', 'Author', 'Binding', 'ISBN', 'MRP', 'Pages', 'Publisher']]))

# Check for Karbala
karbala = df[df['Title'].astype(str).str.contains('Karbala', case=False, na=False)]
print('\n--- Karbala rows ---')
for idx, row in karbala.iterrows():
    print(dict(row[['Title', 'Author', 'Binding', 'ISBN', 'MRP', 'Pages', 'Publisher']]))
