from selenium import webdriver
from selenium.webdriver.common.keys import Keys


email = ""  # add your username or email
password = ""  # add your password
git_username = input("Please enter your GitHub username: ")
name = input("Enter a name for your repository: ")
description = input(
    "Do you want to add description to your repo? [Y/N]: ")
description.lower()
url = "https://github.com/" + git_username + "/" + name

if len(name) != 0 and description == 'n' and len(description) != 0:
    driver = webdriver.Chrome()

    driver.get("https://github.com/login")

    def login():
        email_field = driver.find_element_by_xpath(
            "//*[@id='login_field']")
        password_field = driver.find_element_by_xpath(
            "//*[@id='password']")
        submit_button = driver.find_element_by_xpath(
            "//*[@id='login']/form/div[4]/input[9]")

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.submit()

    login()

    def create_repo():
        new_repository_button = driver.find_element_by_xpath(
            "/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")
        new_repository_button.click()
        repository_name = driver.find_element_by_xpath(
            "//*[@id='repository_name']")
        repository_name.send_keys(name)
        create_repository_button = driver.find_element_by_xpath(
            "//*[@id='new_repository']/div[3]/button")
        create_repository_button.submit()
        driver.close()
        print("Done! Your repository has been created: " + url)
    create_repo()

elif len(name) != 0 and description == 'y' and len(description) != 0:
    description_text = input("Add text here: ")
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")

    def login():
        email_field = driver.find_element_by_xpath(
            "//*[@id='login_field']")
        password_field = driver.find_element_by_xpath(
            "//*[@id='password']")
        submit_button = driver.find_element_by_xpath(
            "//*[@id='login']/form/div[4]/input[9]")

        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.submit()

    login()

    def create_repo():
        new_repository_button = driver.find_element_by_xpath(
            "/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a")
        new_repository_button.click()
        repository_name = driver.find_element_by_xpath(
            "//*[@id='repository_name']")
        repository_name.send_keys(name)

    create_repo()

    def add_description():
        if len(description_text) != 0:
            description_field = driver.find_element_by_xpath(
                "//*[@id='repository_description']")
            description_field.send_keys(description_text)
            create_repository_button = driver.find_element_by_xpath(
                "//*[@id='new_repository']/div[3]/button")
            create_repository_button.submit()
            driver.close()
            print("Done! Your repository has been created: " + url)
        else:
            print("Please enter a text to your description!")

    add_description()

else:
    print("Something went wrong. Try again.")
