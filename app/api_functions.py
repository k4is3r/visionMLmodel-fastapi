from fastapi.responses import JSONREsponse

def ResponseModel(data, message):
    return JSONResponse(
            status_code= 200,
            content={"code": status_code, "status": message, "data": data}
            )

def ErrorResponseModel(code, message):
    return JSONResponse(
            status_code = code,
            content= {"code": code, "message": message}
            )

