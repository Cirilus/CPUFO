from fastapi import APIRouter

from ml.conversation_pipeline import result_pipeline
from schemas.recognition import RecognizeRequest, RecognizeResponse
from schemas.recognition import Product
from utils.utils import base642nparray, str2json

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/recognize",
    description="getting the answer",
    response_model=RecognizeResponse,
)
async def get_answer(req: RecognizeRequest):
    back_side = base642nparray(req.back_side)
    front_side = base642nparray(req.front_side)

    pipeline_json, rules = result_pipeline([back_side, front_side])

    try:
        pipeline_json = str2json(pipeline_json)

        product = Product().parse_obj(pipeline_json)

    except Exception as e:
        raise ValueError(f"error json dumping: {e}")

    return RecognizeResponse(
        product=product,
        rule=rules,
    )
