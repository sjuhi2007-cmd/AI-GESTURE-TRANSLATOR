# AI Gesture Translator

An AI-based project that detects hand gestures and displays the corresponding text using machine learning and computer vision.

## Features
- Hand gesture detection
- Gesture classification using a Random Forest model
- Hand landmark detection using MediaPipe
- Text output for recognised gestures

## Technologies Used
- Python
- MediaPipe
- Scikit-learn
- Jupyter Notebook

## Project Files
- `dataset/` – Dataset used for the project
- `ai ges final.ipynb` – Gesture recognition notebook
- `asl_random_forest.pkl` – Trained Random Forest model
- `hand_landmarker.task` – Hand landmark model
- `final.ipynb` – Additional notebook

## How It Works
1. Detects hand landmarks from visual input.
2. Uses machine learning to classify the gesture.
3. Displays the recognised gesture as text.

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/sjuhi2007-cmd/AI-GESTURE-TRANSLATOR.git
   ```
2. Open `ai ges final.ipynb` in Jupyter Notebook or Google Colab.
3. Install the required libraries and run the notebook cells.

## Future Improvements
- Support more gestures.
- Improve recognition accuracy.
- Add more features for accessible communication.