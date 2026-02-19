
class CloudMonitor:
    def __init__(self):

        self.active_functions = []

    def add_function(self,function):
        self.active_functions.append(function)

    def generate_report(self):
        print(f"Report: {len(self.active_functions)} active functions")

        total_cost = 0.0

        for function in self.active_functions:
            
            cost = function.calculate_cost()

            total_cost += cost

        print("-----------------------------------------")
        print(f"Total monthly costs: {total_cost} $")