#import standard python socket library
#import datetime for date & time
import socket
import datetime

#using socket to find host & ports
def scanPort(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True
#create new file then write to it


scanFile = open("ScanResult", "w")
host = input("Enter IP address to scan: ")
start = datetime.datetime.now()
#date & time right after asking to scan
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    HostIpAddress = socket.gethostbyname(host)
    print("You're IP Address is valid" + "\n")
#create exception handling
except:
    print("You're IP Address is invalid")
    exit()
try:
    # Port 4, an empty one
    s.connect((host, 4))
    print("Host is not from this planet.")
except socket.error as e:
    result = str(e)
# print results
s.close()
# f in print to show {}
if result.startswith("[WinError 10061]"):
    print(f"Host is responding. Proceeding with scan at {start} \n")
    scanFile.write(f"{host} is responding. Scan beginning at {start}\n")
else:
    print("Host seems to be offline or unreachable. Aborting scan")
    scanFile.write(f"host {host} is not responding. Scan aborted")
    scanFile.close()
    exit()
for x in range(50, 1025):     #use 1, 1025 , 50 is shorter for testing
    if scanPort(host, x):
        print("port ", x, " is open", "\n")
        scanFile.write(f"Port {x} is open \n")
print("Scan completed.")
end = datetime.datetime.now()
print("Scan completed at: ", end)
print("Total scan time:", start)
scanFile.write(f"Scan completed at {end} \n")
scanFile.write(f"Total scan time {end - start} seconds")
scanFile.close()
