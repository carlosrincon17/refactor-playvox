# This file was created to have a central access point to read the variables that the application needs 
# to work. Those vare should be readed from a .env file, python evironment or ofr example SSM parameters
# from amazon. If the decision is to use a env file, it should not be added to repo.


class AWSConfig:

    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    REGION_NAME = ""

class MysqlDatabaseConfig:

    USER = ""
    PASSWORD = ""
    HOST = ""
    PORT = ""
    DATABASE = ""