from ExtractToClassConverter import converter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service  
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select

def webInteractor():
    order = converter()  
    edge_path = 'repos\\FFAutoOrder\\msedgedriver.exe'  
    
    
    service = Service(edge_path)
    options = Options()  
    
    
    # Initialize the Edge WebDriver
    driver = webdriver.Edge(service=service, options=options)
    
    #Log in
    driver.get('https://metalroofingsystems.biz/OIS/index.php')
    username = driver.find_element(By.ID, 'txtUsername')  
    password = driver.find_element(By.ID, 'txtPassword')  
    username.send_keys('')
    password.send_keys('')
    password.send_keys(Keys.RETURN)
    
    
    
    #Create Job
    driver.get('https://metalroofingsystems.biz/OIS/job_type.php')
    newJob = driver.find_element(By.CSS_SELECTOR, 'a[href="create_job.php"]')
    newJob.click()
    
    
    #Job stuff
    jobName = order.get_project_name()
    jobNameField = driver.find_element(By.ID, 'txtJobName')
    jobNameField.send_keys(jobName)
    dropdownCustomer = driver.find_element(By.ID, "selCustomer")
    select = Select(dropdownCustomer)
    select.select_by_visible_text("FLORES AND FOLEY")
    submitJobName = driver.find_element(By.ID, 'SubmitJob')
    submitJobName.click()
    radioButtonPanel = driver.find_element(By.CSS_SELECTOR, 'input[name="radOrderType"][value="Panel"]')
    radioButtonPanel.click()
    submitJobDetails = driver.find_element(By.CSS_SELECTOR,'input[name="btnNext"][value="Next"]')
    submitJobDetails.click()
    
    
    #Panel setup
    dropdownPanel = driver.find_element(By.ID, "selProduct")
    
    select = Select(dropdownPanel)
    select.select_by_visible_text(order.get_panel_profile())
    
    if driver.find_element(By.CSS_SELECTOR, 'input[id="radClipRelief0"][value="Yes"]'):
      radioButtonPanel = driver.find_element(By.CSS_SELECTOR, 'input[id="radClipRelief0"][value="Yes"]')
      radioButtonPanel.click()
    
    dropdownWidth = driver.find_element(By.ID, "selWidth")
    select = Select(dropdownWidth)
    select.select_by_visible_text('16"')
    
    
    dropdownVendor = driver.find_element(By.ID, "selVendor")
    select = Select(dropdownVendor)
    select.select_by_visible_text(order.get_vendor())
    
    dropdownColor = driver.find_element(By.ID, "txtColor")
    select = Select(dropdownColor)
    select.select_by_visible_text(order.get_material_color())
    
    dropdownGauge = driver.find_element(By.ID, "selGauge")
    select = Select(dropdownGauge)
    select.select_by_visible_text(order.get_gauge())
    
    radioButtonDel = driver.find_element(By.CSS_SELECTOR, 'input[name="radDelivery"][value="Delivery"]')
    radioButtonDel.click()
    
    Contact1 = driver.find_element(By.ID, 'txtContact')
    Contact1.send_keys("Alim Aminev")
    
    Contact2 = driver.find_element(By.ID, 'txtContact2')
    Contact2.send_keys("843-347-6673")
    
    Contact3 = driver.find_element(By.ID, 'txtContact3')
    Contact3.send_keys("aaminev@metalroofingsystems.com")
    
    submitPanel = driver.find_element(By.ID, 'submitOrder')
    submitPanel.click()
    
    k = 0
    for index, item in enumerate(order.get_cut_list(), start=1):  # start=1 to match ID numbering starting from 1
    # Dynamically find the fields based on the index
      amount_input = driver.find_element(By.ID, f'txtQty{index}')
      length_ft_input = driver.find_element(By.ID, f'txtFeet{index}')
      length_in_input = driver.find_element(By.ID, f'txtInch{index}')
      
      # Enter the amount and hit Tab to go to the next field
      amount_input.clear()
      amount_input.send_keys(item['Number of panels'])
      amount_input.send_keys(Keys.TAB)

      # Enter the length in feet and hit Tab to go to the next field
      length_ft_input.clear()
      length_ft_input.send_keys(item['Feet Length'])
      length_ft_input.send_keys(Keys.TAB)

      # Enter the length in inches and hit Enter to submit the line
      length_in_input.clear()
      length_in_input.send_keys(item['Inch Length'])
      length_in_input.send_keys(Keys.RETURN)
      k += 1
      remove_buttons = driver.find_elements(By.XPATH, '//a[contains(@href, "create_panel_list.php?Remove=")]')

    # Define which k-th button you want to interact with
    k = 3  # For example, interact with the 3rd button (zero-based index)

    # Make sure k is a valid index
    if 0 <= k < len(remove_buttons):
        # Click on the k-th button
        remove_buttons[k].click()
    else:
        print(f"Invalid index: {k}")
    OrderFinish = driver.find_element(By.ID, 'btnSubmit')
    OrderFinish.click()
    
    Confirm = driver.find_element(By.CSS_SELECTOR, 'input[name="Submit"][value="Confirm Order"]')
    Confirm.click()
    print(driver.title)  # Print the title of the webpage
      # Close the browser after use
      