# This is a repository for Workshop 2.1

The code works with the Steam VR app, converts the HTC Vive tracker poses to quaternians, and publishes them to an IP adress.

# OpenVR Device Tracker

This Python script interfaces with an OpenVR setup to fetch real-time positional and orientation data from specified VR devices (e.g., base stations and trackers) and sends this data to a specified socket using UDP in JSON format.

---

## Features

- Tracks devices based on their serial numbers.
- Retrieves both position (as coordinates) and orientation (as a quaternion) of devices.
- Sends tracking data as JSON over UDP to a specified socket address.
- Designed to run continuously and provide real-time updates.

---

## Requirements

### Software Requirements
- **Anaconda**: To manage dependencies and create a Python environment.
- **Python Version**: 3.8.20 (configured through Anaconda).

---

## Setup

### 1. Install Anaconda

If you don’t already have Anaconda installed, download and install it from [Anaconda’s official website](https://www.anaconda.com/).

---

### 2. Create the Python Environment

1. Open your terminal or Anaconda Prompt.
2. Create a new environment named `openvr-env` with Python 3.8.20:
   ```bash
   conda create -n openvr-env python=3.8.20
