import requests
from typing import List, Dict

class JobSeekerAI:
    def __init__(self, api_urls: List[str]):
        self.api_urls = api_urls

    def fetch_job_listings(self) -> List[Dict]:
        all_jobs = []
        for url in self.api_urls:
            response = requests.get(url)
            if response.status_code == 200:
                jobs = response.json().get('jobs', [])
                all_jobs.extend(jobs)
            else:
                print(f"Failed to fetch jobs from {url}")
        return all_jobs

    def filter_jobs_by_keyword(self, jobs: List[Dict], keyword: str) -> List[Dict]:
        return [job for job in jobs if keyword.lower() in job['title'].lower()]

    def filter_jobs_by_location(self, jobs: List[Dict], location: str) -> List[Dict]:
        return [job for job in jobs if location.lower() in job['location'].lower()]

    def filter_jobs_by_company(self, jobs: List[Dict], company: str) -> List[Dict]:
        return [job for job in jobs if company.lower() in job['company'].lower()]
