
FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it firs
ENV PYTHONUNBUFFERED 1

# create /app directory
RUN mkdir /app

# set the current working directory
WORKDIR /app


# Copy the current app files to docker /app
ADD . /app/


# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

VOLUME /carbon_usage

# open port 8000 on docker 
EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py loaddata usage/preloadUType.json && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]