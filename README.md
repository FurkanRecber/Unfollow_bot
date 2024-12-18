# Unfollow Bot

Unfollow Bot is a Python script that compares Instagram followers and following lists, identifies users who don't follow you back, and automatically unfollows them.

---

## Features

- Compares followers and following lists.
- Identifies users who don't follow you back.
- Automates the unfollowing process for identified users.

---

## Requirements

- Python 3.7 or higher
- `selenium`
- `bs4` (BeautifulSoup)
- Google Chrome browser and **ChromeDriver** (must match your browser version)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/FurkanRecber/Unfollow_bot.git
    cd Unfollow_bot
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. If you don't have **ChromeDriver**, download it from the [ChromeDriver website](https://chromedriver.chromium.org/downloads) and set it up according to your system.

---

## Usage

### 1. Export HTML Files

1. Log in to Instagram via a web browser.
2. Save the **Followers** and **Following** lists:
   - For **Followers**: Right-click on the page and choose "View Page Source" to save the HTML.
   - For **Following**: Repeat the same process.

### 2. Run the Bot

Run the script using the following command:

    ```bash
    python unfollow_bot.py -f <followers.html_path> -g <following.html_path> -u <username> -p <password>
    ```

- **`<followers.html_path>`**: Path to the saved followers HTML file
- **`<following.html_path>`**: Path to the saved following HTML file
- **`<username>`**: Your Instagram username
- **`<password>`**: Your Instagram password

### Example

    ```bash
    python unfollow_bot.py -f ./followers.html -g ./following.html -u myusername -p mypassword
    ```

---

## Output

1. The bot lists users who don't follow you back.
2. It sequentially unfollows these users.

---

## Security

- Your username and password are not stored anywhere. These credentials are only used to log in.
- Use this bot only for your own account. Managing other accounts without permission may violate Instagram's terms of service.

---

## Contributing

To contribute, fork the repository, make your changes, and submit a **pull request**.

---

## Notes

- Instagram enforces limits on the number of follow/unfollow actions within a specific time period. Performing too many actions in a short time may result in temporary account restrictions.
- The script includes a random delay (10-60 seconds) between unfollow actions. You can adjust this by modifying the `random.randint(10, 60)` part of the code.

---

**Disclaimer:** This project is intended for personal use and does not encourage violating Instagram's terms of service.
