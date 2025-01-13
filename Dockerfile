FROM python:3.9


WORKDIR /code/app


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./fast_zero_aula01 /code/app


CMD ["fastapi", "run", "/code/app/app.py", "--port", "8000"]