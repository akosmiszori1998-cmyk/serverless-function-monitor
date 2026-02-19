from cloud_functions import BaseCloudFunction

class StorageFunction(BaseCloudFunction):
    def __init__(self, name, memory_mb,data_processed_gb):
        super().__init__(name,memory_mb)

        self.data_processed_gb = data_processed_gb

    @property
    def data_processed_gb(self):
        return self._data_processed_gb
    
    @data_processed_gb.setter
    def data_processed(self,value):
        if value < 0:
            raise ValueError("The amount cannot go under 0")
        self._data_processed_gb = value

    def calculate_cost(self):
        return self.data_processed_gb * 0.02
        





