# Python3 Flask Rest API

This project is a Restful API use for gene name live-search. I also deployed the API to Heroku, so you can also use this API in the cloud platform. 

---
## 1. Setup

Please install python3 and pip in advance. 

### Clone repository to your local machine
```bash
$ git clone https://github.com/JKChang2015/flask_rest_api.git
$ cd flask_rest_api
```

### To Setup and Start
```bash
$ pip install -r requirements.txt 
$ python app.py

# to debug/development mode, run
$ python app.py --debug
```
### Unit Test & output
```bash
$ nosetests --verbosity=2

Test baseURL redirection ... ok
Test output contents ... ok
Test gene_suggest query case_sensitivity ... ok
Test gene_suggest species case_sensitivity ... ok
Test missing required parameters ... ok
Test unmatched species input - NOT FOUND ... ok
Test unmatched query input - NOT FOUND ... ok
Test invalid limit input - BAD REQUEST ... ok
Test Response is a well-formed JSON object ... ok
Test output limitation ... ok
Test no output limitation ... ok
Test '.' in the query ... ok

----------------------------------------------------------------------
Ran 12 tests in 2.172s

OK
```

### Implementation CI/CD in Heroku
GitHub Integration features work together with Heroku CI, every submission to Github will be detected and tested.
![cicd.png](/resources/heroku_cicd.png)
 

<br><br>
## 2. Implement
### Get gene_suggest
#### Hosted Locally
```bash
$ curl -X GET "http://127.0.0.1:5000/gene_suggest?query=brc&species=homo_sapiens&limit=10" -H  "accept: application/json"
```

#### Hosted online
```bash
$ curl -X GET "https://jkchang.herokuapp.com/gene_suggest?query=brc&species=homo_sapiens&limit=10" -H  "accept: application/json"
```


<br><br>
## 3. Swagger UI - API documentation
![swagger.png](/resources/swagger.png)
#### Hosted Locally 
http://127.0.0.1:5000/swagger &nbsp; &nbsp; &nbsp; &nbsp; or &nbsp; &nbsp; &nbsp; &nbsp; http://127.0.0.1:5000/

#### Hosted online
https://jkchang.herokuapp.com/swagger/  &nbsp; &nbsp; &nbsp; &nbsp; or &nbsp; &nbsp; &nbsp; &nbsp; https://jkchang.herokuapp.com/


<br><br>
## 4.Gene suggest web app
I also created a species-suggest endpoint to guide client's input. 

![live_search.gif](/resources/live_search.gif)
#### Hosted Locally 
http://127.0.0.1:5000/livesearch

#### Hosted online
https://jkchang.herokuapp.com/livesearch
