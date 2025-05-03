from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI

from api.services import sessions as SessionsService

load_dotenv()

app = FastAPI(
   swagger_ui_parameters={'tryItOutEnabled': True}
)

@app.get("/session_ids")
def get_session_ids():
    return SessionsService.get_session_ids()


@app.get("/")
def test():
    return {"Hello": "World"}


if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8000)
