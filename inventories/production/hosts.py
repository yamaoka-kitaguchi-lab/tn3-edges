#!/usr/bin/env python3
from datetime import datetime
import os
import json

HOSTS_PATH = os.path.join(os.path.dirname(__file__), "edges")


def main():
  targets = {}
  with open(HOSTS_PATH) as fd:
    for line in fd.read().splitlines():
      if not line or line[0] == "#":
        continue
      host, ip = line.split()
      targets[host] = ip

  n = datetime.now()
  ts = n.strftime("%Y-%m-%d@%H-%M-%S")
  
  print(json.dumps({
    hostname: {
      "hosts": [ip],
      "vars": {
        "hostname": hostname,
        "datetime": ts,
      }
    }
    for hostname, ip in targets.items()
  }))


if __name__ == "__main__":
  main()
