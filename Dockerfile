FROM python:3.12
COPY . /internetshop
WORKDIR /internetshop
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]

