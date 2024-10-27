# Camera Feed Object Detection with Google Generative AI Descriptions
This project leverages Google Generative AI's Gemini model to provide real-time descriptions of objects and scenes captured by a camera. Each captured frame generates a brief text description, which is displayed on the screen and optionally spoken aloud for hands-free user experience.

## Features
1. Real-Time Video Capture: Streams live video from your camera in a real-time feed.
2. AI-Based Description: Uses Google Generative AI to describe each frame with accurate, context-sensitive text.
3. On-Screen Text: Display the generated description on each frame.
4. Text-to-Speech (Optional): Automatically reads out descriptions, enhancing accessibility.
   
## Demo



## Installation
Clone the Repository:
bash
```
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

Install Required Packages:
Install Python and set up a virtual environment (optional).

Install the required libraries:
bash
```
pip install opencv-python pillow google-generativeai pyttsx3
```

Set Up Google Generative AI API:
Sign up for Google Generative AI and obtain your API key.

Set your API key as an environment variable:
bash
```
export API_KEY="your_api_key_here"  # For Linux/macOS
setx API_KEY "your_api_key_here"     # For Windows
```

Verify ffmpeg Installation (Optional):
For the text-to-speech feature to function, ffmpeg must be installed and accessible in your PATH.

## Usage
Run the main script to start the camera feed and AI description:
bash
```
python main.py
```

## Controls
Press 'Q': Quit the application at any time.
Toggle Text-to-Speech: Modify the code to enable or disable TTS based on your preferences.

## Code Explanation
The primary workflow includes:

1. Capturing Camera Frames: Using OpenCV, the program captures frames in real-time.
2. Sending Frames to Generative AI: Each frame is processed and sent to Google Generative AI for description.
3. Displaying and Speaking the Description: The description is shown on the screen and optionally read aloud.

## Troubleshooting
1. API Key Not Recognized: Ensure your API key is set correctly as an environment variable.
2. Lag in Camera Feed: Reduce the frame size for better performance on low-spec devices.
3. Text-to-Speech Errors: Ensure ffmpeg is installed and accessible via PATH.

## Help Improve the Project
1. Credit Limitations:
The free credits for Google Gemini’s API can run out quickly, leading to service interruptions. Consider setting up an alternative API or optimizing the frequency of API calls by skipping frames.

2. Real-Time Feed Optimization:
The current setup may feel choppy, as each frame requires a network call to the API. Potential improvements include:
-> Reducing the frame size before sending to the API.
-> Sending every alternate frame instead of every single frame.
-> Adding a queue to process frames more asynchronously.

## Contributing
Feel free to fork the project and make improvements or open issues for bugs and feature suggestions.

