FROM python:3.6-alpine

WORKDIR /app

RUN pip install flask

COPY MainScores.py .
COPY Utils.py .

COPY Scores.txt .

EXPOSE 5000

CMD ["python", "MainScores.py"]