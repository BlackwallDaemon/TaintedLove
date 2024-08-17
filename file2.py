# file2.py
from file1 import tainted_input

def process_data():
    data = tainted_input()
    print(f"Processing: {data}")
    execute_command(data)

def execute_command(command):
    # Potentially dangerous execution based on input from file1
    exec(command)
