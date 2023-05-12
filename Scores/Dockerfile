FROM python:3.5

WORKDIR /app .


RUN pip install flask


COPY MainScores.py .
COPY /Utils.py .
COPY Scores.txt /app

EXPOSE 5001

CMD ["python", "MainScores.py"]
