

class Project:
    #constructor have main project info
    def __init__(self, project_name, project_adress, panel_profile, vendor, material_color, gauge, roof_width, roof_specs , cut_list):
        self._project_name  = project_name
        self._project_adress = project_adress
        self._panel_profile = panel_profile
        self._vendor = vendor
        self._material_color =  material_color
        self._gauge = gauge
        self._roof_specs = roof_specs
        self._cut_list = cut_list
        
    #Getter Section
    def get_project_name(self):
        return self._project_name
    
    def get_project_adress(self):
        return self._project_adress
    
    def get_material_color(self):
        return self._material_color
    
    def get_gauge(self):
        return self._gauge
    
    def get_vendor(self):
        return self._vendor
    
    def get_roof_specs(self):
        return self._roof_specs

    def get_cut_list(self):
        return self._cut_list
   
    def get_panel_profile(self):
        return self._panel_profile
    
    #Setter Section
    def set_project_name(self, project_name):
        self._project_name = project_name
    
    def set_project_adress(self, project_adress):
        self._project_adress = project_adress
    
    def set_material_color(self, material_color):
        self._material_color = material_color
    
    def set_gauge(self, gauge):
        self._gauge = gauge
        
    def set_vendor(self, vendor):
        self._vendor = vendor
    
    def set_roof_specs(self, roof_specs):
        self._roof_specs = roof_specs
        
    def set_cut_list(self, cut_list):
        self._cut_list = cut_list
    
    def set_panel_profile(self, panel_profile):
        self._panel_profile = panel_profile
    
    #Cutlist, I will make it not a private part as it will have to be iterated
    





        