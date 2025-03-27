
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as fd:
    data = json.load(fd)

print("[")
first = True
for case, caseData in data.items():
    for step, stepData in caseData.items():
        if step not in ("verilate", "execute"):
            continue
        for metric, samples in stepData.items():
            if metric not in ("elapsed", "memory"):
                continue
            if not first:
                print(",")
            first = False
            print("  {")
            print(f'    "name": "{case} - {step} - {metric}",')
            print(f'    "unit": "{"s" if metric == "elapsed" else "MB"}",')
            print(f'    "value": "{samples[0]}"')
            print("  }")

print("]")

