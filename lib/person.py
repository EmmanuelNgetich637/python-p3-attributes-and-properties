#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unknown"):
        self.name = self.validate_name(name)
        self.job = self.validate_job(job)
    
    def validate_name(self, name):
        if not isinstance(name,str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return None 
        else:
            return name.title()
        
    def validate_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return None
        else:
            return job
        
        