import cv2
import numpy as np
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet
import webbrowser

# Load the encryption key
with open('encryption_key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data.encode()).decode()

def main():
    cap = cv2.VideoCapture(0)
    link_detected = False

    while True:
        ret, frame = cap.read()

        if not ret or link_detected:
            break

        decoded_objects = decode(frame)

        for obj in decoded_objects:
            encrypted_data = obj.data.decode('utf-8')
            try:
                decrypted_data = decrypt_data(encrypted_data)

                if decrypted_data.startswith('http://') or decrypted_data.startswith('https://'):
                    link_detected = True
                    break

                points = obj.polygon
                if len(points) > 4: 
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))

                else:
                    hull = points

                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (0, 255, 0), 3)

                x, y, w, h = obj.rect
                cv2.putText(frame, decrypted_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            except Exception as e:
                print("Error decrypting data:", e)

        cv2.imshow('QR Code Scanner', frame)

        # Keyboard "q" untuk berhenti pada scanner yollo
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if link_detected and decrypted_data:
        print(f"Opening URL: {decrypted_data}")
        try:
            browser = webbrowser.get()
            browser.open(decrypted_data)
        except webbrowser.Error as e:
            print("Failed to open browser:", e)

if __name__ == "__main__":
     main()