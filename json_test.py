#!/usr/bin/env python3
import json

with open('words.json', 'r') as f:
    data = json.loads(f.read())
    words = data["data"]

print(words)
