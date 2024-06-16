
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse 
from pydantic import BaseModel

app = FastAPI()
print(FastAPI)

CORRECT_PASSWORD = 'SyrupIsTheBest'

class PasswordRequest(BaseModel):
    password: str

@app.post("/validate_password")
async def validate_password(request: PasswordRequest):
    if request.password == CORRECT_PASSWORD:
        return {"valid": True}
    else:
        return {"valid": False}

@app.get("/download_pdf")
async def download_pdf():
    pdf_file_path = 'static/DummyTest.pdf'  #Update depending on what PDF file
    return FileResponse(pdf_file_path, media_type='application/pdf', filename='DummyTest.pdf')
# print(FileResponse)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
