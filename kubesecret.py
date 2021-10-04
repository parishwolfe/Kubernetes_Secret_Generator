import argparse
import sys
import base64
import csv

parser = argparse.ArgumentParser(description='Kubernetes secrets yaml maker')
parser.add_argument('-n', '--name', help='Name of the secret', required=True)
parser.add_argument('-s', '--namespace', help='Namespace of the secret', required=False)
parser.add_argument('-c', '--csv', help='csv of secrets', required=True)

options = parser.parse_args()
output = f"""apiVersion: v1
kind: Secret
metadata:
    name: {options.name}\n"""
if options.namespace:
    output += f"""    namespace: {options.namespace}\n"""
output += """type: Opaque
data:
"""
try:
    with open(options.csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            output += f"""  {row['key']}: {base64.b64encode(row['value'].encode()).decode()}\n"""
except FileNotFoundError:
    print(f"File {options.csv} not found")
    sys.exit(1)

print(output)
