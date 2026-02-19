from cloud_functions import BaseCloudFunction
from compute import ComputeFunction
from monitoring_system import CloudMonitor

my_monitor = CloudMonitor()

first_list = [{"Name": "Fs_Server", "Memory": 1400,"Time": 5000},
    {"Name": "FC_Server", "Memory": 20000, "Time": 5000}, 
    {"Name": "TC_Server", "Memory": -100, "Time": 5000},  
    {"Name": "Web_Server", "Memory": 512, "Time": 10000}]


for my_list in first_list:

    base_name = my_list["Name"]
    base_memory = my_list["Memory"]
    base_time = my_list["Time"]
    print(f"\nProcessing order: {base_name} ({base_memory}MB)...")
    try:
        server1 = ComputeFunction(base_name,base_memory,base_time)
        my_monitor.add_function(server1)
        print("Success! Added to the system")
    except ValueError as e:
        print(f"Error: Server cannot be created{e}")

    print("\n---- Final REPORT-----")
    my_monitor.generate_report()

    