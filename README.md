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

### Python Libraries

Ensure you have the following Python libraries installed:

- `numpy`
- `openvr`
- `transforms3d`

Install them using pip:

```bash
pip install numpy openvr transforms3d

