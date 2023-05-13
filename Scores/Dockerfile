FROM python:3.6

WORKDIR /app


RUN pip install flask \
    && pip install selenium

COPY /Scores/MainScores.py .
COPY Utils.py .
#COPY Scores.txt /app

EXPOSE 5555

CMD ["python", "MainScores.py"]
