import json


from JobWorker.JobWorker import  JobWorker
from RuleEngine.RuleEngine import RuleEngine
from ValidationEngine.ValidationEngine import ValidationEngine

if __name__ == "__main__":
    with open('min-time.json', 'r') as referenceJob:
        job = json.loads(referenceJob.read())

        # ToDo: Pass Json to JobWorker instead of loading it here
        jobWorker = JobWorker('backendProviderJson', referenceJob)
        jobWorker.start_fetching()
        results = jobWorker.get_results()

        ruleEngine = RuleEngine(job)
        ruleEngine.parse_rules()

        validationEngine = ValidationEngine(ruleEngine, results)
        validationEngine.validate()