// Définition de l’URL de base de l’API
const API_BASE = "http://localhost:8000";

// Sélection des éléments HTML pour interagir avec eux
const sessionSelect = document.getElementById("sessionSelect");
const messagesDiv = document.getElementById("messages");
const getBtn = document.getElementById("getBtn");
const sendBtn = document.getElementById("sendBtn");
const messageInput = document.getElementById("messageInput");

// Variables pour garder en mémoire la session en cours et le nombre de messages
let currentSessionId = 0;
let currentMessageId = 0;
let msg = {};

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
  const div = document.createElement("div"); // Crée un élément <div>
  console.log(div)
  div.classList.add("message", `${msg.user_type}`); // Ajoute des classes CSS pour le style
  div.textContent = `[${msg.user_type} - ${msg.user_name}] : ${msg.message}`; // Texte à afficher
  if (msg.user_type === 'Customer') {
    div.style.border = "1px solid white";
    div.style.background = "purple";
  }
  if (msg.user_type === 'Employee') {
    div.style.border = "1px solid white";
    div.style.background = "green";
  }
  if (msg.user_type === 'Assistant') {
    div.style.border = "1px solid white";
    div.style.background = "yellow";
  }
  console.log(div)
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
    return msg;
  } else {
    console.warn("Pas de message dans la conversation.");
  }
}

/**
 * Fonction qui reset l'id de message
 */
 function resetMessageId() {
  currentMessageId = 0;
  console.log("Message id reset to 0")
  return currentMessageId
 }

// une fonction send message qui envoie à l'endpoint avec le LLM et display sa réponse
async function getAssistantResponse() {
  console.log("POST body :" + JSON.stringify(msg));

  const userMessage = {
    session_id: currentSessionId,
    conversation: [
      {
        user_id: 2,
        user_type: "Employee",
        user_name: "Test",
        timestamp: 0.0,
        message: "Hello Bob, what's the weather in France? ",
        nb_tokens: 0
      }
    ]
  };

  // Envoie du message à l’API (POST)
  const res = await fetch(`${API_BASE}/assistant_message`, {
    method: "POST",
      headers: { "Content-Type": "application/json" },
//      body: JSON.stringify(msg),
      body: JSON.stringify(userMessage) // On convertit en JSON
    });

    const bobResponse = await res.json(); // Réponse de l’utilisateur 3 (automatique)
    if (bobResponse.conversation && bobResponse.conversation.length > 0) {
    displayMessage(bobResponse.conversation[0]); // Affiche le message dans la page
  };
  }


// send btn : si input vide, récup message mocké et l'envoie au LLM - si input non vide, envoie l'inout au LLM



// Événement : quand on change la session dans la liste, on recharge les messages
sessionSelect.addEventListener("change", () => {
  messagesDiv.innerHTML = ""; // On vide l'affichage précédent
  resetMessageId();
});

// Event: when we click on "Get" button, we excute getMessage
getBtn.addEventListener("click", getMessage);

// Événement : quand on clique sur "Envoyer", on exécute getAssistantResponse
sendBtn.addEventListener("click", getAssistantResponse());

// Au démarrage, on charge les sessions disponibles
loadSessions();



/**
 * Fonction qui charge les messages d’une session donnée
 * @param {number} sessionId - ID de la session à charger
 */
//async function loadMessages(sessionId) {
//  messagesDiv.innerHTML = ""; // On vide l'affichage précédent
//  currentSessionId = sessionId; // On mémorise la session choisie
//
//  // On récupère de nouveau la liste des sessions pour obtenir le nombre de messages
//  const res = await fetch(`${API_BASE}/sessions`);
//  const sessions = await res.json();
//  const session = sessions.find(s => s.session_id == sessionId);
//  currentMessageCount = session.nb_messages;
//
//  // On boucle sur tous les messages de la session
//  for (let i = 0; i < currentMessageCount; i++) {
//    const msgRes = await fetch(`${API_BASE}/simulated_message/${sessionId}/${i}`); // Appel API
//    const msgData = await msgRes.json(); // Conversion JSON
//    const msg = msgData.conversation[0]; // Récupère le message
//    displayMessage(msg); // Affiche le message dans la page
//  }
//}



///**
// * Fonction qui envoie un message à l'API, puis affiche la réponse automatique
// */
//async function sendMessage() {
//  const userId = parseInt(userIdSelect.value); // Utilisateur choisi (1 ou 2)
//  const message = messageInput.value.trim(); // Contenu du message
//
//  if (!message || currentSessionId === null) return; // Si vide ou pas de session, on ne fait rien
//
//  // Prépare le message à envoyer
//  const userMessage = {
//    session_id: currentSessionId,
//    conversation: [
//      {
//        user_id: userId,
//        user_type: "simu",
//        user_name: `User${userId}`,
//        timestamp: Date.now(),
//        message: message,
//        nb_tokens: 0
//      }
//    ]
//  };
//
//  displayMessage(userMessage.conversation[0]); // Affiche tout de suite le message dans le chat
//  messageInput.value = ""; // Vide le champ de saisie
//
//  // Envoie du message à l’API (POST)
//  const res = await fetch(`${API_BASE}/assistant_message`, {
//    method: "POST",
//    headers: { "Content-Type": "application/json" },
//    body: JSON.stringify(userMessage) // On convertit en JSON
//  });
//
//  const botResponse = await res.json(); // Réponse de l’utilisateur 3 (automatique)
//  displayMessage(botResponse.conversation[0]); // On affiche sa réponse
//}