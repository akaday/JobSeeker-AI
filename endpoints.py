from fastapi import FastAPI
from jobs import JobSeekerAI

app = FastAPI()
job_seeker = JobSeekerAI(api_urls=["https://api.example.com/jobs1", "https://api.example.com/jobs2"])

@app.get("/jobs")
async def get_jobs(keyword: str = None):
    jobs = job_seeker.fetch_job_listings()
    if keyword:
        jobs = job_seeker.filter_jobs_by_keyword(jobs, keyword)
    return jobs
