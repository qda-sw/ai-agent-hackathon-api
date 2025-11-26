from fastapi import APIRouter, UploadFile, File, Body, Form
from fastapi.responses import StreamingResponse
from app.controllers.image_controller import ImageController


router = APIRouter(prefix="/image", tags=["image"])
controller = ImageController()

@router.post("/face_recognition/")
async def face_recognition(
    image: UploadFile = File(...),
):
    image_data = await image.read()
    bboxes = await controller.recognize_faces(image_data)
    return { 'bboxes': bboxes }

@router.post("/draw")
async def draw_boxes(
    image: UploadFile = File(...),
    bboxes: str = Form(...),
):
    image_data = await image.read()
    boxed_image = await controller.draw_bounding_boxes(image_data, bboxes)
    
    return StreamingResponse(content=boxed_image, media_type="image/jpeg")

@router.post("/blur")
async def blur_boxes(
    image: UploadFile = File(...),
    bboxes: str = Form(...),
):
    image_data = await image.read()
    blurred_image = await controller.blur_bounding_boxes(image_data, bboxes)
    
    return StreamingResponse(content=blurred_image, media_type="image/jpeg")