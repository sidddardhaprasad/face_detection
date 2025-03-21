# face_detection
# Face Detection Using OpenCV

## 📌 Project Overview
This project implements face detection using OpenCV and Haar cascade classifiers. It provides functionalities for:
- Detecting faces in an image
- Capturing real-time video from the webcam
- Performing live face detection with bounding boxes

## 📸 Features
- Face detection from static images
- Real-time face detection via webcam
- Grayscale and color video preview
- Simple and efficient implementation using OpenCV

## 🛠️ Technologies Used
- Python
- OpenCV
- Haar Cascade Classifier

## 🚀 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/siddardhaprasad/face-detection-opencv.git
   ```
2. Navigate to the project directory:
   ```sh
   cd face-detection-opencv
   ```
3. Install dependencies:
   ```sh
   pip install opencv-python
   ```
4. Download the Haar Cascade file:
   - Get `haarcascade_frontalface_default.xml` from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project folder.

## 🏃 Usage
### 1. Face Detection from an Image
Run the following command:
```sh
python face.py
```
Make sure to replace `'Bean.webp'` in the script with your image file.

### 2. Real-Time Face Detection via Webcam
Uncomment the relevant section in `face.py` and execute:
```sh
python face.py
```
Press `ESC` to exit the webcam feed.

## 🛠️ Project Structure
```
face-detection-opencv/
│-- haarcascade_frontalface_default.xml
│-- face.py
│-- Bean.webp (sample image)
│-- README.md
```

## ⚠️ Troubleshooting
- If the webcam is not detected, change `cv2.VideoCapture(0)` to `cv2.VideoCapture(0, cv2.CAP_DSHOW)`.
- Ensure OpenCV is installed (`pip install opencv-python`).
- Verify that the `haarcascade_frontalface_default.xml` file is in the project directory.

## 📜 License
This project is open-source and available under the MIT License.

## 🤝 Contributing
Feel free to fork the repo, make improvements, and submit a pull request! 🎉

## 📬 Contact
For any issues or suggestions, reach out via GitHub Issues or connect on LinkedIn.

Happy Coding! 🚀

