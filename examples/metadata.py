import springernature_api_client.metadata as metadata
from springernature_api_client.utils import results_to_dataframe

metadata_client = metadata.MetadataAPI(api_key="your_api_key")

response = metadata_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)

# Convert to DataFrame and export to Excel
df = results_to_dataframe(response, export_to_excel=True)

print(df.head())
