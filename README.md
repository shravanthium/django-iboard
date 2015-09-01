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


**Solution/ Tasks Performed:**

Github Issues API provides an information rich json response.
Take any public github repo url and construct url for Github API request.
https://api.github.com/repos/<user>/<repo> return list of issues and the response
header contains link for pagination.

1. Construct url for api request specific to user provided repository
2. Make api request for the given repo and capture next urls
3. Parse the reponse and compute set of data as expected in the output
4. Deploy the application 
Tech Stack:
Django 1.8
Github API's

**Enhancements:**
- Migrate the code to golang for better performace with concurrency
- Dockerize the django app 
    
