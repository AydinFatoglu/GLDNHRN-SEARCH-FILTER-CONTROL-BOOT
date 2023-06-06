import os
import psutil
import winsound
import atexit
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



print("\033[92m" + "GLDNHRN SEARCH FILTER CONTROL BOOT" + "\033[0m")

# Prompt the user for the username and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")
url = input("Enter Search Filter URL: ")

# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

# Create Chrome WebDriver

# Create Chrome WebDriver with headless option
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)


# Store the PIDs of the Chrome and ChromeDriver processes
chrome_pid = None
chromedriver_pid = None


def get_process_pid(process_name):
    for proc in psutil.process_iter(["name", "pid"]):
        if proc.info["name"] == process_name:
            return proc.info["pid"]
    return None


def perform_search():
    # Select the element on the page
    element = driver.find_element(
        By.CSS_SELECTOR, "div.table-scrollable#table-scrollable"
    )

    # Get the selected text of the element
    selected_text = element.text

    # Define the path to the text file
    file_path_team_members = "team_members.txt"  # Update with your file path
    
    # Define the path to the text file
    file_path_group = "group.txt"  # Update with your file path

    # Read the names from the text file
    with open(file_path_team_members, "r") as file:
        names = file.read().splitlines()
        
    # Open the file in read mode
    with open(file_path_group, "r") as file:
        # Read the content of the file
        text_to_check = file.read()
        
    

    # Assign the names to the sentences_to_search variable
    sentences_to_search = names



    # Check if any of the sentences are not found in the selected text
    # and if the text_to_check is present
    not_found = False
    if text_to_check in selected_text and not any(
        sentence in selected_text for sentence in sentences_to_search
    ):
        not_found = True

    return selected_text, not_found


# Function to be called when the script exits
def cleanup():
    # Quit the browser
    driver.quit()

    # Terminate the Chrome and ChromeDriver processes started by the script
    if chrome_pid:
        chrome_process = psutil.Process(chrome_pid)
        chrome_process.terminate()

    if chromedriver_pid:
        chromedriver_process = psutil.Process(chromedriver_pid)
        chromedriver_process.terminate()


# Register the cleanup function with atexit
atexit.register(cleanup)

# Go to link for TH filter
driver.get(url)


# Store the PIDs of the Chrome and ChromeDriver processes
chrome_pid = get_process_pid("chrome.exe")
chromedriver_pid = get_process_pid("chromedriver.exe")

# Wait for the login page to fully load
wait = WebDriverWait(driver, 10)
username_input = wait.until(
    EC.visibility_of_element_located((By.ID, "userid"))
)  # Replace "username" with the actual ID or selector of the username input field
password_input = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)  # Replace "password" with the actual ID or selector of the password input field
login_button = wait.until(
    EC.visibility_of_element_located((By.ID, "btn_login"))
)  # Replace "login-button" with the actual ID or selector of the login button

# Enter login credentials
username_input.send_keys(username)  # Use the username entered by the user
password_input.send_keys(password)  # Use the password entered by the user

# Perform login action
os.system("cls" if os.name == "nt" else "clear")
login_button.click()
os.system("cls" if os.name == "nt" else "clear")

# Wait for the page to fully load
wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.table-scrollable#table-scrollable")
    )
)

# Loop the search every minute
os.system("cls" if os.name == "nt" else "clear")
while True:
    # Refresh the page
    os.system("cls" if os.name == "nt" else "clear")
    driver.refresh()
    os.system("cls" if os.name == "nt" else "clear")

    # Wait for the page to fully load
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.table-scrollable#table-scrollable")
        )
    )

    # Perform the search
    os.system("cls" if os.name == "nt" else "clear")
    selected_text, not_found = perform_search()
    os.system("cls" if os.name == "nt" else "clear")
    # Check if the conditions are met
    if not_found:
        frequency = 900  # Set the beep frequency (adjust as needed)
        duration = 100  # Set the beep duration in milliseconds (adjust as needed)
        winsound.Beep(frequency, duration)
        
        print("\033[92m" + "Filtrede Mudahaleye Baslamayi Bekleyen Çagri var!" + "\033[0m")
        print('\033[92m' + '' + '\033[0m')

    # Check if "Kayıt bulunamadı!" is in the selected text
    if "Kayıt bulunamadı!" in selected_text:
        print('\u001b[31m' + 'Filtrede Hiç Kayıt Yok!' + '\u001b[31m')
        print('\033[92m' + '' + '\033[0m')
        time.sleep(2)
        
        

    # Wait for 5 seconds before the next iteration
    print('\u001b[31m' + 'Tekrar kontrol ediliyor' + '\u001b[31m')
    print('\033[92m' + '' + '\033[0m')
    time.sleep(30)
   




