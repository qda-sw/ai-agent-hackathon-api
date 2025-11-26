from fastapi.exceptions import HTTPException

from app.services.image_service import ImageService

import json
import io

class ImageController:
    def __init__(self):
        self.image_service = ImageService()
    
    async def recognize_faces(self, image_data: bytes) -> list[tuple[int, int, int, int]]:
        bboxes = await self.image_service.recognize_faces(image_data)
        return bboxes
        
    async def draw_bounding_boxes(self, image_data: bytes, boxes: str) -> bytes:
        try:
            bboxes = json.loads(boxes)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid bounding boxes format")
        image = await self.image_service.draw_bounding_boxes(image_data, bboxes)
        image = io.BytesIO(image)
        return image
    
    async def blur_bounding_boxes(self, image_data: bytes, boxes: str) -> bytes:
        try:
            bboxes = json.loads(boxes)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid bounding boxes format")
        image = await self.image_service.blur_bounding_boxes(image_data, bboxes)
        image = io.BytesIO(image)
        return image