from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI

from api.common.data_models import ChatPayloadAndDbObject, MessageRetrievalInputPayload, UserMessage, UserType
from api.services import assistant_response as AssistantService
from api.services import sessions as SessionsService
from api.services import simulated_message as SimulationService

load_dotenv()

app = FastAPI(
   swagger_ui_parameters={'tryItOutEnabled': True}
)

@app.get("/session_ids")
def get_session_ids():
    return SessionsService.get_session_ids()


@app.get("/sessions")
def get_sessions():
    return SessionsService.get_sessions_info()


@app.post(
    "/mocked_message",
    response_model=ChatPayloadAndDbObject,
)
def get_mocked_message(payload: MessageRetrievalInputPayload):
    return SimulationService.get_mocked_message(payload.session_id, payload.message_id)
# TODO make it a GET endpoint

@app.post(
    "/assistant_message",
    response_model= ChatPayloadAndDbObject,
)
def get_assistant_response(payload:ChatPayloadAndDbObject):
    return AssistantService.get_assistant_response(payload)


@app.post(
    "/next_messages",
    response_model= ChatPayloadAndDbObject,
)
def get_next_user_and_assistant_messages(payload:MessageRetrievalInputPayload):
    return AssistantService.get_next_user_and_assistant_messages(payload)


if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8000)
