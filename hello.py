#!/usr/bin/env python3

import os, json

print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=4))
