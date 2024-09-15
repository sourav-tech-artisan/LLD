# generally implemented by private constructor and a public method
# metaclasses define the behavior of classes 

from typing import Any
import threading


class Singleton:
    _instance: Any = None
    _lock: threading.Lock = threading.Lock() # prevents race condition

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)

        return cls._instance
    
    def __init__(self):
        pass


