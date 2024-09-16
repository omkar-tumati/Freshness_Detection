import base64
from PIL import Image
import requests

# Convert image to base64
def convert_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Send the image and prompt to Gemini API
def send_request_to_gemini(image_base64, prompt):
    url = "https://gemini-api-endpoint"  # Replace with actual Gemini API endpoint
    headers = {
        "Authorization": "AIzaSyBsaIoUvd6GWDkD2uK57-5NfKbOFYcrofo",  # Replace with your Gemini API key
        "Content-Type": "application/json"
    }

    data = {
        "image": image_base64,
        "prompt": prompt
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        if "answer" in result:
            return result
        else:
            return {}
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return {}

# Main function to classify image and get the result
def classify_image(image_path, prompt):
    # Convert image to base64
    image_base64 = convert_image_to_base64(image_path)
    
    # Send the image and prompt to Gemini API
    result = send_request_to_gemini(image_base64, prompt)
    
    # Return the result or an empty JSON if the answer is uncertain
    return result

# Test the function with an image and prompt
image_path = "path_to_your_image.jpg"  # Replace with the path to your image
prompt = "Identify the fruit or vegetable"  # You can change this prompt

result = classify_image(image_path, prompt)
print(result)
