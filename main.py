import requests
from bs4 import BeautifulSoup
import csv

class JobScraper:
    def __init__(self, keyword, location):
        self.keyword = keyword
        self.location = location
        self.base_url = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords={keyword}&cboWorkExp1=-1&txtLocation={location}".format(keyword=keyword, location=location)

    def fetch_jobs(self):
        # params = {"q": self.keyword, "l": self.location}
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        
        for job_card in soup.find_all("div", class_="srp-listing clearfix"):
            job_title= job_card.find("div",class_="srp-job-heading").h3.text
            info = job_card.find('a')['href']
            skills = job_card.find_all('a',class_="srphglt")
            company = job_card.find('h4').find('span',class_="srp-comp-name").text .strip()
            location = job_card.find("div", class_="srp-loc").text.strip()
            jobs.append({"company": company, "title": job_title,"location": location, "skills": [skill.text for skill in skills], "info": info})
        
        return jobs


class JobStorage:
    @staticmethod
    def save_jobs_to_csv(jobs, filename="jobs.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["company", "title","location", "skills", "info"])
            writer.writeheader()
            writer.writerows(jobs)

    @staticmethod
    def save_filtered_jobs_to_csv(jobs, filename="filtered_jobs.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["company", "title","location", "skills", "info", "skill_match_percentage"])
            writer.writeheader()
            writer.writerows(jobs)

        



class Candidate:
    def __init__(self, name, skills, experience, preferred_role, location):
        self.name = name
        self.skills = skills  # List of skills
        self.experience = experience  # Years of experience
        self.preferred_role = preferred_role  # Job title preference
        self.location = location

    def __str__(self):
        return f"{self.name} | {self.experience} years | Skills: {', '.join(self.skills)} | Preferred Role: {self.preferred_role} | Location: {self.location}"



class JobMatcher:
    @staticmethod
    def match_jobs(candidate, job_list, skill_match_threshold=0.6):
        matched_jobs = []
        
        for job in job_list:
            job_title = job["title"].lower()
            job_skills = job["skills"]  # List of required skills
            
            # Title Matching: Check if preferred role is in job title
            title_match = candidate.preferred_role.lower() in job_title

            # Skill Matching: Count matching skills
            candidate_skills = set([skill.lower() for skill in candidate.skills])
            job_skills_set = set([skill.lower() for skill in job_skills])
            common_skills = candidate_skills.intersection(job_skills_set)

            # Calculate skill match percentage
            skill_match_percentage = len(common_skills) / len(job_skills_set) if job_skills_set else 0
            
            # Consider a job a match if title matches OR skill match % is >= threshold
            if title_match or skill_match_percentage >= skill_match_threshold:
                matched_jobs.append({
                    **job,  # Include all job details
                    "skill_match_percentage": round(skill_match_percentage * 100, 2)  # Add match %
                })

        return matched_jobs

if __name__ == "__main__":

    # Step 1: Create Candidate Profile
    name = "John Doe"
    skills = ['python', 'django', 'api', 'sql', 'nosql']
    experience = 3
    preferred_role = "Python"
    location = "Bangalore"


    candidate = Candidate(name, [skill.strip() for skill in skills], experience, preferred_role, location)

    # Step 2: Scrape Jobs
    scraper = JobScraper(candidate.preferred_role, candidate.location)
    jobs = scraper.fetch_jobs()

    # Step 3: Match Jobs
    matched_jobs = JobMatcher.match_jobs(candidate, jobs)

    # Filter jobs with at least 60% skill match
    filtered_jobs = [job for job in matched_jobs if job["skill_match_percentage"] >= 60]

    # Step 4: Save Matched Jobs to CSV
    if filtered_jobs:
        # Print Matched Jobs
        print("\nMatched Jobs (60%+ Skill Match):\n" + "-" * 40)
        for idx, job in enumerate(filtered_jobs, start=1):
            print(f"{idx}. {job['title']} at {job['company']} ({job['location']})")
            print(f"   Skills: {', '.join(job['skills'])}")
            print(f"   Match Score: {job['skill_match_percentage']}%")
            print(f"   Info: {job['info']}\n")
    else:
        print("\nNo jobs found with 60% or more skill match.")

    # Save all matched jobs to CSV
    JobStorage.save_filtered_jobs_to_csv(filtered_jobs)
    print(f"\nMatched Jobs saved to 'filtered_jobs.csv' file.")


