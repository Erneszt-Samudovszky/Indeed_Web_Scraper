import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

URL = "https://www.indeed.co.uk/jobs?q=python&l=United+Kingdom&start" 

Companies, Locations, Jobs, Salaries = [],[],[],[]
pages = np.arange(1, 50, 10)

for page in pages:
    page = requests.get(URL + str(page))
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})

    for x in results:
        company = x.find('span', attrs={"class":"company"})
        if company:
            print("\n")
            print('company:', company.text.strip() )
            Companies.append(company.text.strip())

        location = x.find("span", attrs={"class":"location"})
        if location:
            print("location:", location.text.strip())
            Locations.append(location.text.strip())

        job = x.find('a', attrs={'data-tn-element': "jobTitle"})
        if job:
            print('job:', job.text.strip())
            Jobs.append(job.text.strip())

        salary = x.find('span', attrs={"class":"salaryText"})
        if salary:
            print('salary:', salary.text.strip())
            Salaries.append(salary.text.strip())

python_jobs = pd.DataFrame({"Company":pd.Series(Companies), "Location":pd.Series(Locations),"Job":pd.Series(Jobs), "Salary":pd.Series(Salaries)})


print(python_jobs.to_string())
python_jobs.to_csv("python_jobs.csv")
