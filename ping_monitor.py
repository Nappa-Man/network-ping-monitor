import os


with open('ips.txt', 'r') as file:
    targets = [line.strip() for line in file]


print('--Starting Network Pink Check--')


for ip in targets:
    response = os.system(f'ping -n 1 {ip} > nul')
    if response == 0:
        print(f'[UP]  {ip} is reachable. ')
    else:
        print(f'[DOWN] {ip} is NOT responding!!')  