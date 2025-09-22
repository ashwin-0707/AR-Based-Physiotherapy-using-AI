import mediapipe as mp
import math

# Initialize MediaPipe face module
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to calculate angle between three points
def calculate_angle(point1, point2, point3):
    radians = math.atan2(point3[1] - point2[1], point3[0] - point2[0]) - math.atan2(point1[1] - point2[1], point1[0] - point2[0])
    angle = math.degrees(radians)
    return angle + 360 if angle < 0 else angle

reps = 0

# Function to detect face landmarks and track head movement using yaw angle
def track_head_movement_yaw():
    angle_threshold = 20  # Define the angle threshold for detecting a rep
    prev_yaw_angle = 0
    angle_count = 0

    while True:
        # Assuming the face mesh processing is handled by the frontend and the data is sent here
        
        # Sample data for demonstration
        sample_face_landmarks = {
            "nose": (0.5, 0.5),
            "left_eye": (0.4, 0.4),
            "right_eye": (0.6, 0.4)
        }

        # Extract specific facial landmarks for head movement tracking
        nose_landmark = sample_face_landmarks["nose"]
        left_eye_landmark = sample_face_landmarks["left_eye"]
        right_eye_landmark = sample_face_landmarks["right_eye"]

        # Calculate yaw angle
        dx = right_eye_landmark[0] - left_eye_landmark[0]
        dy = right_eye_landmark[1] - left_eye_landmark[1]
        yaw_angle = -math.atan2(dy, dx) * 180.0 / math.pi

        # Track head movement and count reps
        if prev_yaw_angle <= angle_threshold and yaw_angle > angle_threshold:
            angle_count += 1
        elif prev_yaw_angle >= -angle_threshold and yaw_angle < -angle_threshold:
            angle_count += 1

        if angle_count >= 2:
            reps += 1
            print("Reps:", reps)
            angle_count = 0

        prev_yaw_angle = yaw_angle

