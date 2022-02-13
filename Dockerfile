FROM python:3.9  

WORKDIR /code

COPY ./Pipfile /code/Pipfile

RUN pip install -p

COPY ./main.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
