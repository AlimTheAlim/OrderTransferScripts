class Project:
    # Constructor to initialize main project information
    def __init__(self, project_name, project_adress, panel_profile, vendor, material_color, gauge, roof_width, roof_specs, cut_list):
        # Initialize project attributes with the provided values
        self._project_name  = project_name  # The name of the project
        self._project_adress = project_adress  # The address of the project
        self._panel_profile = panel_profile  # Profile type of the panel
        self._vendor = vendor  # Vendor supplying materials
        self._material_color = material_color  # Color of the material
        self._gauge = gauge  # The thickness of the material
        self._roof_specs = roof_specs  # Specifications related to the roof
        self._cut_list = cut_list  # List of cuts to be made (possibly materials or dimensions)
        
    # Getter methods for accessing the private attributes
    
    def get_project_name(self):
        # Returns the project name
        return self._project_name
    
    def get_project_adress(self):
        # Returns the project address
        return self._project_adress
    
    def get_material_color(self):
        # Returns the material color
        return self._material_color
    
    def get_gauge(self):
        # Returns the material gauge (thickness)
        return self._gauge
    
    def get_vendor(self):
        # Returns the vendor of the project materials
        return self._vendor
    
    def get_roof_specs(self):
        # Returns the roof specifications
        return self._roof_specs

    def get_cut_list(self):
        # Returns the cut list (this might need iteration based on your needs)
        return self._cut_list
   
    def get_panel_profile(self):
        # Returns the panel profile type
        return self._panel_profile
    
    # Setter methods for modifying the private attributes
    
    def set_project_name(self, project_name):
        # Sets the project name
        self._project_name = project_name
    
    def set_project_adress(self, project_adress):
        # Sets the project address
        self._project_adress = project_adress
    
    def set_material_color(self, material_color):
        # Sets the material color
        self._material_color = material_color
    
    def set_gauge(self, gauge):
        # Sets the material gauge (thickness)
        self._gauge = gauge
        
    def set_vendor(self, vendor):
        # Sets the vendor of the project materials
        self._vendor = vendor
    
    def set_roof_specs(self, roof_specs):
        # Sets the roof specifications
        self._roof_specs = roof_specs
     # Cutlist section: 
    # it is reasonable to make it accessible publicly.    
    def set_cut_list(self, cut_list):
        # Sets the cut list (which can be modified or iterated)
        self._cut_list = cut_list
    
    def set_panel_profile(self, panel_profile):
        # Sets the panel profile type
        self._panel_profile = panel_profile
    

