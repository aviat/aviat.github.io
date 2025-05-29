import json
import sys

port = json.load(open(sys.argv[1]))
urls = json.load(open(sys.argv[2]))

idx = 0
for item in port:

    item["url"] = urls[idx]
    item.pop("Source Link")
    idx += 1

res=json.dumps(port, indent=4)
print(res)
