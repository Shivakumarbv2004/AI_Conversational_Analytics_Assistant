import streamlit as st
import requests

st.set_page_config(page_title="AI Analytics Assistant", page_icon="📈", layout="centered")

# Injecting Custom CSS for Rich Aesthetics
st.markdown("""
<style>
    /* Global Styles & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }

    /* Header styling */
    h1 {
        background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* Chat bubbles styling (Glassmorphism) */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1) !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.4) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255,255,255,0.5);
    }
    
    /* Input box styling */
    .stChatInputContainer {
        border-radius: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        border: 1px solid rgba(200,200,200,0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2822/2822791.png", width=100)
    st.title("About")
    st.info(
        "**AI Conversational Analytics Assistant**\n\n"
        "Ask natural language questions about your Enterprise SaaS Analytics dataset. "
        "Powered by an autonomous Multi-Agent system and Groq LLMs."
    )
    st.markdown("---")
    st.markdown("### Supported Commands:")
    st.markdown("- *'What are the total sales?'*\n- *'Which branch performed best?'*\n- *'How do people prefer to pay?'*\n- *'Give me an overview'*")

# Main content
st.title("Enterprise SaaS Analytics AI 📈")
st.markdown("<p style='text-align: center; color: #555; font-size: 1.1rem;'>Instantly query your enterprise data with AI.</p>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a welcoming initial message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I am your AI Analytics Assistant. You can ask me anything about the Enterprise SaaS Analytics data."
    })

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("E.g., What are the top products?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare request to FastAPI backend
    API_URL = "http://127.0.0.1:8000/chat"
    
    with st.spinner("Analyzing your data..."):
        try:
            response = requests.post(API_URL, json={"question": prompt})
            response.raise_for_status()
            
            data = response.json()
            answer = data.get("answer", "No answer received.")
            
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(answer)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to backend: {e}")
            if hasattr(e, 'response') and e.response is not None:
                st.error(f"Backend details: {e.response.text}")
