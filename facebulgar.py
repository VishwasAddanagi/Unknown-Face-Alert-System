import cv2
import numpy as np
import face_recognition
import os
import requests

# Initialize variables
known_encodings = []
known_names = []

# Telegram bot details
bot_token = '{BotToken}'
chat_id = '{Your ChatID}'

# Function to send Telegram message
def send_telegram_notification(message):
    url = f'https://api.telegram.org/bot{botToken}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Notification sent successfully!")
        else:
            print(f"Failed to send notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending notification: {e}")

# Load known faces from a directory
def load_known_faces():
    global known_encodings, known_names
    for filename in os.listdir('known_faces'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join('known_faces', filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
            else:
                print(f"No face encodings found in {filename}")

# Load known faces at the start
load_known_faces()

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Camera not accessible.")
    exit()

while True:
    ret, frame = video_capture.read()
    
    if not ret:
        print("Failed to capture video")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face detected
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_names[best_match_index]

        # Draw bounding boxes
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)  # Green for known, red for unknown
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)

        # Send notification for unknown face
        if name == "Unknown":
            send_telegram_notification("Unknown face detected!")

    # Display the video
    cv2.imshow('Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
