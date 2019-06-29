# Base 
FROM python:3.6

MAINTAINER Manas Mangaonkar <manasmangaonkar@gmail.com>
 
# Copy app code to opt 
ADD . /tallygst 
WORKDIR /tallygst

# Fetch dependencies 
RUN pip install -r requirements.txt 

EXPOSE 5000 

# Start app
CMD ["python", "./tapi.py"]