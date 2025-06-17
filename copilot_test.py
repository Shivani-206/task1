import os
output = os.popen("uptime -p").read()
print(output)

