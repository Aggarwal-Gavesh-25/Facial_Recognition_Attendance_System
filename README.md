## Facial Recognition Attendance System

The Facial Recognition Attendance System is a desktop application developed in Python using the Tkinter library. It serves as an efficient solution for managing attendance records by employing facial recognition technology to identify students. The system matches the captured facial images with the database of registered students and updates their attendance automatically.

## Features

- Robust facial recognition algorithm for accurate identification.
- User-friendly GUI developed with Tkinter.
- Ability to add, update, delete, and search student records.
- Input validation for mandatory fields.
- Display of student records in a tabular format.
- Integration with MySQL database for storing student information and attendance records.
- Real-time video streaming for capturing facial images.
- Automated attendance updating based on facial matches.


## Usage

1. Launch the application by running the main.py script.
2. Register students by providing their details and capturing their facial images.
3. Use the "Attendance" button to initiate the attendance capturing process.
4. The system will match the captured facial images with the database and update attendance accordingly.
5. View attendance records and student details in the provided interface.

## Dependencies

- Tkinter
- OpenCV
- MySQL Connector

## Files

- [main.py](https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/blob/main/Facial%20Recognition%20Attendance%20System/Scripts/main.py): Main script for the Facial Recognition Attendance System application.
- [student.py](https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/blob/main/Facial%20Recognition%20Attendance%20System/Scripts/student.py): Script containing the Student class for managing student details.
- [face_recognition.py](https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/blob/main/Facial%20Recognition%20Attendance%20System/Scripts/face_recognition.py): Script for facial recognition functionality.
- [detect_face_video.py](https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/blob/main/Facial%20Recognition%20Attendance%20System/Scripts/detect_face_video.py): Script to detect faces in a live video stream.

## Future Improvements / Plans
- Implementation of user authentication and authorization.
- Implementation of additional features such as automatic notification for absentees and latecomers.
- Integration with biometric sensors for enhanced security and accuracy.
- Enhancement of GUI design for a more modern and intuitive interface.

## Result

- main.py :-
<img width="1440" alt="1" src="https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/assets/118240223/0bfeb235-90f5-400e-ab77-a94f47792e4b">

- student.py :-
<img width="1440" alt="2" src="https://github.com/Aggarwal-Gavesh-25/Facial_Recognition_Attendance_System/assets/118240223/a8d972cb-78b8-4423-b7fc-a6a1e7a25713">

- face_recognition.py :-


- detect_face_video.py :-
