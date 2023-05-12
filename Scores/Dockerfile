FROM python:3.8

WORKDIR /app


RUN pip install flask


COPY MainScores.py .
COPY /Utils.py .
COPY Scores/Scores.txt .
COPY Scores.txt /app

EXPOSE 6000

CMD ["python", "MainScores.py"]
