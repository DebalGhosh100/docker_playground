FROM python:3.8

RUN mkdir /employee_db_interface

WORKDIR /employee_db_interface

RUN pip install --upgrade pip

COPY . /employee_db_interface

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x /employee_db_interface/main.py

CMD ["python", "/employee_db_interface/main.py"]
