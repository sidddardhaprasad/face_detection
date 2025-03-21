import cv2

# Load the Haarcascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# ----------- Face Detection in an Image -----------
def detect_faces_in_image(image_path):
    # Read the image
    img = cv2.imread(image_path, 1)  # 1 = Load in color

    # Convert image to grayscale (better detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw a rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(img, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Resize image for better display
    resized = cv2.resize(img, (500, 500))

    # Show the image with detected face
    cv2.imshow("Face Detection", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function (use any image path)
detect_faces_in_image("image.jpg")

# ----------- Webcam Test -----------
def test_webcam():
    cap = cv2.VideoCapture(0)  # Open webcam (0 = Default webcam)

    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    while True:
        ret, frame = cap.read()  # Read frame
        frame = cv2.flip(frame, 1)  # Flip frame horizontally

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        cv2.imshow('Color Video', frame)  # Show color frame
        cv2.imshow('Grayscale Video', gray)  # Show grayscale frame

        if cv2.waitKey(30) & 0xFF == 27:  # Press 'ESC' to exit
            break

    cap.release()  # Release webcam
    cv2.destroyAllWindows()  # Close all windows

# Call the function to test webcam
# test_webcam()

# ----------- Real-Time Face Detection -----------
def real_time_face_detection():
    cap = cv2.VideoCapture(0)  # Open webcam

    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    while True:
        ret, img = cap.read()  # Read frame
        img = cv2.flip(img, 1)  # Flip horizontally
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

        # Draw a rectangle around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Show the frame with face detection
        cv2.imshow('Real-Time Face Detection', img)

        if cv2.waitKey(30) & 0xFF == 27:  # Press 'ESC' to quit
            break

    cap.release()  # Release webcam
    cv2.destroyAllWindows()  # Close all windows

# Call the function to detect faces in real-time
real_time_face_detection() 