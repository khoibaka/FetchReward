# How to run server:
1. Initialize a new virtualenv in install packages
   - virtualenv env
   - window: .\env\Scripts\activate
   - pip install -r requirements.txt

2. Go in to main directory
   - cd fetchreward
3. Run the server:
   - python manage.py runserver

# How to call the api
1. After run the server, the api call will be <local_url>/api/version/compare. By default <local_url> will be localhost:8888
2. 2 parameters will be first and second contain first and second version string to be compared.
3. Api call will return a Json contain {result: <result>}. <result> will be in 'before', 'after', or 'equal'
   
