from .api_client import SpringerNatureAPI
import os
from xml.dom import minidom
import re

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
        all_responses = []
        
        # Set pagination limit based on premium status
        max_start = 500 if is_premium else 100

        while s <= max_start:
            print(f"Fetching TDM: query='{q}', page={p}, start={s}")
            
            # Get raw XML response from TDM API (single page)
            response = self._make_request("xmldata/jats", q=q, p=p, s=s, is_tdm=True)
            
            if not isinstance(response, str):
                raise TypeError(f"Expected XML string, got {type(response)}")
            
            # Check if we got content
            if len(response.strip()) > 0:
                all_responses.append(response)
                s += p  # Increment start position by page size
            else:
                print("No more TDM content found.")
                break  # Stop if no data is returned

            if not fetch_all:  # Exit loop if pagination is disabled
                break

        # Return single response or concatenated responses
        if len(all_responses) == 1:
            return all_responses[0]
        else:
            return "\n\n".join(all_responses)

    def save_xml(self, xml_content: str, filename: str = None):
        """
        Save XML content to file with pretty formatting.
        Handles multiple concatenated XML responses gracefully.
        Keeps XML declaration, stylesheet, and DOCTYPE only once at the top.
        """
        try:
            # Auto-generate filename if not provided
            if filename is None:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"output_tdm_{timestamp}.xml"

            # 1️⃣ Separate header (xml declaration, stylesheet, doctype)
            header_pattern = re.compile(
                r'^(<\?xml[^>]*\?>\s*)?(<\?xml-stylesheet[^>]*\?>\s*)?(<!DOCTYPE[\s\S]*?\]>\s*)?',
                re.MULTILINE
            )
            header_match = header_pattern.match(xml_content)
            header = header_match.group(0).strip() if header_match else ""

            # 2️⃣ Remove redundant headers from the rest of the content
            body = header_pattern.sub("", xml_content).strip()

            # 3️⃣ If multiple <response> blocks exist, wrap them in a single root
            if body.count("<response") > 1:
                body = f"<tdm_responses>\n{body}\n</tdm_responses>"

            # 4️⃣ Pretty print safely
            try:
                parsed_xml = minidom.parseString(body)
                pretty_body = parsed_xml.toprettyxml(indent="  ")
            except Exception as parse_err:
                print(f"⚠️ Could not format XML cleanly (saving raw): {parse_err}")
                pretty_body = body

            pretty_body = re.sub(r'\n\s*\n', '\n', pretty_body)

            # 5️⃣ Combine header + formatted body
            pretty_xml = f"{header}\n{pretty_body}" if header else pretty_body

            # 6️⃣ Save to file
            file_path = os.path.join(os.getcwd(), filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(pretty_xml)
                
            return file_path

        except Exception as e:
            print(f"❌ Failed to save XML/TDM response: {e}")
            raise