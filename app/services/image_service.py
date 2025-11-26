import numpy as np
import cv2

class ImageService:
    def __init__(self):
        pass

    async def recognize_faces(self, image_data: bytes) -> list[tuple[int, int, int, int]]:
        try:
            image = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

            face_bounding_boxes = [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in faces]


            return face_bounding_boxes
        
        except Exception as e:
            raise e
        
    async def draw_bounding_boxes(self, image_data: bytes, boxes: list[tuple[int, int, int, int]]) -> bytes:
        try:
            image = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            for (x, y, w, h) in boxes:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
            _, buffer = cv2.imencode('.jpg', image)
            return buffer.tobytes()
        
        except Exception as e:
            raise e
        
    async def blur_bounding_boxes(self, image_data: bytes, boxes: list[tuple[int, int, int, int]]) -> bytes:
        try:
            image = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            for (x, y, w, h) in boxes:
                face_region = image[y:y+h, x:x+w]
                blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
                image[y:y+h, x:x+w] = blurred_face

            _, buffer = cv2.imencode('.jpg', image)
            return buffer.tobytes()
        
        except Exception as e:
            raise e
