import PIL.ImageShow
import google.generativeai as genai
import os
import os
import cv2
import PIL.Image
from PIL import Image
import io


genai.configure(api_key=os.environ["API_KEY"])
#$env:API_KEY="your api"

import PIL.Image

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:

        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = PIL.Image.fromarray(frame_rgb)

        small_frame = cv2.resize(frame, (640, 480))
        frame_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        pil_image = PIL.Image.fromarray(frame_rgb)

    
        buffer = io.BytesIO()
        pil_image.save(buffer, format="PNG")
        image_data = buffer.getvalue()
        image_data = Image.open(io.BytesIO(image_data))
        
        prompt = "Describe what's in the image in a line"
        try:
            response = model.generate_content([prompt, image_data])
            description = response.text
            print(description)
        except Exception as e:
            print("Error generating content:", e)
            description = "No description available"

        cv2.putText(frame, description, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
        cv2.imshow("Camera Feed", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()