# django-iboard

A Django App to summarize information related to issues of any given Github repo.

**Input:**
User can input a link to any public GitHub repository

**Output:**
display a table with the following information -

- Total number of open issues

- Number of open issues that were opened in the last 24 hours

- Number of open issues that were opened more than 24 hours ago but less than 7 days ago

- Number of open issues that were opened more than 7 days ago 


**Tasks Performed:**

Github Issues API provides an information rich json response.
Take any public github repo url and construct url for Github API request.
API request to *https://api.github.com/repos/{user}/{repo}* returns list of issues and the response
header contains link for pagination.

1. Construct url for api request specific to user provided repository
2. Make api request for the given repo and capture next urls
3. Parse the reponse and compute set of aggregations as expected in the output
4. Display the result in a table
5. 
Technology Stack Used:
Django 1.8
Digitalocean for deployment
Github API's to fetch the relevant data

**Enhancements:**
- Migrate the code to golang for better performace
- Dockerize the app
    
