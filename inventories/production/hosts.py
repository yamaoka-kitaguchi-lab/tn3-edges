#!/usr/bin/env python3
import os
import json

HOSTS_PATH = os.path.join(os.path.dirname(__file__), "edges")


def main():
  target_ips = []
  with open(HOSTS_PATH) as fd:
    for line in fd.read().split("\n"):
      if not line or line[0] == "#":
        continue
      host, ip = line.split()
      target_ips.append(ip)

  print(json.dumps({
    "all": target_ips
  }))


if __name__ == "__main__":
  main()
