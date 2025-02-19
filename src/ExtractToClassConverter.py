import re
from ProjectClass import Project  # Importing the Project class to use later
import PdfReader  
from libraries import gauges, vendors, panel_profiles, colors  # Import predefined data for matching

# Instantiate the OrderExtractor object to read order data from a PDF
Order = PdfReader.OrderExtractor()

# Helper function to search for a matching string from a list of items
def find_match(data_list, search_str):
    for item in data_list:
        # Iterate through each variant in the item
        for variant in item:
            # If any variant matches the search string (case-insensitive), return the first element (standardized value)
            if variant.lower() in search_str.lower():
                return item[0]
    return None  # If no match is found, return None

# Converter function to parse the order data and create a Project object
def converter():
    try:
        # Use regular expressions to extract project-related details from the PDF order data
        name = re.search(r'Project\s+Address:\s+(.*?)\s+(?:Project\s+Name|Customer\s+Name)', Order).group(1)
        panel_profile = re.search(r'Roofing\s+System:\s+(.*?)\s*(?=\n|$)', Order).group(1)
        material = re.search(r'Metal\s+Type\s+&\s+Color:\s+([^R]+?)\s+Roof\s+Panel\s+Specifics:', Order).group(1)
        roof_specs = re.search(r'Roof\s+Panel\s+Specifics:\s+([^R]+?)\s*(?=\n|$)', Order).group(1)

        # Clean and format the extracted strings (e.g., removing unwanted characters or excess spaces)
        material = re.sub(r'\s+', ' ', material.replace('\u00A0', ' ').strip())
        # Match panel profile with predefined systems (from libraries) based on the extracted material
        panel_profile = next((system[0] for system in panel_profiles.panel_systems if any(system_type.lower() in panel_profile.lower() for system_type in system)), panel_profile)
        # Use find_match helper function to find matching vendor, gauge, and color from predefined lists
        vendor = find_match(vendors.vendors, material)
        gauge = find_match(gauges.gauges, material)
        color = find_match(colors.colors, material)

    except (AttributeError, IndexError) as e:
        # In case of an error (e.g., no match found), use default values for the project attributes
        print(f"Error: {e}, setting default values.")
        name, panel_profile, vendor, gauge, color, roof_specs = ("default name", "System 1000", "Sheffield", "24 ga", "Regal White", '16" Smooth')

    # Regex pattern for extracting cut list details, like panel lengths and quantities
    pattern = r"(\d{1,3}'\d{1,2}\")\s+(\d+)\s+([\d.]+)\s+(\d{1,4}'\d{1,2}\")\s+([\d.]+)"
    cutList = []

    # Split the extracted order data into lines and iterate through each line
    for line in Order.strip().split("\n"):
        if not line.strip():  # Skip empty lines
            continue

        # Try to match the line with the cut list regex pattern
        matches = re.search(pattern, line.strip())
        if matches:
            # Extract relevant details (length, quantity, etc.) from the matched line
            length1, qty, null, null1, null2 = matches.groups()
            cleaned_str = re.sub(r'\xa0', ' ', length1)  # Remove non-breaking spaces
            cleaned_str = re.sub(r'[^\d\'"]', '', cleaned_str)  # Clean up unwanted characters

            # Extract feet and inches from the cleaned length string
            match = re.match(r"(\d+)'(\d+)\"", cleaned_str)
            if match:
                # Create a dictionary to store panel information (length and quantity)
                panel_info = {
                    "Number of panels": qty,
                    "Feet Length": int(match.group(1)),
                    "Inch Length": int(match.group(2))
                }
                cutList.append(panel_info)  # Add the panel info to the cut list

    # Set default values for the project attributes if they weren't extracted correctly
    if name == None:
        name = "default name"
    if panel_profile == None:
        panel_profile = "System 1500"
    if vendor == None:
        vendor = "Sheffield"
    if color == None:
        color = "Slate Gray"
    if gauge == None:
        gauge = ".032 Alum."
    
    # Create a Project object with the gathered and cleaned data
    FFOrder = Project(name, name, panel_profile, vendor, color, gauge, roof_specs, roof_specs, cutList)
    
    return FFOrder  # Return the created Project object

# Test the converter (uncomment to test)
"""
alpha_func = converter()

# Print out various project details using the getter methods
print("\n", "\n--------------------------------\n", alpha_func.get_project_name(),"\n",
      alpha_func.get_panel_profile(),"\n",alpha_func.get_gauge(),"\n", 
      alpha_func.get_material_color(),"\n",alpha_func.get_roof_specs())

# Iterate through the cut list and print the details
for i in alpha_func.get_cut_list():
    print(i, "\n")
"""
