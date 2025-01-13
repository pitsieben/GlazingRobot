# This is a repository for Workshop 2.1

The code works with the Steam VR app, converts the HTC Vive tracker poses to quaternians, and publishes them to an IP adress.

## OpenVR Device Tracker

This Python script interfaces with an OpenVR setup to fetch real-time positional and orientation data from specified VR devices (e.g., base stations and trackers) and sends this data to a specified socket using UDP in JSON format.

### Features
	•	Tracks devices based on their serial numbers.
	•	Retrieves both position (as coordinates) and orientation (as a quaternion) of devices.
	•	Sends tracking data as JSON over UDP to a specified socket address.
	•	Designed to run continuously and provide real-time updates.

### Requirements

Anconda

Python Libraries

Ensure you have the following Python libraries installed:
	•	numpy
	•	openvr
	•	transforms3d

Install them using pip:

pip install numpy openvr transforms3d

### How It Works
	1.	Initializes the OpenVR system in the background mode.
	2.	Filters tracked devices based on their serial numbers:
	•	Base station serials: "LHB-12CD2DC1", "LHB-803AC526"
	•	Tracker serial: "LHR-D61E634E"
	3.	Captures position and orientation data:
	•	Position: Extracted as [x, y, z] from the tracking matrix.
	•	Orientation: Converted to a quaternion from the rotation matrix using transforms3d.
	4.	Sends the data as a JSON payload via UDP to the specified socket address.

### Usage
	1.	Set the Socket Address:
In the if __name__ == "__main__" block, modify the socket address:

socket_address = ("127.0.0.1", 5000)

Replace "127.0.0.1" and 5000 with the desired IP address and port.

	2.	Run the Script:
Execute the script using Python:

python script_name.py


	3.	Receive the Data:
On the receiving end, listen on the specified socket to capture the JSON payload.

JSON Output Format

The tracking data is sent as a JSON payload with the following structure:

{
  "device_serial": {
    "device_serial": "LHB-12CD2DC1",
    "position": [x, y, z],
    "quaternion": [qw, qx, qy, qz]
  }
}

Example:

{
  "LHB-12CD2DC1": {
    "device_serial": "LHB-12CD2DC1",
    "position": [1.23, 4.56, 7.89],
    "quaternion": [0.707, 0, 0.707, 0]
  }
}

Customization
	•	Add More Devices: Add the serial numbers of additional devices to the base_stations_serials or tracker_serial lists.
	•	Change Data Processing: Modify the way data is processed or formatted before sending it.

Notes
	•	Make sure OpenVR is properly installed and configured.
	•	Ensure the VR devices are powered on and within tracking range.
	•	UDP is a connectionless protocol, so there is no guarantee of delivery. Use TCP if reliability is critical.
