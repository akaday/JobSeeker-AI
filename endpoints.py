from fastapi import APIRouter
from jobs import JobSeekerAI

router = APIRouter()

# Sample API URLs, replace these with real job search API endpoints
api_urls = [
    "https://api.example.com/jobs1",
    "https://api.example.com/jobs2"
]

job_seeker = JobSeekerAI(api_urls)

@router.get("/jobs")
async def get_jobs(keyword: str = None):
    jobs = job_seeker.fetch_job_listings()
    if keyword:
        jobs = job_seeker.filter_jobs_by_keyword(jobs, keyword)
    return jobs

@router.get("/jobs/location")
async def get_jobs_by_location(location: str):
    jobs = job_seeker.fetch_job_listings()
    jobs = job_seeker.filter_jobs_by_location(jobs, location)
    return jobs

@router.get("/jobs/company")
async def get_jobs_by_company(company: str):
    jobs = job_seeker.fetch_job_listings()
    jobs = job_seeker.filter_jobs_by_company(jobs, company)
    return jobs

@router.get("/jobs/salary")
async def get_jobs_by_salary(min_salary: int):
    jobs = job_seeker.fetch_job_listings()
    jobs = [job for job in jobs if job['salary'] >= min_salary]
    return jobs
