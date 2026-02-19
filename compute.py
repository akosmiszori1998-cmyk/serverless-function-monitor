from cloud_functions import BaseCloudFunction

class ComputeFunction(BaseCloudFunction):
    def __init__(self,name,memory_mb,execution_time_ms):
        super().__init__(name,memory_mb)
        self.time_in_ms = execution_time_ms

    def calculate_cost(self):
        return (self.memory * self.time_in_ms) * 0.000016