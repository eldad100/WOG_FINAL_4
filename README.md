# **World of Games**

Welcome to World of Games, a collection of three simple games written in Python.
In this project, you will find the following file structure:



* #### World-Of-Games/
  * #### |-- Games/
    * |   |-- CurrencyRoulette.py
    * |   |-- GuessGame.py
    * |   |-- MemoryGame.py
  * #### |-- Scores/
    * |   |-- Dockerfile
    * |   |-- MainScores.py
    * |   |-- Score.py
    * |   |-- Scores.txt
    * |   |-- docker-compose.yml
  * #### |-- tests/
    * |   |-- e2e.py
* |-- Live.py
* |-- MainGame.py
* |-- Replay.py
* |-- Utils.py
* |-- Jenkinsfile
***
### ****Games****

The Games folder contains the three games that are part of World of Games. These games are:

1. MemoryGame.py: A memory game where the player has to remember a sequence of numbers and repeat it back.
2. GuessGame.py: A simple number guessing game where the player has to guess a number between 1 and 100.
3. CurrencyRoulette.py: A guessing game where the player needs to guess the value of a random currency exchange rate.


To start playing the games, in your terminal run: 
***
### python3 MainGame.py

This will launch a menu where you can select which game you want to play.
***
### **Scores**

The Scores folder contains the Flask app that handles the game scores.
When a player completes a game, their score is saved in the Scores.txt file.
The Score.py module is responsible for adding the game scores and for storing them in the Scores.txt file.

To view the scores, navigate to the Scores folder in your terminal and run :
python3 MainScores.py 
This will launch a local server where you can view the scores in your browser by accessing it here: http://localhost:5000

Alternatively, you can use Docker to run the Flask app. In this case, navigate to the Scores folder and run the following commands:

docker-compose build
docker-compose up -d
This will start a Docker container that runs the Flask app. You can access the app by going to http://172.20.0.2:5555/ in your browser.

### **Tests**

The tests folder contains the e2e.py module, which is an end-to-end test that uses Selenium to check if the score is between 1 and 1000.
If the score is within that range, the test return code 0. Otherwise, it returns code -1.
You can run the test manually by navigating to the tests folder and running python3 e2e.py in your terminal.
Alternatively, the test is automatically triggered as part of the Jenkins pipeline.
***
### **Jenkins Pipeline**

The Jenkinsfile in the root of the project defines the Jenkins pipeline. The pipeline consists of four stages:

Build: Builds the Docker image for the Flask app.
Run: Starts the Docker container for the Flask app.
Test: Runs the end-to-end test using Selenium.
Finalize: Logs in to the Docker registry using Jenkins credentials, shuts down the Docker container,
and pushes the Docker image to the registry.
You can run the pipeline by creating a Jenkins job and pointing it to the Jenkinsfile in your repository.
The pipeline will automatically build, test, and deploy the Flask app for you.
***
### Project **Requirments**

To install the requirements for this project, please run the following command in your terminal:

**pip install -r requirements.txt**

This will install all the required dependencies, including Flask and Selenium.
Make sure you are in the root directory of the project before running this command.

***

## **We hope you enjoy playing World of Games!**