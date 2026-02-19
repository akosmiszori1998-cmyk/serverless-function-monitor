from abc import ABC,abstractmethod

class BaseCloudFunction(ABC):
    def __init__(self,name,memory_mb):
        self.name = name
        self.memory = memory_mb

    @property
    def memory(self):
        return self._memory
    
    @memory.setter
    def memory(self,value):
        if value < 128 or value > 10240:
            raise ValueError("Error: Invalid memory amount")
        self._memory = value

    @abstractmethod
    def calculate_cost(self):
        pass
    
