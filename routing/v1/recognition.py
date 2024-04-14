import io

import pandas as pd
from fastapi import APIRouter, Response
from starlette.responses import StreamingResponse

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


@router.post(
    "/report",
    description="getting the answer in excel format",
)
async def get_report(req: RecognizeRequest):
    back_side = base642nparray(req.back_side)
    front_side = base642nparray(req.front_side)

    pipeline_json, rules = result_pipeline([back_side, front_side])

    try:
        pipeline_json = str2json(pipeline_json)

        df = pd.DataFrame(pipeline_json)
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer) as writer:
            df.to_excel(writer, index=False)

        return StreamingResponse(
            io.BytesIO(buffer.getvalue()),
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={"Content-Disposition": f"attachment; filename=data.csv"}
        )

    except Exception as e:
        raise ValueError(f"error json dumping: {e}")
