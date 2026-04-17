from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Tell Chrome to detach and stay open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Pass those options to the browser
driver = webdriver.Chrome(options=chrome_options)


# ==========================================
# STEP 1: LOG IN ONLY ONCE (Outside the loop)
# ==========================================
print("Starting up and attempting to log in...")
driver.get("https://spotme.jdn.gov.my")
time.sleep(3) 

try:
    # 1. Enter ID (MyKad)
    id_box = driver.find_element(By.XPATH, "//input[@formcontrolname='mykad']")
    id_box.send_keys("xxxxxxxxxxxx") 

    # 2. Enter Password
    password_box = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
    password_box.send_keys("xxxxxxxxxxxxxxxx") 
    
    # 3. Click the Login Button
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log Masuk')]") 
    login_button.click()
    
    # Wait for the login to process
    time.sleep(5) 
    print("Login successful!")
    
except Exception as e:
    print("Note: Login fields not found. You might already be logged in.")


# ==========================================
# STEP 2: THE INFINITE LOOP
# ==========================================
while True:
    # --- 1. Safely force the browser to pop up ---
    try:
        driver.switch_to.window(driver.current_window_handle) # Focus the window
        driver.minimize_window()
        time.sleep(1)
        driver.maximize_window()
    except Exception:
        # If Chrome complains about being maximized, just ignore it and move on!
        pass 
        
    # --- 2. Do the actual clicking ---
    try:
        # Go directly to the specific dashboard URL
        driver.get("https://spotme.jdn.gov.my/dashboard/pegawai")
        time.sleep(5) 
        
        # Find the Daftar Pergerakan button
        button = driver.find_element(By.XPATH, "//button[normalize-space()='Daftar Pergerakan']")
        
        # Use JavaScript to forcefully click it
        driver.execute_script("arguments[0].click();", button)
        
        print("SUCCESS: Clicked Daftar Pergerakan.")

    except Exception as e:
        print("An error occurred during this run:", e)
    
    print("Waiting before clicking again...")
    
    # Wait exactly 3600 seconds (1 hour) before the loop starts over
    time.sleep(3660)