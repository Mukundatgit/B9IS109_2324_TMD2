
# Clone the Git repository

``` git clone URL https://github.com/Mukundatgit/B9IS109_2324_TMD2 ```

``` cd Vacancy-Management```

# Create and Activate Virtual Environment

``` python -m venv myvenv ```

``` source myvenv/bin/activate ```

# Collect static files

``` python manage.py collectstatic ```


# Install all the required dependencies after activating virtual environment(This includes new library created for this project named - job-application-count)

`` pip install -r requirements.txt ```

# make migrations and migrate

``` python manage.py makemigrations ```
``` python manage.py migrate ```

# Create a superuser 

``` python manage.py createsuperuserpython manage.py createsuperuser ```

#### Enter the email id and password for the superuser - This user would be able to login to django adminstrator page

# Run the application by starting the server

``` python manage.py runserver ```

 ##### And navigate to https://127.0.0.1:8000 to launch the application



 # admin -muk@gmail.com
 # pass-muk123


