from .api_client import SpringerNatureAPI

class MetadataAPI(SpringerNatureAPI):
    def search(self, q: str, p: int = 10, s: int = 1, fetch_all: bool = False, is_premium: bool = False):
        """
        Search metadata dynamically with pagination.

        Parameters:
        - `q`: Search query (e.g., DOI, keyword, subject)
        - `p`: Number of results per page
        - `s`: Starting position (default: 1)
        - `fetch_all`: If True, fetches until `s=200`

        Returns: JSON response with all records
        """
        all_results = []

        while s <= 500 if is_premium else 100:
            print(f"Fetching metadata: query='{q}', page={p}, start={s}")
            
            response = self._make_request("metadata/json", q=q, p=p, s=s)

            if response and "records" in response:
                all_results.extend(response["records"])
                s += p  # Increment `s` by page size `p`
            else:
                print("No more records found or API returned an empty response.")
                break  # Stop if no data is returned

            if not fetch_all:  # Exit loop if pagination is disabled
                break

        return {"records": all_results}
