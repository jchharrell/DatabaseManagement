## Jared Harrell, Molly Thomas
This project shows how we can connect PostgreSQL with flask and insert new rows in our database and select distinct items form our table.

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

To access the update_basket_a webpage, navigate to:
```
127.0.0.1:5000/api/update_basket_a
```
To access the unique fruits webpage, navigate to:
```
127.0.0.1:5000/api/unique
```
