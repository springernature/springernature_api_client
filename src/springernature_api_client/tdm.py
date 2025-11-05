from .api_client import SpringerNatureAPI
import os
from xml.dom import minidom
import re
from datetime import datetime

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
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"output_tdm_{timestamp}.xml"

            # 1. Separate header (xml declaration, stylesheet, doctype)
            header_pattern = re.compile(
                r'^(<\?xml[^>]*\?>\s*)?(<\?xml-stylesheet[^>]*\?>\s*)?(<!DOCTYPE[\s\S]*?\]>\s*)?',
                re.MULTILINE
            )
            header_match = header_pattern.match(xml_content)
            header = header_match.group(0).strip() if header_match else ""

            # 2. Remove redundant headers from the rest of the content
            body = header_pattern.sub("", xml_content).strip()

            # 3. Use regex to count only actual <response> tags (not <responseType>, <responses>, etc.)
            response_tag_count = len(re.findall(r'<response(\s|>)', body))
            if response_tag_count > 1:
                body = f"<tdm_responses>\n{body}\n</tdm_responses>"

            # 4. Pretty print safely
            try:
                parsed_xml = minidom.parseString(body)
                pretty_body = parsed_xml.toprettyxml(indent="  ", encoding=None).split('\n', 1)[1]
            except Exception as parse_err:
                print(f"⚠️ Could not format XML cleanly (saving raw): {parse_err}")
                pretty_body = body

            # Remove XML declaration from pretty_body if present
            xml_decl_pattern = re.compile(r'^<\?xml[^>]*\?>\s*', re.MULTILINE)
            xml_decl_match = xml_decl_pattern.match(pretty_body)
            if xml_decl_match:
                pretty_body = pretty_body[xml_decl_match.end():]
            pretty_body = re.sub(r'\n\s*\n', '\n', pretty_body)

            # 5. Combine header + formatted body, ensure newline after header
            if header:
                pretty_xml = f"{header}\n{pretty_body.lstrip()}"
            else:
                pretty_xml = pretty_body

            # 6. Save to file
            file_path = os.path.join(os.getcwd(), filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(pretty_xml)
                
            return file_path

        except Exception as e:
            print(f"❌ Failed to save XML/TDM response: {e}")
            raise