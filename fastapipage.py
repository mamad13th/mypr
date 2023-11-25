import uvicorn
from fastapi import FastAPI,Request, Path, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory="./templates")

@app.middleware("http")
async def error_middleware(request: Request, call_next):
    response = await call_next(request)
    if response.status_code != 200:
        return templates.TemplateResponse("index.html", {"request":request}, status_code=response.status_code)
    return response


@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)



