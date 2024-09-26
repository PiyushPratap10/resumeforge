from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from tempfile import NamedTemporaryFile
from generate_resume import generate_resume
import uvicorn
from typing import List, Dict
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory='static'), name="static")
class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: str
    education: List[Dict[str, str]]
    experience: List[str]
    skills: List[str]
    projects: List[Dict[str, str]]
    certifications: List[Dict[str, str]]


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/build-resume/", response_class=HTMLResponse)
async def build_resume(request: Request):
    return templates.TemplateResponse("build_resume.html", {"request": request})

@app.get("/score-resume/", response_class=HTMLResponse)
async def score_resume(request: Request):
    return templates.TemplateResponse("score_resume.html", {"request": request})


@app.post("/generate-resume/")
async def generate_resume_endpoint(data: ResumeData):
    # Create a temporary file to store the PDF
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        try:
            # Generate the resume PDF
            generate_resume(
                name=data.name,
                email=data.email,
                phone=data.phone,
                linkedin=data.linkedin,
                education=data.education,
                experience=data.experience,
                skills=data.skills,
                projects=data.projects,
                certifications=data.certifications,
                file_path=tmp_file.name
            )

            # Return the generated PDF as a file response
            return FileResponse(tmp_file.name, filename="resume.pdf", media_type="application/pdf")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port=8001)
