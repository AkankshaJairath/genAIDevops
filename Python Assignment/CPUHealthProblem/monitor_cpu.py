import psutil
import time
import sys

def monitor_cpu(threshold):
    try:
        while True:            
            # Get the current CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            #else:
            #    print(f"CPU usage is at {cpu_usage}%")
            time.sleep(1)  # Wait for 1 second before the next check
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by the user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    threshold = 80  # Set the CPU usage threshold
    print(f"Monitoring CPU usage...")
    monitor_cpu(threshold)

if __name__ == '__main__':
    main()
