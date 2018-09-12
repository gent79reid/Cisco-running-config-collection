#!/usr/bin/evn 

from netmiko import ConnectHandler
from device_list import all_devices
import threading
from datetime import datetime


def show_running(a_device):
    remote_conn = ConnectHandler(**a_device)
    result = remote_conn.send_command("show running")
    remote_conn.disconnect()
    target_file = open(a_device['ip']+".txt", "w")
    target_file.write(result)
    target_file.close()


def main():
    start_time = datetime.now()
    for a_device in all_devices:
        my_thread = threading.Thread(target=show_running,args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()
    
    print("\nElapsed time: " + str(datetime.now() - start_time))
    exit()

if __name__ == "__main__":
    main()
