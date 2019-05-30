# IMDB_REST_API
API implementation of demo IMDB data

## Setup

`$ git clone https://github.com/wasi-m/IMDB_REST_API.git`

**Change dir to project dir**
<br />
`$ cd IMDB_REST_API`

**setup the virtual environment**
<br />
`$ virtualenv venv`

**Activate the virtual environment**
<br />
`$ source venv/bin/activate`

**Install the requirements.txt**
<br />
`$ pip install -r requirements.txt`

**Start the Server**
<br />
`$ python manage.py runserver`

**Vola! your REST API is running**


## Testing the API
**Open the local server in browser**
<br />
`http://127.0.0.1:8000`
> Give all the records present in the Database.

`http://127.0.0.1:8000/1`
> Give the reecord with primary key as *1*.

**Navigate to the admin**
<br />
 `http://127.0.0.1:8000/admin`
> The admin panal for creating, editing and deleting records. 
 
