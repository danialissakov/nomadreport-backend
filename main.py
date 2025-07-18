from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from diagram_generator import generate_diagram_dynamic
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # На проде — домен фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-report")
async def generate_report(
    sectors: str = Form(...),
    values: str = Form(...),
    color: str = Form("#9b5de5"),
    title: str = Form("Отчет")
):
    try:
        sector_list = json.loads(sectors)
        value_list = json.loads(values)
        path = generate_diagram_dynamic(sector_list, value_list, title, color)
        return FileResponse(path, media_type="image/png", filename="report.png")
    except Exception as e:
        return {"error": str(e)}