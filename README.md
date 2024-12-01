# Traffic Sign Classification using Deep Learning

## **Problem Statement**
Traffic sign recognition is a critical task in autonomous driving systems and traffic monitoring. The ability to identify traffic signs like "Stop," "Yield," and "Proceed" ensures safer navigation for vehicles and pedestrians. Misclassification or an inability to identify traffic signs can lead to accidents or violations of traffic laws. Our goal was to develop a robust deep learning model capable of accurately classifying traffic signs into predefined categories.

---

## **Proposed Solution**
We developed a traffic sign classification system using a Convolutional Neural Network (CNN) to automatically recognize and classify traffic signs. The system was trained on a labeled dataset of traffic sign images to classify them into four categories: **Stop, Proceed, Yield, and Extra**. The model is deployed as a Flask API, making it accessible for real-world applications via web or mobile interfaces.

Key features of our solution:
1. **Deep Learning Model**: A CNN architecture trained using TensorFlow/Keras.
2. **Data Augmentation**: Enhanced the dataset by applying transformations like rotations, shifts, and zooms to improve generalization.
3. **API Deployment**: A lightweight Flask application that enables users to upload images and get real-time predictions.
4. **Organized Dataset**: Labeled traffic sign images were preprocessed and split into training and testing datasets for better model performance.

---

## **AI Tools and Frameworks**
1. **YOLOv8 (Ultralytics)**: Used for initial object detection and labeling of traffic signs in images.
2. **TensorFlow/Keras**: Framework used for building and training the CNN model.
3. **Flask**: Lightweight web framework used to deploy the trained model as an API.
4. **Scikit-learn**: Utilized for splitting the dataset into training and testing sets.
5. **OpenCV**: Used for image preprocessing and visualization tasks.
6. **Matplotlib**: For plotting annotated images and visualizing results.

---

## **Model Architecture**
We designed a simple CNN with the following layers:
1. **Input Layer**: Accepts 64x64 RGB images.
2. **Convolutional Layers**: Extract features using 32 and 64 filters with ReLU activation.
3. **MaxPooling Layers**: Reduces spatial dimensions while retaining important features.
4. **Fully Connected Layers**: Processes extracted features for classification.
5. **Output Layer**: Uses a softmax activation function to classify images into 4 categories.

---

## **Results and Impact**
- **Model Accuracy**: Achieved a classification accuracy of over **90%** on the test dataset.
- **Real-time Predictions**: The Flask API provides quick and accurate predictions for uploaded images.
- **Dataset Organization**: Proper labeling and augmentation improved model generalization.
- **Practical Application**: The system can be integrated into autonomous driving software, traffic monitoring systems, or educational tools for driver training.

---

## **Future Scope**
1. **Dataset Expansion**: Increase the number of classes to include more traffic signs and enhance the diversity of images.
2. **Model Optimization**: Implement transfer learning using pre-trained models like MobileNet or ResNet for better accuracy and faster training.
3. **Edge Deployment**: Deploy the model on edge devices such as Raspberry Pi or Nvidia Jetson for on-the-go traffic sign detection.
4. **Real-time Video Processing**: Extend the model to process real-time video streams for dynamic traffic environments.
5. **Multilingual Traffic Signs**: Adapt the system to recognize text-based or regional traffic signs from different countries.

---

## **How to Use**
### **Requirements**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/traffic-sign-classification.git
