// =================================================================
// Islamic Finance Assistant - Frontend Logic
// =================================================================

// FastAPI backend endpoint
const API_ENDPOINT = "/chat";

// Session ID storage key in localStorage
const SESSION_STORAGE_KEY = "islamicFinanceChat.sessionId";

// DOM elements
const chatWindow = document.getElementById("chatWindow");
const typingIndicator = document.getElementById("typingIndicator");
const composerForm = document.getElementById("composerForm");
const questionInput = document.getElementById("questionInput");
const sendBtn = document.getElementById("sendBtn");

/**
 * Returns an existing session ID from localStorage,
 * or creates a new UUID on the first visit.
 */
function getOrCreateSessionId() {
  let sessionId = localStorage.getItem(SESSION_STORAGE_KEY);
  if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem(SESSION_STORAGE_KEY, sessionId);
  }
  return sessionId;
}

const sessionId = getOrCreateSessionId();

/**
 * Appends a message to the chat window.
 * @param {"user"|"assistant"|"error"} role
 * @param {string} text
 */
function appendMessage(role, text) {
  const wrapper = document.createElement("div");
  wrapper.className =
    role === "user"
      ? "message user-message"
      : role === "error"
      ? "message assistant-message error-message"
      : "message assistant-message";

  // Avatar
  const avatar = document.createElement("div");
  avatar.className =
    role === "user" ? "avatar user-avatar" : "avatar assistant-avatar";
  avatar.setAttribute("aria-hidden", "true");
  avatar.innerHTML =
    role === "user"
      ? `<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5Z"/></svg>`
      : `<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2 15 9 22 10 17 15 18 22 12 18.5 6 22 7 15 2 10 9 9 12 2Z"/></svg>`;

  // Message bubble
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = (text || "").trim();

  wrapper.appendChild(avatar);
  wrapper.appendChild(bubble);
  chatWindow.appendChild(wrapper);

  scrollToBottom();
}

// Scroll chat to the latest message
function scrollToBottom() {
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Show or hide typing indicator
function setTypingIndicator(visible) {
  typingIndicator.hidden = !visible;
  if (visible) scrollToBottom();
}

// Enable or disable input while sending
function setSendingState(isSending) {
  sendBtn.disabled = isSending;
  questionInput.disabled = isSending;
}

/**
 * Sends the user's question to the FastAPI backend.
 */
async function sendQuestionToServer(question) {
  
  const response = await fetch(API_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      session_id: sessionId,
      question: question,
    }),
  });

  if (!response.ok) {
    throw new Error(`Request failed (HTTP ${response.status})`);
  }

  const data = await response.json();
  console.log(data);
  return data.answer || data.Assistant || "";
}

// Handle form submission
composerForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const question = questionInput.value.trim();
  if (!question) return;

  appendMessage("user", question);
  questionInput.value = "";

  setSendingState(true);
  setTypingIndicator(true);

  try {
    const answer = await sendQuestionToServer(question);
    setTypingIndicator(false);
    appendMessage(
      "assistant",
      answer || "Sorry, no response was received from the assistant."
    );
  } catch (error) {
    setTypingIndicator(false);
    appendMessage(
      "error",
      "Unable to reach the server. Please try again."
    );
    console.error(error);
  } finally {
    setSendingState(false);
    questionInput.focus();
    scrollToBottom();
  }
});

// Focus the input field on page load
window.addEventListener("load", () => {
  questionInput.focus();
});
