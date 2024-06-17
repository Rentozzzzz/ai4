# This one failed to work unfortunately, I tried to make it work but it was not working as expected. I will try to fix it next time.
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, FileResponse 
from pydantic import BaseModel

app = FastAPI()

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
    pdf_file_path = 'DocPDF/TheWayOfHAMLET'  #Update depending on what PDF file
    return FileResponse(pdf_file_path, media_type='application/pdf', filename='TheWayOfHAMLET.pdf')
# print(FileResponse)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
