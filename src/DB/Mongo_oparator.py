import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


load_dotenv()


class MongoOperator:
    def __init__(self, host='localhost', db_name='Curriculo'):
        self.host = host
        self.db_name = db_name

    
    def open_connection(self):
        self.client = pymongo.MongoClient(self.host, server_api=ServerApi('1'))
    
    def close_connection(self):
        self.client.close()


    def check_connection(self):
        try:
            self.open_connection()
            self.client.admin.command('ping')
            self.close_connection()
            return True
        except pymongo.errors.ConnectionFailure:
            return False

    def insert_one(self, collection_name, document):
        self.open_connection()
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.insert_one(document)

    def find_all(self, collection_name):
        try:
            self.open_connection()
            db = self.client[self.db_name]
            collection = db[collection_name]
            results = collection.find({})
            return list(results)
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            self.close_connection()
    
    def find_by_query(self, collection_name, query=None):
        try:
            self.open_connection()
            db = self.client[self.db_name]
            collection = db[collection_name]
            if query is None:
                query = {}
            results = collection.find(query)
            return list(results)
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            self.close_connection()

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        return collection.update_one(query, update)

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def close(self):
        self.client.close()

if __name__ == "__main__":
    mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
    values = [
        {
            "position": "Tech Lead QA",
            "company": "Radix Engineering and Software",
            "startDate": "APRIL 2023",
            "endDate": "Present",
            "descriptions": [
                "Manage the quality assurance team and ensure team productivity and the quality of delivered results;",
                "Establish and implement test automation strategies to ensure efficiency and accuracy of tests;",
                "Coordinate the execution of software tests to identify defects and ensure compliance with product requirements;",
                "Communicate with other team leaders and stakeholders to ensure alignment of testing priorities and project progress;",
                "Automate web-based test cases using Cypress, Protractor, and Puppeteer to improve test coverage and reliability;"
            ],
            "state": "Rio de Janeiro - RJ",
            "lang": "en/Us"
        },
        {
            "position": "Senior Test Analyst",
            "company": "Radix Engineering and Software",
            "startDate": "Nov. 2022",
            "endDate": "Apr. 2023",
            "descriptions": [
                "Providing leadership to the QA team and ensuring productivity and quality standards;",
                "Automating multilingual API test cases using frameworks such as K6 to improve efficiency and accuracy;",
                "Automating web-based test cases using Selenium and programming languages such as Python or NodeJS to ensure compatibility across different browsers and platforms;",
                "Automating web-based test cases using Playwright and programming languages such as Python or NodeJS to improve test efficiency;",
                "Automating web-based test cases using Cypress, Protractor, and Puppeteer to improve test coverage and reliability;"
            ],
            "state": "Rio de Janeiro - RJ",
            "lang": "en/Us"
        },
        {
            "position": "Test Analyst Pl.",
            "company": "Radix Engineering and Software",
            "startDate": "Feb. 2022",
            "endDate": "Nov. 2022",
            "descriptions": [
                "Automating multilingual API test cases using frameworks such as K6 to improve efficiency and accuracy;",
                "Automating web-based test cases using Selenium and programming languages such as Python or NodeJS to ensure compatibility across different browsers and platforms;",
                "Automating web-based test cases using Playwright and programming languages such as Python or NodeJS to improve test efficiency;",
                "Automating web-based test cases using Cypress, Protractor, and Puppeteer to improve test coverage and reliability;"
            ],
            "state": "Rio de Janeiro - RJ",
            "lang": "en/Us"
        },
        {
            "position": "Junior Test Analyst",
            "company": "Radix Engineering and Software",
            "startDate": "Jan. 2020",
            "endDate": "Feb. 2022",
            "descriptions": [
                "Automating multilingual API test cases using frameworks such as K6 to improve efficiency and accuracy;",
                "Automating web-based test cases using Selenium and programming languages such as Python or NodeJS to ensure compatibility across different browsers and platforms;",
                "Automating web-based test cases using Playwright and programming languages such as Python or NodeJS to improve test efficiency;",
                "Automating web-based test cases using Cypress, Protractor, and Puppeteer to improve test coverage and reliability;"
            ],
            "state": "Rio de Janeiro - RJ",
            "lang": "en/Us"
        }
    ]
    for value in values:
        mongo_operator.insert_one('Experiencia', value)
    print(mongo_operator.find_all('Experiencia'))