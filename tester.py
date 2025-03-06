from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

class JobUITester:
    def __init__(self, keyword, csv_file="jobs.csv"):
        self.keyword = keyword.lower()  # Convert to lowercase for case-insensitive matching
        self.csv_file = csv_file
        self.driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

    def test_job_links(self):
        with open(self.csv_file, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            jobs = list(reader)

        for job in jobs[:5]:
            job_title = job["title"]
            job_url = job["info"]

            print(f"Testing job: {job_title}")
            self.driver.get(job_url)  # Open job page
            time.sleep(3)  # Wait for page to load

            # Extract job description (modify selector as per the website structure)
            try:
                page_desc = self.driver.find_element(By.TAG_NAME, "body").text.lower()
            except:
                page_desc = ""

            # Check if keyword exists in description
            if self.keyword in page_desc:
                print(f"✅ Match found for '{self.keyword}' in {job_title} ({job_url})")
            else:
                print(f"❌ No match found for '{self.keyword}' in {job_title} ({job_url})")

        self.driver.quit()  # Close browser after testing

# Run Selenium Tester
if __name__ == "__main__":
    keyword = input("Enter job keyword to validate: ")
    tester = JobUITester(keyword)
    tester.test_job_links()
