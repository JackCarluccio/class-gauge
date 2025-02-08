# ClassGauge: Enhancing Classroom Engagement with AI

ClassGauge is an innovative tool designed to track and analyze student participation in class using a combination of cutting-edge technologies. By leveraging computer vision, speech-to-text transcription, and Large Language Models (LLMs), ClassGauge provides instructors with valuable insights into student engagement, fostering a more interactive and inclusive learning environment.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Team](#team)

## Introduction

ClassGauge addresses the challenge of accurately and objectively measuring student participation in classroom settings. Traditional methods often rely on subjective assessments, which can be biased or inaccurate. ClassGauge automates this process by using computer vision to identify students, speech-to-text to transcribe their contributions, and LLMs to analyze the quality and relevance of their participation. This comprehensive approach provides instructors with a holistic view of student engagement, enabling them to tailor their teaching strategies and provide personalized support.

## Features

* **Real-time Student Detection:** Utilizes YOLO and OpenCV for accurate and efficient detection of students in the classroom.
* **Speaker Identification:** Employs computer vision techniques to identify the active speaker.
* **Speech-to-Text Transcription:** Integrates VOSK for high-quality, real-time transcription of student contributions.
* **Participation Analysis:** Leverages Google Gemini to analyze the transcribed text, assessing the relevance, depth, and quality of student participation.
* **Data Visualization:** (Future Implementation) Presents participation data in a user-friendly dashboard, providing instructors with actionable insights.
* **OpenVINO Optimization:** Uses OpenVINO for optimized performance of computer vision models on Intel hardware.
* **Flask Web Interface:** Provides a user-friendly web interface for accessing and managing ClassGauge.

## Technologies Used

* **Computer Vision:** OpenCV, YOLO, OpenVINO
* **Speech-to-Text:** VOSK
* **Large Language Model:** Google Gemini
* **Backend:** Flask (Python)
* **Core Language:** C++

## Installation

Detailed installation instructions will be provided soon.  This will include:

1. Setting up the development environment (including Python, C++, and necessary libraries).
2. Installing the required dependencies (OpenCV, VOSK, Flask, etc.).
3. Obtaining API keys for Google Gemini.
4. Building the C++ components.
5. Running the Flask web application.

### Vision and backend on `dev` branch

## Usage

1. Start the Flask web application.
2. Connect your camera (future applications may use multiple cameras)
3. Calibrate the system for the classroom environment.
4. Begin class. ClassGauge will automatically detect students, transcribe their contributions, and analyze their participation.
5. Access the participation data through the web interface.

## License

This project is currently unlicensed.

## Team

* Jack Carluccio
* Rafayel Amirkhanyan
* Anthony Cardello
