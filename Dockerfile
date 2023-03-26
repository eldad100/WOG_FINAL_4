FROM python:3.6-alpine

WORKDIR /app

RUN pip install flask
RUN pip install selenium

COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt /app

EXPOSE 5555

CMD ["python", "MainScores.py"]
