# GLDNHRN Search Filter Control

This is a Python script that automates a search process and performs specific actions depending on the results.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Browser
- psutil
- winsound

## Setup and Execution

1. Ensure you have Python 3 installed. If not, you can download it [here](https://www.python.org/downloads/).

2. Clone this repository by running `git clone <repository_url>` in your command line.

3. Install the required Python libraries by running `pip install -r requirements.txt` in your command line.

4. Navigate to the directory of the script using command line and run the Python script using `python script_name.py`.

5. When prompted, enter your username, password, and the URL for the search filter. 

## How It Works

The script uses Selenium to automate the web browsing process. It logs into a specified page using user-provided credentials, then continually refreshes the page and checks for specific conditions on the page. 

If certain conditions are met, the program will output a message to the console and emit a beep sound.

This script is intended to be run on a continuous loop, checking the specified web page every 30 seconds.

## Contribution

Feel free to fork this project, make changes in your own branch and create a PR. All the contributions are welcome.

## Disclaimer

This script is meant for educational purposes only. 

## License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.
