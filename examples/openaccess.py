import springernature_api_client.openaccess as openaccess
from springernature_api_client.utils import results_to_dataframe

openaccess_client = openaccess.OpenAccessAPI(api_key="your_api_key")

response = openaccess_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)

# Convert to DataFrame and export to Excel
df = results_to_dataframe(response, export_to_excel=True)

print(df.head())
