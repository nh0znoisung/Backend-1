# from utils import *
import os

class Checker:
    # floor_number. Fastapi make sure it is Int
    # upper_bound. Make sure int > 0
    @staticmethod
    def check_floor(floor_number: int, upper_bound: int):
        if floor_number < 0:
            raise Exception("The floor number can not be negative")
        elif floor_number >= upper_bound:
            raise Exception("The floor number is out of range")

    @staticmethod
    def get_environment(field_name: str = 'NUMS_FLOOR'):
        if not os.path.exists("./.env"):
            raise Exception("The environment file is not found")
        
        # UndefinedValueError
        env = os.getenv('NUMS_FLOOR')
        env = int(env) # int checker
        return env

        
    @staticmethod
    def check_environment(var: int):
        if var <= 0:
            raise Exception("The number of floors can not be negative")
