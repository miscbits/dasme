from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html.j2",
        context={"message": "Welcome to my space!"}
    )


@app.get("/blog/{name}", response_class=HTMLResponse)
async def blog(request: Request, name: str):
    return templates.TemplateResponse(
        request=request,
        name=f"blogs/{name}.html.j2",
    )
