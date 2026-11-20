# Network Ping Monitor

Lightweight Python code made to retrieve ip addresses and see if they're available or not.



## What this Project Does

Created this script in order to make the process of pinging servers, routers and other machines more efficient. With this script you can automate ICMP availability with simple output for the user.



## How it Works

* Reads a list of websites and IP addresses from the `ips.txt` file.* Utilizes built in `os` module to send pings to each target.


* Utilizes built in `os` module to send pings to each target.


* Reviews responses and prints `[UP]` if there's a connection or `[DOWN]` if it fails.


## How to Use

1. Make sure Python3 is installed on your pc
2. Add the websites or IP addresses you want to test into `ips.txt` with one per line.
3. Run script in your terminal with `python ping_monitor.py` . 