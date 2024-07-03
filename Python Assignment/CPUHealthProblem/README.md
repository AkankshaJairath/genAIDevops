Problem Statement:

As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:
●       The program should continuously monitor the CPU usage of the local machine.
●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
●       The program should run indefinitely until interrupted.
●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.
  Hint:
●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.
●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

Expected Output:
Monitoring CPU usage...
Alert! CPU usage exceeds threshold: 85%
Alert! CPU usage exceeds threshold: 90%
... (continues until interrupted) 


Explanation:

1.	Importing Libraries:

	psutil: A cross-platform library for retrieving system information, including CPU usage.

2.	Function 

        monitor_cpu(threshold):
	Takes a threshold parameter as input, which specifies the percentage above which an alert will be triggered.
	Uses a while True loop to continuously monitor the CPU usage.
	Inside the loop:

	psutil.cpu_percent(interval=1): Retrieves the current CPU usage as a percentage. The interval=1 parameter specifies that the function waits 1 second      	between successive calls to avoid excessive CPU usage by the monitoring itself.

	If the cpu_usage exceeds the threshold, an alert message is printed.

	time.sleep(1): Sleeps for 1 second before checking again.

3.	Exception Handling:

	try-except block handles KeyboardInterrupt (Ctrl+C from the user) to gracefully stop the monitoring loop and print a message indicating monitoring  	has been stopped.

4.	Main Execution:

	Sets the threshold value (e.g., 80%).
	Calls monitor_cpu(threshold) to start monitoring.

Usage:

•	Adjust the threshold variable to set your desired CPU usage percentage limit.
•	Run the script (python monitor_cpu.py).
•	It will continuously monitor the CPU usage and print alerts whenever the threshold is exceeded.
•	To stop the monitoring, press Ctrl+C.

