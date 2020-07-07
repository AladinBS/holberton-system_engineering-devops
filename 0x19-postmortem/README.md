## POSTMORTEM ##
The README for project `0x19-postmortem` located within the `holberton-system_engineering-devops` repo is actually a postmortem based off multiple past projects. It is an issue that rises all the time.

### Issue Summary ###
Project issue started on April 29th 2020.

The impact this issue had was that the project was not able to be tested on. Data in the SQL database was not able to be accessed.

The root cause of this issue was that the MySQL service was never started. This issue was found by running the command:
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py
```
This issue was resolved by running the command:
```
sudo service mysql start
```
This may be prevented in the future by checking if the MySQL service is running before using it in anyway. This can also be applied to any other services that may be used, such as `nginx`.

### Timeline ###
* Issue occurred after running a command with a test file that interacted with the MySQL database.
* Issue detected when error message appeared.
* Actions taken was to investigate the test file.
* Misleading investigation of test file as the issue wasn't there.
* Incident escalated to asking fellow cohort 10 student, Ezra Nobrega, to take a look at the error message.
* Nobrega told me the MySQL service needed to be started before being able to interact with it.

### For Such a Simple Mistake... ###
Remember to always read the error messages and to not panic! The initial panic caused me to not rationally think and simply Google what was wrong if I could not figure it out from the line `Can't connect to local MySQL server` within:
```
sqlalchemy.exc.OperationalError: (_mysql_exceptions.OperationalError) (2002, "Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)") (Background on this error at: http://sqlalche.me/e/e3q8)
```
At least it wasn't a memory leak! Those can be hard to figure out:

![alt text](https://github.com/AladinBS/holberton-system_engineering-devops/blob/master/0x19-postmortem/memory_leak.jpg "Memory Leak Joke")

But all jokes aside... remember to always test your code because:

![alt text](https://github.com/AladinBS/holberton-system_engineering-devops/blob/master/0x19-postmortem/test_bugs.png "Code and Bugs Come")
