from .api_client import SpringerNatureAPI
import os
from xml.dom import minidom

class TDMAPI(SpringerNatureAPI):
    def search(self, q: str, p: int = 10, s: int = 1, fetch_all: bool = False, is_premium: bool = False):
        """
        Search TDM API and return raw XML data.

        Parameters:
        - `q`: Search query (e.g., DOI, keyword)
        - `p`: Number of results per page
        - `s`: Starting position (default: 1)
        - `fetch_all`: If True, fetches all pages
        - `is_premium`: Premium access flag

        Returns: Raw XML string response
        """
        print(f"Fetching TDM: query='{q}', page={p}, start={s}")
        
        # Get raw XML response from TDM API
        response = self._make_request("xmldata/jats", q=q, p=p, s=s, is_tdm=True)
        
        if not isinstance(response, str):
            raise TypeError(f"Expected XML string, got {type(response)}")
            
        return response
    
    def save_xml(self, xml_content: str, filename: str = None):
        """
        Save XML content to file with pretty formatting.
        
        Parameters:
        - xml_content: Raw XML string
        - filename: Optional filename, auto-generated if not provided
        
        Returns: File path where XML was saved
        """
        try:
            # Try to pretty print / format the XML
            try:
                parsed_xml = minidom.parseString(xml_content)
                pretty_xml = parsed_xml.toprettyxml(indent="  ")
            except Exception as parse_err:
                print(f"⚠️ Could not format XML (saving raw instead): {parse_err}")
                pretty_xml = xml_content
            
            os.makedirs("exports", exist_ok=True)
            file_path = os.path.join(os.getcwd(), filename)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(pretty_xml)
                
            return file_path

        except Exception as e:
            print(f"❌ Failed to save XML/TDM response: {e}")
            raise