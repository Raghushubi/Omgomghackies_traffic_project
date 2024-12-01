import requests 
import os
import sys
import traceback

# Ensure UTF-8 encoding
if sys.version_info[0] >= 3:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

url = "http://127.0.0.1:5000/predict" 
file_path = r"pexels-thanks-394797.jpg" 

try:
    # Verify file exists and is readable
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)

    # Open in binary mode with explicit filename
    with open(file_path, 'rb') as file: 
        files = {'file': (os.path.basename(file_path), file, 'image/jpeg')} 
        response = requests.post(url, files=files) 
    
    print("Response Status Code:", response.status_code)
    print("Full Response Content:", response.text)
    
    # Parse and print JSON
    response_json = response.json()
    print("Response JSON:", response_json)

except Exception as e:
    print(f"Client-side error occurred: {e}")
    print(traceback.format_exc())