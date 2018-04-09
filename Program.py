
class Stopwatch:
    import sys
    import time
    # Construct self and start it running.
    def __init__(self):
        self._creationTime = time.time()  # Creation time

    # Return the elapsed time since creation of self, in seconds.
    def elapsedTime(self):
        return time.time() - self._creationTime

if __name__ == "__main__":

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from page.problem import ProblemPage
    from common.consts import consts
    import json
    import urllib
    import requests
    import time

    try:

        url = consts.API_URL
        #url = "http://localhost:64429/api/grader"
        headers = {'content-type': 'application/json'}
        data_path = "data/python.csv"

        index = 0
        with open(data_path, 'r', encoding='utf-8-sig', errors='ignore') as r:
            line = r.readline()
            # while line and index < 1:
            while line:
                if len(line) > 1000:
                    continue

                watch = Stopwatch()

                response = requests.post(
                    url, data=line, headers=headers)
                
                print(index)
                print(watch.elapsedTime())
                print(response.text)
                print(line)

                line = r.readline()
                index += 1
    except Exception as e:
        print(line)
        print('ValueError:', e)
    finally:
        exit
