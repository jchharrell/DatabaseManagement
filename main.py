from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='vboxuser'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/api/update_basket_a')
# this is how you define a function in Python
def index_update():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    try:
    	cursor.execute("INSERT INTO basket_a VALUES (5, 'Cherry')")
    	status = ["Success!"]
    except Exception as e:
    	print("Error updating basket_a")
    	status = e
    
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html',table_title = status)
    
    
@app.route('/api/unique')
# this is how you define a function in Python
def index_unique():
    # this is your index page
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands(fetch is best for SELECT, execute for other commands)
    record_a = util.run_and_fetch_sql(cursor, "Select fruit_a FROM basket_a Left JOIN basket_b on fruit_a = fruit_b where b is null")
    record_b = util.run_and_fetch_sql(cursor, "Select fruit_b FROM basket_a Right JOIN basket_b on fruit_a = fruit_b where a is null")
    if record_a == -1 or record_b == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = ["Unique Fruits_A","Unique Fruits_B"]
        # only use the first five rows
        log_a = record_a[:5]
        log_b = record_b[:5]
        # log=[[1,2],[3,4]]
        combined_result = list(zip(log_a, log_b))
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = combined_result, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)


