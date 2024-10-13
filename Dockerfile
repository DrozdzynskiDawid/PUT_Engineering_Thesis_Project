FROM python:3.10
LABEL authors="Wikoria Dębowska"

WORKDIR /app/LLMToolkit

COPY requirements.txt /app/LLMToolkit
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/LLMToolkit

RUN python3 -m nltk.downloader punkt
CMD ["python3", "-m", "unittest", "discover", "-s", "test", "-p", "test_*.py"]
