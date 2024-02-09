import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init("templates")


@app.get("/")
@template(template_file="index.html")
def index():
    return {"user_name": "amit"}


if __name__ == "__main__":  # if this file is being run directly
    # for testing
    uvicorn.run(app)
