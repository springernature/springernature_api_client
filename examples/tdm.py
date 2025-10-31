import os
from xml.dom import minidom
from springernature_api_client.tdm import TDMAPI

tdm_client = TDMAPI(api_key="your_api_key/your_api_metric")

try:
    # Get raw XML response directly as a string
    response = tdm_client._make_request(
        "xmldata/jats",
        q='keyword:"cancer"',
        p=20,
        s=1,
        is_tdm=True
    )

    if not isinstance(response, str):
        print("❌ Expected XML string, got something else.")
        raise TypeError(f"Got {type(response)} instead of str")

    try:
        parsed_xml = minidom.parseString(response)
        pretty_xml = parsed_xml.toprettyxml(indent="  ")
    except Exception as parse_err:
        print(f"⚠️ Could not format XML (saving raw instead): {parse_err}")
        pretty_xml = response

    os.makedirs("exports", exist_ok=True)
    file_path = os.path.join(os.getcwd(), "output.xml")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"✅ XML response saved successfully to {file_path}")

except Exception as e:
    print(f"❌ Failed to save XML/TDM response: {e}")

