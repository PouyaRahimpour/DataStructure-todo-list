from datetime import datetime
from typing import NamedTuple
from enum import Enum


#class Priority(Enum):
(
    HIGH,
    MEDIUM,
    LOW,
) = range(3)

class Task:
    def __init__(self, name: str , priority: int = MEDIUM, due_date: datetime = "", note: str = "", steps: list[str] = [], tags: list[str] = []):
        self.name = name
        self.steps = steps 
        self.tags = tags
        self.priority = priority
        self.due_date = due_date
        self.note = note
        self.created_date = datetime.now()
        self.done = False
        
