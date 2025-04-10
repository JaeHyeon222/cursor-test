from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from openai import OpenAI
import logging
import httpx
from ....core.config import get_settings

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()
settings = get_settings()

class ImageRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_image(request: ImageRequest):
    try:
        # API 키 로깅 (마스킹 처리)
        api_key = settings.OPENAI_API_KEY
        masked_key = f"{api_key[:8]}...{api_key[-4:]}" if api_key else "Not Set"
        logger.info(f"Using API key: {masked_key}")
        
        # OpenAI 클라이언트 초기화
        http_client = httpx.Client()
        client = OpenAI(
            api_key=api_key,
            http_client=http_client
        )
        logger.info("OpenAI client initialized successfully")
        
        # 이미지 생성 요청
        logger.info(f"Generating image with prompt: {request.prompt}")
        response = client.images.generate(
            model="dall-e-3",
            prompt=request.prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        logger.info("Image generated successfully")
        
        image_url = response.data[0].url
        return JSONResponse(content={"image_url": image_url})
    except Exception as e:
        logger.error(f"Error generating image: {str(e)}")
        logger.exception("Full error details:")
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")
    finally:
        if 'http_client' in locals():
            http_client.close() 