FROM python:3.10
LABEL authors="Wikoria Dębowska"

WORKDIR /app/NLPToolkit

COPY requirements.txt /app/NLPToolkit
RUN pip install --no-cache-dir -r requirements.txt
#COPY . /app/NLPToolkit

# to see how test run please uncommend line below and commend second CMD and in contaioner do that command: python3 setup.py test
CMD [ "bash" ]
#CMD [ "python3", "setup.py", "test" ]