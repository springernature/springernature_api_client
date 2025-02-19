import springernature_api_client.tdm as tdm
from springernature_api_client.utils import results_to_dataframe

tdm_client = tdm.TDMAPI(api_key="your_api_key")

response = tdm_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=True, is_premium=True)

# Convert to DataFrame and export to Excel
df = results_to_dataframe(response, export_to_excel=True)

print(df.head())
