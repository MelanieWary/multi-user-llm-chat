from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, HTTPException

from api.common.data_models import ChatPayloadAndDbObject, MessageRetrievalInputPayload, UserMessage, UserType
from api.services import assistant_response as AssistantService
from api.services import sessions as SessionsService
from api.services import simulated_message as SimulationService

load_dotenv()

app = FastAPI(
   swagger_ui_parameters={'tryItOutEnabled': True}
)


# TODO: endpoint init session that (re)set working_conv_db ??


@app.get("/session_ids")
def get_session_ids():
    return SessionsService.get_session_ids()
# TODO: to delete


@app.get("/sessions")
def get_sessions():
    return SessionsService.get_sessions_info()


@app.get(
    "/simulated_message/{session_id}/{message_id}",
    response_model=ChatPayloadAndDbObject,
)
def get_mocked_message(
    session_id: int,
    message_id: int,
) -> ChatPayloadAndDbObject:
    try:
        return SimulationService.get_mocked_message(session_id, message_id)
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail=f"No message with id {message_id} for session {session_id}"
        )


@app.post(
    "/assistant_message",
    response_model= ChatPayloadAndDbObject,
)
def get_assistant_response(payload:ChatPayloadAndDbObject):
    return AssistantService.get_assistant_response(payload)


if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8000)
