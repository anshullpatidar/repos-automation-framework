from selenium.webdriver.common.by import By


class RepositoriesPage():
    locator_dictionary = {
        'repo': [By.XPATH, "//*[@class='flex-auto']"],
        'repo_name': [By.XPATH, "h3/a"],
        'repo_description': [By.XPATH, "p"]
    }

    def __init__(self, webDriver):
        self.webDriver = webDriver

    def get_repo(self):
        repos = self.webDriver.driver.find_elements(By.XPATH, "//*[@class='flex-auto']")
        ui_repos = {}

        for repo in repos:
            name = repo.find_element(By.XPATH, "h3/a").text
            description_web_element = repo.find_elements(By.XPATH, "p")
            description = None if len(description_web_element) == 0 else description_web_element[0].text
            ui_repos[name] = description
        return ui_repos