import re
from ProjectClass import Project
import PdfReader
from libraries import gauges, vendors, panel_profiles, colors

Order = PdfReader.OrderExtractor()

def find_match(data_list, search_str):
    for item in data_list:
        for variant in item:
            if variant.lower() in search_str.lower():
                return item[0]
    return None

def converter():
    try:
        # Reading pattern to find information
        name = re.search(r'Project\s+Address:\s+(.*?)\s+(?:Project\s+Name|Customer\s+Name)', Order).group(1)
        panel_profile = re.search(r'Roofing\s+System:\s+(.*?)\s*(?=\n|$)', Order).group(1)
        material = re.search(r'Metal\s+Type\s+&\s+Color:\s+([^R]+?)\s+Roof\s+Panel\s+Specifics:', Order).group(1)
        roof_specs = re.search(r'Roof\s+Panel\s+Specifics:\s+([^R]+?)\s*(?=\n|$)', Order).group(1)

        # Clean and format
        material = re.sub(r'\s+', ' ', material.replace('\u00A0', ' ').strip())
        panel_profile = next((system[0] for system in panel_profiles.panel_systems if any(system_type.lower() in panel_profile.lower() for system_type in system)), panel_profile)
        vendor = find_match(vendors.vendors, material)
        gauge = find_match(gauges.gauges, material)
        color = find_match(colors.colors, material)

    except (AttributeError, IndexError) as e:
        print(f"Error: {e}, setting default values.")
        name, panel_profile, vendor, gauge, color, roof_specs = ("default name", "System 1000", "Sheffield", "24ga", "regal white", '16" Smooth')

    # Regex pattern for extracting cut list details
    pattern = r"(\d{1,3}'\d{1,2}\")\s+(\d+)\s+([\d.]+)\s+(\d{1,4}'\d{1,2}\")\s+([\d.]+)"
    cutList = []

    for line in Order.strip().split("\n"):
        if not line.strip():
            continue

        matches = re.search(pattern, line.strip())
        if matches:
            length1, qty, null, null1, null2 = matches.groups()
            cleaned_str = re.sub(r'\xa0', ' ', length1)
            cleaned_str = re.sub(r'[^\d\'"]', '', cleaned_str)
            match = re.match(r"(\d+)'(\d+)\"", cleaned_str)

            if match:
                panel_info = {
                    "Number of panels": qty,
                    "Feet Length": int(match.group(1)),
                    "Inch Length": int(match.group(2))
                }
                cutList.append(panel_info)

    # Create Project object
    FFOrder = Project(name, name, panel_profile, vendor, color, gauge, roof_specs, roof_specs, cutList)
    
    return FFOrder

# Test the converter
"""  _summary_
alpha_func = converter()

print("\n", "\n--------------------------------\n", alpha_func.get_project_name(),"\n",
      alpha_func.get_panel_profile(),"\n",alpha_func.get_gauge(),"\n", 
      alpha_func.get_material_color(),"\n",alpha_func.get_roof_specs())

for i in alpha_func.get_cut_list():
    print(i, "\n")
 """