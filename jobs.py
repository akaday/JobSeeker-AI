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
                jobs = response.json().get('jobs
