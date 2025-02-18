# Live Video Streaming Client

## Overview
This project involves a **Live Video Streaming Client** built with **ReactJS** and a **Python-based server** that provides live video streams. The client communicates with the server over WebSocket to receive real-time video data and display it to the user.

## Features
- **Real-time video streaming**: Watch live video streams with minimal delay.
- **Playback controls**: Pause, resume, and adjust video settings.
- **Responsive design**: Optimized for different screen sizes and devices.
- **Multiple streams support**: Switch between different live video streams.
- **WebSocket communication**: Real-time bidirectional communication between client and server.

## Technologies Used
### Client (ReactJS)
- **ReactJS**: Frontend framework for building the user interface.
- **WebSocket API**: For real-time communication with the server.
- **HTML5**: For rendering the video content.
- **CSS3**: For styling the application.
- **MediaSource Extensions (MSE)**: For dynamically loading and displaying live video streams.

### Server (Python)
- **Python**: Server-side scripting language.
- **Flask**: Lightweight web framework for setting up the server.
- **WebSocket (Flask-SocketIO)**: For handling WebSocket connections to stream live video.
- **FFmpeg**: For encoding and streaming live video content.

## Installation

### Prerequisites
- **Node.js**: For running the React client.
- **Python 3.x**: For running the Flask server.
- **FFmpeg**: For handling video streams (if applicable).

### Steps

....