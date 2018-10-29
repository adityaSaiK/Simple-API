# this sentence pulls python3 from dockerhub
# it comes with ubuntu with python3
FROM python:3

# maintain this as the working directory
WORKDIR /usr/src/app

COPY requirements.txt .
# run pip install to install these requirements recursively
RUN pip install --no-cache-dir -r requirements.txt

#copy all the files from out directory to the created machine
COPY . .
CMD ["python", "app.py"]
