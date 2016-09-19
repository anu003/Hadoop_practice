import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, clientId, userName, time, timeZone, _, requestLine, _, statusCode, objectSize = data
        if len(requestLine.strip()) > 2:
            print requestLine.replace('http//www.the-associates.co.uk','')
