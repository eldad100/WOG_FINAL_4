FROM python:3.6

WORKDIR /app

RUN apk add --update --no-cache chromium chromium-chromedriver
RUN pip install flask \
    && pip install selenium

COPY MainScores.py .
COPY Utils.py .
COPY Scores.txt /app

EXPOSE 5555

CMD ["python", "MainScores.py"]
