FROM python:3.7

ADD src /src

ADD . .

CMD ["python", "./src/CalculatorTests.py"]