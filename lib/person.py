#!/usr/bin/env python3
"""
Define a name property for your Person class. The name must be of type str and under 25 characters. 
If the name is invalid, the setter method should print() "Name must be string under 25 characters."
Define a job property for your Person class.
If the job is invalid, the setter method should print() "Job must be in list of approved jobs." 
"""

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
    def __init__(self, name='Erica', job='Admin'):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
    def set_name(self, name):
        if (type(name) == str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)

    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
    job = property(get_job, set_job)
