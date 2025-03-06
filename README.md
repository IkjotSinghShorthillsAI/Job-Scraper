# Job Scraper and Matcher with Selenium Testing

## 📌 Overview
This project is a **Job Scraper & Matcher** that fetches job listings from **TimesJobs**, filters them based on a candidate's skills and preferred role, and automates UI testing of job postings using **Selenium**.

### ✨ Features
✅ **Web Scraping**: Extract job listings from TimesJobs using `requests` & `BeautifulSoup`  
✅ **OOP Structure**: Modularized classes for scraping, storage, and matching  
✅ **Job Matching**: Filters jobs based on skills and preferred role  
✅ **Selenium UI Testing**: Automates checking job pages for relevance  
✅ **CSV Storage**: Saves all jobs and matched jobs for analysis  

---
## 📂 Project Structure
```
📦 Job Scraper Project
 ┣ 📜 main.py           # Core logic for scraping and job matching
 ┣ 📜 tester.py         # Selenium UI testing script
 ┣ 📜 jobs.csv          # Scraped job listings (output)
 ┣ 📜 filtered_jobs.csv # Matched job listings (output)
 ┣ 📜 README.md         # Project documentation
```

---
## 🚀 Getting Started
### 1️⃣ **Install Dependencies**
Ensure you have Python installed, then install the required libraries:
```bash
pip install requests bs4 selenium
```

For **Selenium WebDriver**, download [ChromeDriver](https://chromedriver.chromium.org/downloads) and place it in your system PATH.

### 2️⃣ **Run Job Scraper & Matcher**
```bash
python main.py
```
- Scrapes job listings from TimesJobs
- Matches jobs based on skills (60% match threshold)
- Saves results to `filtered_jobs.csv`

### 3️⃣ **Run Selenium UI Tester**
```bash
python tester.py
```
- Asks for a keyword to validate job descriptions
- Opens job links in a browser
- Checks if the keyword is present in job descriptions

---
## 🏗️ Code Overview

### `JobScraper` (Web Scraper)
- Fetches job listings from **TimesJobs**
- Extracts title, company, location, skills, and job link

### `JobStorage` (CSV Storage)
- Saves all jobs (`jobs.csv`)
- Saves filtered jobs (`filtered_jobs.csv`)

### `Candidate` (Candidate Profile)
- Stores user’s **name, skills, experience, preferred role, and location**

### `JobMatcher` (Matching Algorithm)
- Matches jobs based on **title similarity** and **skill match percentage**

### `JobUITester` (Selenium UI Tester)
- Opens job links in **Chrome**
- Checks if the **job description contains the keyword**


---
## 📌 Notes
- The scraper **relies on TimesJobs**; structure changes may require updates.
- The Selenium tester **needs ChromeDriver**; update if browser versions change.
