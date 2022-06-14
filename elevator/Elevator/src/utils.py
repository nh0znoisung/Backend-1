from distutils.util import check_environ
from enum import Enum
from dataclasses import dataclass
import time
from collections import deque
from src.checker import Checker
# import asyncio
# from typing import List, Set, Tuple, Dict, Union, Optional
# import threading
from decouple import config

class Request:
    is_done: bool
    def __init__(self):
        self.is_done = False

    def __del__(self):
        self.is_done = False


class Floor:
    requests: list
    floor_number: int
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.requests = []
    
    def __del__(self):
        self.floor_number = -1 # Excetion number
        self.requests = []
    
    def ping(self): # Ping to Elevator
        # Only 1 elevator is global
        elevator.requests.append(self.floor_number)

    def add_request(self, request: Request):
        if len(self.requests) == 0:
            self.ping()
        self.requests.append(request)
    
    def release_request(self):
        for request in self.requests:
            request.is_done = True
        self.requests = [] # Need mutex lock


class Elevator:
    requests: deque
    curr_floor: int
    target_floor: int
    is_running: bool
    is_stopped: bool

    def __init__(self):
        self.requests = deque()
        self.curr_floor = 0
        self.target_floor = 0
        self.is_running = False
        self.is_stopped = False


    def move(self):
        # Move from curr_floor to target_floor
        print("The elevator is moving to floor {}".format(self.target_floor))
        up = True if self.target_floor > self.curr_floor else False
        while self.curr_floor != self.target_floor:
            print("The elevator is on floor {}".format(self.curr_floor))
            tic = time.time()
            while True:
                toc = time.time()
                if toc - tic > DELAY_TIME:
                    break
            # Go up or down
            if up:
                self.curr_floor += 1
            else:
                self.curr_floor -= 1

    def stop(self):
        self.is_stopped = True

    def run(self):
        if self.is_running:
            return
        self.is_running = True
        self.is_stopped = False
        while True:
            if self.is_stopped:
                break
            if len(self.requests) == 0:
                continue

            # Get request
            self.target_floor = self.requests[0]

            # Move
            self.move()
            # print("Done move")

            # Come and release the request in floor
            LIST_FLOOR[self.requests[0]].release_request()
            self.requests.popleft()


DELAY_TIME = 1.5
FLOOR_NUMS = Checker.get_environment("NUMS_FLOOR") # 0-9
Checker.check_environment(FLOOR_NUMS)
LIST_FLOOR = [Floor(i) for i in range(FLOOR_NUMS)]
elevator = Elevator()
# lock = threading.Lock()
