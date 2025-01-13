import numpy as np
import openvr
import transforms3d as t3d
import socket
import json


def get_device_info_and_send(socket_address):
    openvr.init(openvr.VRApplication_Background)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        vr_system = openvr.VRSystem()

        base_stations_serials = ["LHB-12CD2DC1", "LHB-803AC526"]
        tracker_serial = "LHR-D61E634E"

        data = {}

        for device_index in range(openvr.k_unMaxTrackedDeviceCount):
            if not vr_system.isTrackedDeviceConnected(device_index):
                continue

            device_class = vr_system.getTrackedDeviceClass(device_index)
            device_serial = vr_system.getStringTrackedDeviceProperty(
                device_index, openvr.Prop_SerialNumber_String
            )
            device_model = vr_system.getStringTrackedDeviceProperty(
                device_index, openvr.Prop_ModelNumber_String
            )

            if device_serial in base_stations_serials or device_serial == tracker_serial:

                poses = vr_system.getDeviceToAbsoluteTrackingPose(
                    openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount
                )
                pose = poses[device_index]

                if pose.bPoseIsValid:
                    position = pose.mDeviceToAbsoluteTracking

                    position_np = np.array([position[0][3], position[1][3], position[2][3]])
                    rotation_matrix = np.array([position[0][:3], position[1][:3], position[2][:3]])

                    quaternion = t3d.quaternions.mat2quat(rotation_matrix)

                    data[device_serial] = {
                        "device_serial": device_serial,
                        "position": position_np.tolist(),
                        "quaternion": quaternion.tolist(),
                    }

        server_socket.sendto(json.dumps(data).encode(), socket_address)

    finally:
        openvr.shutdown()
        server_socket.close()


if __name__ == "__main__":
    socket_address = ("127.0.0.1", 5000)

    while True:
        get_device_info_and_send(socket_address)
