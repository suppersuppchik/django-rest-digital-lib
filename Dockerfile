FROM python:3.11
WORKDIR /app 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python digitallibrary/manage.py migrate 
# RUN cd digitallibrary

CMD ["python","digitallibrary/manage.py","runserver","0.0.0.0:8000"]


