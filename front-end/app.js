// Definition of API base url
const API_BASE = "http://localhost:8000";

// Selection of HTML elements to interact with them
const sessionSelect = document.getElementById("sessionSelect");
const messagesDiv = document.getElementById("messages");
const simulateBtn = document.getElementById("simulateBtn");
const messageInput = document.getElementById("messageInput");

// Variables to keep in memory: current session, current message ID, and last message received.
let currentSessionId = 0;
let currentMessageId = 0;
let lastMessage = null;

/**
 * Function to get available sessions from API
 * and display them in the dropdown
 */
async function loadSessions() {
  const res = await fetch(`${API_BASE}/sessions`); // API call
  const sessions = await res.json(); // JSON conversion

  sessions.forEach(session => {
    const option = document.createElement("option"); // Creation of a session option <option>
    option.value = session.session_id; // Set option value to session ID
    option.textContent = `Session ${session.session_id} (${session.nb_messages} msg)`; // Set text to display for the option
    sessionSelect.appendChild(option); // Add to dropdown
  });
}

/**
 * Function that display a message in the chat box
 * @param {Object} msg
 */
function displayMessage(msg) {

  if (msg.message.length == 0) {
    // If message is empty, do nothing
    return;
  }
  // else:
  const div = document.createElement("div"); // Create a <div> element
  div.classList.add("message", `${msg.user_type}`); // Add CSS classes linked to user_type for style
  div.textContent = `[${msg.user_type} - ${msg.user_name}] : ${msg.message}`; // Text to display
  messagesDiv.appendChild(div); // Add message to chat box
  messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto scroll down
}

/**
 * Funtion that retrieves and display the message of a given id from the current session,
 * and then retrieves and display assistant response to this message
 * @param {number} sessionId
 * @param {number} messageId
 */
async function getMessage() {
  let sessionId = parseInt(sessionSelect.value); // Selected session ID
  let messageId = currentMessageId; // Message ID to retrieve
  console.log("Session id: ", sessionId)
  console.log("Required message id: ", messageId)

  const res = await fetch(`${API_BASE}/simulated_message/${sessionId}/${messageId}`); // API call
  const msg = await res.json(); // JSON conversion
  console.log("Raw message:", msg);
  console.log("Conversation: ", msg.conversation[0]);
  currentMessageId += 1; // increment message ID for next round
  console.log("Future message id: ", currentMessageId);

  if (msg.conversation && msg.conversation.length > 0) {
    displayMessage(msg.conversation[0]); // Display message, if any
    lastMessage = msg; // Keep in memory message used for the API call to assistant
    await getAssistantResponse(); // API call to get assistant response
  } else {
    console.warn("Pas de message dans la conversation.");
  }
}

/**
 * Function that resets message ID and last message
 */
 function resetMessageId() {
  currentMessageId = 0;
  lastMessage = null;
  console.log("Message id reset to 0")
  return currentMessageId
 }

/**
 * Function that sends last message to retrieve assistant response, and display this latter
 */
async function getAssistantResponse() {

  if (lastMessage === null) {
    // If last message is empty, do nothing
    return;
  }
  // else:
  let msg = lastMessage;

  // API call
  const res = await fetch(`${API_BASE}/assistant_message`, {
    method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(msg),
    });

    const bobResponse = await res.json(); // JSON conversion of Bob response
    if (bobResponse.conversation && bobResponse.conversation.length > 0) {
    displayMessage(bobResponse.conversation[0]); // Display Bob response
  };
  }


// Event : when we change the selected session in the dropdown, we reset the chat window and message id
sessionSelect.addEventListener("change", () => {
  messagesDiv.innerHTML = "";
  resetMessageId();
});

// Event: when we click on "Simulate" button, we excute getMessage
simulateBtn.addEventListener("click", getMessage);

// At start, we load available session
loadSessions();
