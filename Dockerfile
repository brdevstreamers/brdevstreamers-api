FROM python:3.9  

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY /etc/letsencrypt/live/api.brstreamers.dev/privkey.pem /code/privkey.pem
COPY /etc/letsencrypt/live/api.brstreamers.dev/cert.pem /code/cert.pem

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

CMD ["python", "main.py"]
