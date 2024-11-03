Overview
Unknown-Face-Alert-System is a facial recognition project designed to detect faces that are not present in a pre-defined dataset of known individuals. When an unknown face is detected, the system automatically sends an alert notification to a specified Telegram chat, helping users stay informed about any unfamiliar person appearing in their monitored area.

Features
Face Recognition: Uses a dataset of known faces to recognize familiar individuals.
Unknown Face Detection: Identifies any unrecognized face in the video feed or images.
Telegram Notifications: Sends real-time alerts to a Telegram chat, including an image of the detected unknown face.
Modular Codebase: Easily customizable for different datasets and notification options.

Requirements:
Python 3.x
face_recognition
OpenCV
Telegram Bot API

Setup Instructions:
1. Clone the Repository
git clone https://github.com/your-username/Unknown-Face-Alert-System.git
cd Unknown-Face-Alert-System

2. Install Dependencies
Install the required Python libraries using pip:
pip install face_recognition opencv-python requests

3. Prepare Known Faces Dataset:
Create a directory called known_faces.
Place images of known individuals inside this folder. Each image should be labeled with the name of the person (e.g., john_doe.jpg).

4. Set Up Telegram Bot:
Go to Telegram and create a new bot using BotFather.
Copy the Bot Token you receive.
Find your Telegram chat ID, which you can do by starting a conversation with your bot and using an API to retrieve the ID.

5. Configure Environment Variables
Create a .env file in the project directory with the following content:
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

6. Run the System:
You can start the face detection and alert system by running:
python main.py
The program will start accessing your webcam or video feed, detect faces, and send a Telegram notification if an unknown face is detected.

How It Works:
The system captures frames from the video feed or webcam.
Each face in the frame is compared against the known_faces dataset.
If a face is not recognized (i.e., it does not match any face in the dataset), a screenshot is taken.
The system then sends this screenshot to the specified Telegram chat via the Telegram Bot API.
Example Screenshot of Alert
![b8a06bc2-9d03-407a-a793-df94611823d8](https://github.com/user-attachments/assets/87bb4012-9656-4661-8db7-d304a5d1d251)


Future Enhancements
Add support for additional notification channels (e.g., email, SMS).
Implement logging for detected faces and alert history.
Optimize face matching with large datasets.
