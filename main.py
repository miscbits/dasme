from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2.exceptions import TemplateNotFound

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.exception_handler(TemplateNotFound)
@app.exception_handler(404)
async def custom_http_exception_handler(request, exc):
    return templates.TemplateResponse(
        request=request,
        name="404.html.j2",
        status_code=404
    )


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
