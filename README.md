
# Gesture-Controlled Drone

This project enables drone control through hand gestures using computer vision techniques. The system integrates hand detection via MediaPipe, simulation with Mission Planner, and socket communication with a Raspberry Pi.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Model Training](#data-model-training)
3. [Hand Detection with MediaPipe](#hand-detection-with-mediapipe)
4. [Simulation with Mission Planner](#simulation-with-mission-planner)
5. [Socket Connection with Raspberry Pi](#socket-connection-with-raspberry-pi)
6. [Special Note on Socket Connections in `app.py`](#special-note-on-socket-connections-in-app-py)
7. [References](#references)

## Introduction

The Gesture-Controlled Drone project leverages computer vision to interpret hand gestures, allowing for intuitive drone navigation. By utilizing MediaPipe for hand detection and Mission Planner for simulation, the system offers a comprehensive approach to gesture-based drone control.

## Data Model Training

Training a robust model is crucial for accurate gesture recognition. The process involves:

### Data Collection
Capturing diverse hand gesture images under varying conditions to ensure model robustness.

### Preprocessing
Normalizing images, augmenting data, and labeling gestures appropriately.

### Model Training
Utilizing machine learning frameworks to train the model on the preprocessed dataset.

### Evaluation
Assessing model performance using validation datasets and refining as necessary.

For a practical guide on creating a gesture-controlled drone, refer to this tutorial: [Make Your Drone Gesture Controlled](https://example.com)

## Hand Detection with MediaPipe

MediaPipe is a cross-platform framework by Google that offers customizable ML solutions. In this project, MediaPipe's Hand module is employed to detect and track hand landmarks in real-time, facilitating gesture recognition.

### Key Steps

- **Integration**: Incorporating MediaPipe's Hand module into the application.
- **Detection**: Real-time identification of hand landmarks.
- **Gesture Mapping**: Translating detected hand positions into corresponding drone commands.

For more details on controlling drones via gestures using MediaPipe Hands, see this article: [Drone control via gestures using MediaPipe Hands](https://example.com)

## Simulation with Mission Planner

Mission Planner is a ground control station software for planning and simulating drone missions. It allows users to create and test flight plans in a virtual environment before deploying them in real-world scenarios.

### Steps to Utilize Mission Planner for Simulation

1. **Installation**
   Download and install Mission Planner from the [official website](https://ardupilot.org/planner/docs/mission-planner-overview.html).

2. **Configuration**
   Set up the software with the appropriate vehicle type and parameters.

3. **Simulation**
   Use the Simulation tab to test flight plans and drone responses to gesture inputs.

For a beginner's tutorial on using Mission Planner for simulation, watch this video: [Beginner's Tutorial - Simulation using Mission Planner](https://example.com)

## Socket Connection with Raspberry Pi

Establishing a socket connection between the application and a Raspberry Pi enables real-time command transmission to the drone. This setup involves:

### Socket Programming
Implementing socket communication protocols in Python.

### Server Setup
Configuring the Raspberry Pi to receive and execute commands.

### Testing
Ensuring reliable data transmission between the application and the Raspberry Pi.

For a comprehensive guide on setting up socket communication, refer to this resource: [Socket Programming](https://www.youtube.com/watch?v=79dlpK03t30)
Using the requirements.txt File

##To ensure that all dependencies for the project are installed, use the requirements.txt file provided. Follow these steps:

Install Python: Ensure that Python is installed on your system. You can download it from python.org.

Install pip: Pip, the Python package installer, should be included with Python. Verify by running:

###pip --version

Install Dependencies:
Navigate to the project directory containing the requirements.txt file and run the following command:

###pip install -r requirements.txt

This will install all necessary packages, including ConfigArgParse, djitellopy, numpy, opencv-python, tensorflow, and mediapipe.

## Special Note on Socket Connections in `app.py`

In the `app.py` file, certain socket connection lines are commented out. These lines should only be uncommented after successfully establishing a connection with the Raspberry Pi to prevent runtime errors or connection issues.

**Important**: Ensure that the Raspberry Pi is properly configured and connected before modifying these lines.

## References

- [Make Your Drone Gesture Controlled](https://example.com)
- [Drone control via gestures using MediaPipe Hands](https://example.com)
- [Mission Planner Simulation - ArduPilot](https://ardupilot.org/planner/docs/mission-planner-overview.html)
- [Socket Programming](https://www.youtube.com/watch?v=79dlpK03t30)

