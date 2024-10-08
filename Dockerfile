FROM python:3.10
LABEL authors="Wikoria Dębowska"

WORKDIR /app/NLPToolkit

COPY requirements.txt /app/NLPToolkit
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/NLPToolkit

CMD [ "python3", "-m", "unittest", "discover", "-s", "test", "-p", "\"test_*.py\"" ]
