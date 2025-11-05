import springernature_api_client.tdm as tdm

tdm_client = tdm.TDMAPI(api_key="your_api_key/your_api_metric")

response = tdm_client.search(q='keyword:"cancer"', p=20, s=1, fetch_all=False, is_premium=False)

# Save XML response to file
file_path = tdm_client.save_xml(response, "output_tdm.xml")

print(f"✅ XML response saved successfully to: {file_path}")
