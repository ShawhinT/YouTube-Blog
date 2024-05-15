# start from python base image
FROM python:3.10

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# append project and data directories to PYTHONPATH 
ENV PYTHONPATH "${PYTHONPATH}:/code/app/"

# add python code
COPY ./app/ /code/app/

# specify default commands
CMD ["fastapi", "run", "app/main.py", "--port", "80"]