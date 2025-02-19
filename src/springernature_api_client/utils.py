import pandas as pd  # type: ignore

def results_to_dataframe(results, export_to_excel=False, filename="output.xlsx"):
    """Convert paginated API response to Pandas DataFrame and optionally export to Excel."""
    if "records" in results and results["records"]:
        df = pd.DataFrame(results["records"])

        if export_to_excel:
            df.to_excel(filename, index=False)
            print(f"✅ Data exported to {filename}")
        
        return df
    
    print("⚠️ No records found. DataFrame is empty.")
    return pd.DataFrame()
