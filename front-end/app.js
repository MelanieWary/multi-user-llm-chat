// Définition de l’URL de base de l’API
const API_BASE = "http://localhost:8000";

// Sélection des éléments HTML pour interagir avec eux
const sessionSelect = document.getElementById("sessionSelect");
const messagesDiv = document.getElementById("messages");
const simulateBtn = document.getElementById("simulateBtn");
const messageInput = document.getElementById("messageInput");

// Variables pour garder en mémoire la session en cours et le nombre de messages
let currentSessionId = 0;
let currentMessageId = 0;
let lastMessage = null;

/**
 * Fonction qui récupère la liste des sessions depuis l'API
 * et les ajoute dans la liste déroulante.
 */
async function loadSessions() {
  const res = await fetch(`${API_BASE}/sessions`); // Appel API
  const sessions = await res.json(); // Conversion JSON

  sessions.forEach(session => {
    const option = document.createElement("option"); // Création d'une option <option>
    option.value = session.session_id; // Valeur = ID de la session
    option.textContent = `Session ${session.session_id} (${session.nb_messages} msg)`; // Texte lisible
    sessionSelect.appendChild(option); // Ajout à la liste déroulante
  });
}

/**
 * Fonction qui affiche un message dans le chat
 * @param {Object} msg - Un message du format attendu
 */
function displayMessage(msg) {

  if (msg.message.length == 0) {
    // If message is empty, do nothing
    return;
  }

  const div = document.createElement("div"); // Crée un élément <div>
  div.classList.add("message", `${msg.user_type}`); // Ajoute des classes CSS pour le style
  div.textContent = `[${msg.user_type} - ${msg.user_name}] : ${msg.message}`; // Texte à afficher
  messagesDiv.appendChild(div); // Ajoute le message à l'affichage
  messagesDiv.scrollTop = messagesDiv.scrollHeight; // Scroll vers le bas automatiquement
}

/**
 * Funtion that retrives the nth message of a given session
 * @param {number} sessionId
 * @param {number} messageId
 */
async function getMessage() {
  let sessionId = parseInt(sessionSelect.value);
  let messageId = currentMessageId;
  console.log("Session id: ", sessionId)
  console.log("Required message id: ", messageId)

  const res = await fetch(`${API_BASE}/simulated_message/${sessionId}/${messageId}`);
  const msg = await res.json(); // Conversion JSON
  console.log("Raw message:", msg);
  console.log("Conversation: ", msg.conversation[0]);
  currentMessageId += 1;
  console.log("Future message id: ", currentMessageId);

  if (msg.conversation && msg.conversation.length > 0) {
    displayMessage(msg.conversation[0]); // Affiche le message dans la page
    lastMessage = msg;
    await getAssistantResponse();
  } else {
    console.warn("Pas de message dans la conversation.");
  }
}

/**
 * Fonction qui reset l'id de message
 */
 function resetMessageId() {
  currentMessageId = 0;
  lastMessage = null;
  console.log("Message id reset to 0")
  return currentMessageId
 }

// une fonction send message qui envoie à l'endpoint avec le LLM et display sa réponse
async function getAssistantResponse() {

  if (lastMessage === null) {
    return;
  }

  let msg = lastMessage;

  // Envoie du message à l’API (POST)
  const res = await fetch(`${API_BASE}/assistant_message`, {
    method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(msg),
    });

    const bobResponse = await res.json(); // Bob response
    if (bobResponse.conversation && bobResponse.conversation.length > 0) {
    displayMessage(bobResponse.conversation[0]); // Display message
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
