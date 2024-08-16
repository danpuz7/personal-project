FROM python

ADD myproject.py .

CMD ["python", "./myproject.py"]
