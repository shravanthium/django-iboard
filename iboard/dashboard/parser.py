import json
import requests
from datetime import datetime, timedelta
from dateutil.parser import parse
from django.utils.timezone import utc


def fetch_data(url):
"""Take repo issues url and fetch data for all the available number of pages"""

    data = requests.get(url)
    response = json.loads(data.content)
    if data.status_code ==403:
        return {"error":"Your Daily Limit Exceeded"}
    if not response:
        return {"error":"No Issues Raised!!"}
    if data.headers.get("link"):
        pageNum = int(data.headers.get(
                "link").split(
                ",")[1].split(
                ";")[0].replace(
                "<","").replace(
                ">","").split("=")[1])
        for i in range(2,pageNum+1):
            next_url = url+"?page="+str(i)
            response.extend(json.loads(requests.get(next_url).content))
    return parse_json(response)

   
def parse_json(response):
"""Parse the response from github issues API and compute stats"""

    open_issues = 0
    last24hrs_issues = 0
    last7days_issues = 0
    prior7days_issues = 0

    for r in response:
        if r.get("state") =="open":
            open_issues += 1

        if datetime.utcnow().replace(tzinfo=utc)-parse(r.get(
            "created_at")) < timedelta(days=1) and r.get("state") =="open":
            last24hrs_issues += 1

        if datetime.utcnow().replace(tzinfo=utc)-parse(r.get(
            "created_at")) > timedelta(days=1) and datetime.utcnow().replace(
            tzinfo=utc)-parse(r.get("created_at")) < timedelta(days=7) and 
            r.get("state") =="open":
            last7days_issues += 1

        if datetime.utcnow().replace(tzinfo=utc)-parse(r.get(
            "created_at")) > timedelta(days=7) and r.get("state") =="open":
            prior7days_issues += 1

    return {
        "count":open_issues,
        "last_24hrs":last24hrs_issues,
        "last_7days":last7days_issues,
        "before_7days":prior7days_issues
        }
