from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(url):
    
    driver = webdriver.Chrome()
    driver.get(url)

    score_element = driver.find_element(By.ID, "score")

    score = int(score_element.text)

    is_valid_score = score >= 1 and score <= 1000

    driver.quit()

    return is_valid_score
def main_function():
    url = "http://localhost:5000"
    is_valid_score = test_scores_service(url)
    if is_valid_score:
        print("The test passed: " + str(is_valid_score))
        sys.exit(0)
    else:
        print('test failed')
        sys.exit(-1)

if __name__ == '__main__':
    main_function()

