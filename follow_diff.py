from bs4 import BeautifulSoup
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


parser = argparse.ArgumentParser(description="Compare Instagram followers and following lists.")
parser.add_argument("-f", "--followers", required=True, help="Path to the followers HTML file")
parser.add_argument("-g", "--following", required=True, help="Path to the following HTML file")
parser.add_argument("-u", "--username", required=True, help="Username")
parser.add_argument("-p", "--password", required=True, help="Path to the password HTML file")


args = parser.parse_args()


followers_path = args.followers
following_path = args.following
username = args.username
password = args.password


with open(followers_path, "r", encoding="utf-8") as file:
    followers_html = file.read()

with open(following_path, "r", encoding="utf-8") as file:
    following_html = file.read()

print("Files read successfully!\n")


followers_soup = BeautifulSoup(followers_html, "html.parser")
following_soup = BeautifulSoup(following_html, "html.parser")


followers = set(a.text for a in followers_soup.find_all("a") if a.get("href", "").startswith("https://www.instagram.com/"))
following = set(a.text for a in following_soup.find_all("a") if a.get("href", "").startswith("https://www.instagram.com/"))


not_following_back = following - followers

print("Those who don't follow you: " + str(len(not_following_back)) + " users\n")
for user in not_following_back:
    print("- " + user)


print("\nStarting the unfollow process...\n")


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")


time.sleep(2)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(5)

for user in not_following_back:
    driver.get(f"https://www.instagram.com/{user}/")
    time.sleep(3)
    try:
        unfollow_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Takiptesin')]")
        unfollow_button.click()
        time.sleep(1)
        confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Takip etmeyi bırak')]")
        confirm_button.click()
        print(f"{user} unfollowed.")
    except Exception as e:
        print(f"Error unfollowing {user}: {e}")
    time.sleep(random.randint(10, 60))

driver.quit()
