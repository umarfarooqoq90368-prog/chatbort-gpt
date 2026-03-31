import streamlit as st
from groq import Groq
import os
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env file. Please add it to proceed.")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(page_title="Umar AI", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

    * {
        font-family: 'Outfit', sans-serif;
    }

    /* ==================== ADVANCED BACKGROUND ==================== */
    .stApp {
        background: 
            radial-gradient(ellipse at 10% 20%, rgba(0, 255, 204, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 80%, rgba(255, 0, 255, 0.12) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 10%, rgba(120, 0, 255, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 50%, rgba(0, 255, 150, 0.08) 0%, transparent 40%),
            radial-gradient(ellipse at 20% 90%, rgba(255, 100, 0, 0.06) 0%, transparent 40%),
            linear-gradient(180deg, #050508 0%, #0a0a15 50%, #080812 100%);
        background-size: 200% 200%, 200% 200%, 150% 150%, 200% 200%, 150% 150%, 100% 100%;
        animation: cosmic-bg 25s ease infinite;
        min-height: 100vh;
        overflow-x: hidden;
    }

    @keyframes cosmic-bg {
        0%, 100% { 
            background-position: 0% 0%, 100% 100%, 25% 10%, 75% 50%, 20% 80%, 0% 0%;
        }
        25% { 
            background-position: 50% 25%, 25% 75%, 50% 25%, 25% 75%, 75% 25%, 0% 0%;
        }
        50% { 
            background-position: 100% 50%, 0% 50%, 75% 50%, 50% 100%, 25% 50%, 0% 0%;
        }
        75% { 
            background-position: 50% 75%, 75% 25%, 100% 75%, 25% 25%, 50% 75%, 0% 0%;
        }
    }

    /* Floating particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, rgba(0, 255, 204, 0.8), transparent),
            radial-gradient(2px 2px at 40% 70%, rgba(255, 0, 255, 0.8), transparent),
            radial-gradient(1px 1px at 60% 20%, rgba(0, 255, 150, 0.8), transparent),
            radial-gradient(2px 2px at 80% 50%, rgba(255, 150, 0, 0.8), transparent),
            radial-gradient(1px 1px at 10% 80%, rgba(0, 150, 255, 0.8), transparent),
            radial-gradient(2px 2px at 90% 10%, rgba(255, 0, 150, 0.8), transparent),
            radial-gradient(1px 1px at 50% 90%, rgba(150, 0, 255, 0.8), transparent);
        background-size: 550px 550px;
        animation: particles-float 30s linear infinite;
        pointer-events: none;
        z-index: 0;
    }

    @keyframes particles-float {
        0% { transform: translateY(0) rotate(0deg); }
        100% { transform: translateY(-550px) rotate(360deg); }
    }

    /* ==================== HEADER ==================== */
    .header-wrapper {
        position: relative;
        padding: 30px 0 20px;
        text-align: center;
        z-index: 10;
    }

    .header-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 400px;
        height: 150px;
        background: radial-gradient(ellipse, rgba(0, 255, 204, 0.2) 0%, rgba(255, 0, 255, 0.1) 30%, transparent 70%);
        animation: header-aurora 8s ease-in-out infinite;
        pointer-events: none;
    }

    @keyframes header-aurora {
        0%, 100% { 
            transform: translateX(-50%) scale(1) rotate(0deg);
            opacity: 0.6;
        }
        33% { 
            transform: translateX(-50%) scale(1.2) rotate(5deg);
            opacity: 1;
        }
        66% { 
            transform: translateX(-50%) scale(0.9) rotate(-3deg);
            opacity: 0.8;
        }
    }

    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        position: relative;
        display: inline-block;
        animation: title-float 4s ease-in-out infinite;
    }

    .main-title::before {
        content: '🤖';
        position: absolute;
        left: -60px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 2.5rem;
        animation: robot-bounce 2s ease-in-out infinite;
    }

    .main-title::after {
        content: '';
        position: absolute;
        inset: -20px -40px;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 204, 0.1), transparent);
        border-radius: 20px;
        animation: title-beam 3s ease-in-out infinite;
        z-index: -1;
    }

    @keyframes title-beam {
        0%, 100% { opacity: 0.3; transform: scaleX(0.8); }
        50% { opacity: 0.8; transform: scaleX(1.1); }
    }

    @keyframes title-float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }

    @keyframes robot-bounce {
        0%, 100% { transform: translateY(-50%) scale(1); }
        50% { transform: translateY(-60%) scale(1.1); }
    }

    .title-text {
        background: linear-gradient(135deg, #00ffcc 0%, #00ff88 25%, #00ffcc 50%, #ff00ff 75%, #00ffcc 100%);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow-title 5s ease infinite;
        text-shadow: none;
        filter: drop-shadow(0 0 30px rgba(0, 255, 204, 0.5));
    }

    @keyframes rainbow-title {
        0% { background-position: 0% 50%; }
        25% { background-position: 50% 25%; }
        50% { background-position: 100% 50%; }
        75% { background-position: 50% 75%; }
        100% { background-position: 0% 50%; }
    }

    .subtitle-wrapper {
        margin-top: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        animation: subtitle-fade 4s ease-in-out infinite;
    }

    .subtitle-dot {
        width: 6px;
        height: 6px;
        background: #00ffcc;
        border-radius: 50%;
        animation: dot-pulse-3 2s ease-in-out infinite;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.8);
    }

    .subtitle-dot:nth-child(2) { animation-delay: 0.3s; }
    .subtitle-dot:nth-child(3) { animation-delay: 0.6s; }

    @keyframes dot-pulse-3 {
        0%, 100% { transform: scale(0.8); opacity: 0.4; }
        50% { transform: scale(1.3); opacity: 1; }
    }

    .subtitle-text {
        font-size: 16px;
        color: #8a8a9a;
        letter-spacing: 2px;
    }

    @keyframes subtitle-fade {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }

    /* ==================== CHAT MESSAGES ==================== */
    .stChatMessage {
        border-radius: 25px;
        padding: 20px 24px;
        margin: 15px 0;
        backdrop-filter: blur(15px);
        border: 1px solid transparent;
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }

    .stChatMessage::before {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: 25px;
        padding: 1px;
        background: linear-gradient(135deg, transparent, transparent);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        pointer-events: none;
    }

    [data-testid="stChatMessage-user"] {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.1) 0%, rgba(0, 200, 150, 0.06) 100%);
        border-color: rgba(0, 255, 204, 0.2);
        margin-left: 70px;
        box-shadow: 
            0 10px 40px rgba(0, 255, 204, 0.1),
            0 0 1px rgba(0, 255, 204, 0.3),
            inset 0 0 30px rgba(0, 255, 204, 0.03);
        animation: msg-in-right 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    [data-testid="stChatMessage-user"]::before {
        background: linear-gradient(135deg, rgba(0, 255, 204, 0.3), transparent, rgba(0, 255, 204, 0.1));
        animation: border-shimmer-user 3s linear infinite;
    }

    [data-testid="stChatMessage-user"]:hover {
        transform: translateX(-5px) scale(1.01);
        box-shadow: 
            0 15px 50px rgba(0, 255, 204, 0.18),
            0 0 30px rgba(0, 255, 204, 0.1);
    }

    @keyframes msg-in-right {
        0% { opacity: 0; transform: translateX(80px) scale(0.9); }
        60% { transform: translateX(-5px) scale(1.02); }
        100% { opacity: 1; transform: translateX(0) scale(1); }
    }

    @keyframes border-shimmer-user {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }

    [data-testid="stChatMessage-assistant"] {
        background: linear-gradient(135deg, rgba(255, 0, 150, 0.08) 0%, rgba(150, 0, 255, 0.05) 100%);
        border-color: rgba(255, 0, 150, 0.15);
        margin-right: 70px;
        box-shadow: 
            0 10px 40px rgba(255, 0, 150, 0.08),
            0 0 1px rgba(255, 0, 150, 0.2),
            inset 0 0 30px rgba(255, 0, 150, 0.02);
        animation: msg-in-left 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    [data-testid="stChatMessage-assistant"]::before {
        background: linear-gradient(135deg, rgba(255, 0, 150, 0.3), transparent, rgba(150, 0, 255, 0.2));
        animation: border-shimmer-assistant 3s linear infinite;
    }

    [data-testid="stChatMessage-assistant"]:hover {
        transform: translateX(5px) scale(1.01);
        box-shadow: 
            0 15px 50px rgba(255, 0, 150, 0.15),
            0 0 30px rgba(255, 0, 150, 0.08);
    }

    @keyframes msg-in-left {
        0% { opacity: 0; transform: translateX(-80px) scale(0.9); }
        60% { transform: translateX(5px) scale(1.02); }
        100% { opacity: 1; transform: translateX(0) scale(1); }
    }

    @keyframes border-shimmer-assistant {
        0% { background-position: 200% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ==================== AVATARS ==================== */
    [data-testid="stChatMessageAvatar"] {
        border-radius: 50%;
        animation: avatar-entrance 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
    }

    [data-testid="stChatMessageAvatar"]::before {
        content: '';
        position: absolute;
        inset: -6px;
        border-radius: 50%;
        background: inherit;
        filter: blur(15px);
        opacity: 0.6;
        z-index: -1;
        animation: avatar-glow 2s ease-in-out infinite;
    }

    [data-testid="stChatMessageAvatar"]::after {
        content: '';
        position: absolute;
        inset: -3px;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.3);
        animation: avatar-ring 2s ease-in-out infinite;
    }

    @keyframes avatar-entrance {
        0% { transform: scale(0) rotate(-180deg); opacity: 0; }
        60% { transform: scale(1.2) rotate(10deg); }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }

    @keyframes avatar-glow {
        0%, 100% { opacity: 0.4; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.15); }
    }

    @keyframes avatar-ring {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.2); opacity: 0; }
    }

    [data-testid="stChatMessageAvatar-user"] {
        background: linear-gradient(135deg, #00ffcc, #00d4aa, #00ffaa) !important;
        box-shadow: 
            0 0 30px rgba(0, 255, 204, 0.6),
            inset 0 0 20px rgba(255, 255, 255, 0.3),
            inset 0 -5px 15px rgba(0, 200, 150, 0.3);
    }

    [data-testid="stChatMessageAvatar-assistant"] {
        background: linear-gradient(135deg, #ff00ff, #aa00ff, #ff66ff) !important;
        box-shadow: 
            0 0 30px rgba(255, 0, 255, 0.6),
            inset 0 0 20px rgba(255, 255, 255, 0.3),
            inset 0 -5px 15px rgba(150, 0, 255, 0.3);
    }

    /* ==================== CHAT INPUT ==================== */
    .stChatInputContainer {
        padding: 15px 0 25px;
        position: relative;
        z-index: 10;
    }

    .input-wrapper {
        position: relative;
    }

    .input-glow-bg {
        position: absolute;
        inset: -3px;
        border-radius: 35px;
        background: linear-gradient(90deg, #00ffcc, #ff00ff, #00ffcc, #ff00ff);
        background-size: 300% 100%;
        animation: input-rainbow 4s linear infinite;
        opacity: 0.5;
        filter: blur(8px);
        z-index: -1;
    }

    @keyframes input-rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 200% 50%; }
    }

    .stChatInput {
        background: linear-gradient(#0a0a12, #0a0a12) padding-box,
                    linear-gradient(90deg, #00ffcc, #ff00ff, #00b8ff, #00ffcc, #ff00ff) border-box !important;
        background-size: 400% 100% !important;
        border: 2px solid transparent !important;
        border-radius: 30px !important;
        padding: 18px 28px !important;
        box-shadow: 
            0 10px 40px rgba(0, 0, 0, 0.4),
            0 0 0 1px rgba(0, 255, 204, 0.1),
            inset 0 2px 0 rgba(255, 255, 255, 0.05),
            inset 0 -2px 10px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.4s ease !important;
        animation: input-shimmer 8s linear infinite;
    }

    @keyframes input-shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 200% 50%; }
    }

    .stChatInput:focus {
        box-shadow: 
            0 20px 60px rgba(0, 255, 204, 0.3),
            0 0 50px rgba(0, 255, 204, 0.2),
            0 0 100px rgba(0, 255, 204, 0.1),
            inset 0 2px 0 rgba(255, 255, 255, 0.1) !important;
        transform: scale(1.02);
        animation: none !important;
        background: linear-gradient(#0a0a12, #0a0a12) padding-box,
                    linear-gradient(90deg, #00ffcc, #00ffaa) border-box !important;
    }

    .stChatInput input {
        color: #ffffff !important;
        font-size: 16px !important;
        letter-spacing: 0.5px;
    }

    .stChatInput input::placeholder {
        color: #00ffcc !important;
        text-shadow: 0 0 15px rgba(0, 255, 204, 0.8);
        animation: placeholder-glow 2s ease-in-out infinite;
    }

    @keyframes placeholder-glow {
        0%, 100% { 
            text-shadow: 0 0 10px rgba(0, 255, 204, 0.5); 
            opacity: 0.8;
        }
        50% { 
            text-shadow: 0 0 25px rgba(0, 255, 204, 1), 0 0 40px rgba(0, 255, 204, 0.5); 
            opacity: 1;
        }
    }

    /* ==================== SEND BUTTON ==================== */
    .send-btn-wrapper {
        position: relative;
    }

    [data-testid="stChatInputSubmitButton"] {
        background: linear-gradient(135deg, #00ffcc 0%, #00d4aa 50%, #00ffaa 100%) !important;
        background-size: 200% 200% !important;
        border-radius: 50% !important;
        width: 56px !important;
        height: 56px !important;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        box-shadow: 
            0 8px 30px rgba(0, 255, 204, 0.5),
            0 0 50px rgba(0, 255, 204, 0.2),
            inset 0 2px 0 rgba(255, 255, 255, 0.4),
            inset 0 -3px 10px rgba(0, 200, 150, 0.3) !important;
        animation: send-btn-glow 2s ease-in-out infinite, send-btn-shimmer 3s linear infinite;
        position: relative;
        overflow: visible !important;
    }

    @keyframes send-btn-glow {
        0%, 100% { 
            box-shadow: 
                0 8px 30px rgba(0, 255, 204, 0.5),
                0 0 50px rgba(0, 255, 204, 0.2),
                inset 0 2px 0 rgba(255, 255, 255, 0.4);
        }
        50% { 
            box-shadow: 
                0 8px 40px rgba(0, 255, 204, 0.7),
                0 0 70px rgba(0, 255, 204, 0.4),
                0 0 100px rgba(0, 255, 204, 0.2),
                inset 0 2px 0 rgba(255, 255, 255, 0.4);
        }
    }

    @keyframes send-btn-shimmer {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 200% 50%; }
    }

    /* Outer ring */
    [data-testid="stChatInputSubmitButton"]::before {
        content: '';
        position: absolute;
        inset: -8px;
        border-radius: 50%;
        border: 2px solid rgba(0, 255, 204, 0.4);
        animation: ring-pulse 2s ease-in-out infinite;
    }

    @keyframes ring-pulse {
        0%, 100% { transform: scale(1); opacity: 0.4; }
        50% { transform: scale(1.15); opacity: 0; }
    }

    /* Rainbow ring on hover */
    [data-testid="stChatInputSubmitButton"]::after {
        content: '';
        position: absolute;
        inset: -12px;
        border-radius: 50%;
        background: conic-gradient(from 0deg, #00ffcc, #ff00ff, #00ffcc);
        opacity: 0;
        z-index: -1;
        filter: blur(10px);
        transition: opacity 0.3s;
    }

    [data-testid="stChatInputSubmitButton"]:hover::after {
        opacity: 0.5;
        animation: rainbow-spin 2s linear infinite;
    }

    @keyframes rainbow-spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    [data-testid="stChatInputSubmitButton"]:hover {
        transform: scale(1.2) rotate(10deg) !important;
        box-shadow: 
            0 15px 50px rgba(0, 255, 204, 0.7),
            0 0 80px rgba(0, 255, 204, 0.4),
            0 0 120px rgba(0, 255, 204, 0.2),
            inset 0 2px 0 rgba(255, 255, 255, 0.5) !important;
    }

    [data-testid="stChatInputSubmitButton"]:active {
        transform: scale(0.95) !important;
        animation: none !important;
    }

    [data-testid="stChatInputSubmitButton"] svg {
        fill: #050508 !important;
        width: 24px !important;
        height: 24px !important;
        transition: transform 0.3s ease;
    }

    [data-testid="stChatInputSubmitButton"]:hover svg {
        transform: translateX(2px) scale(1.1);
    }

    /* ==================== TYPING INDICATOR ==================== */
    .typing-wrapper {
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px 25px;
        background: rgba(10, 10, 18, 0.7);
        border-radius: 25px;
        border: 1px solid rgba(0, 255, 204, 0.15);
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.3),
            0 0 30px rgba(0, 255, 204, 0.08);
        animation: typing-appear 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes typing-appear {
        0% { opacity: 0; transform: scale(0.9); }
        60% { transform: scale(1.02); }
        100% { opacity: 1; transform: scale(1); }
    }

    .typing-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00ffcc, #00d4aa);
        box-shadow: 
            0 0 15px rgba(0, 255, 204, 0.8),
            0 0 30px rgba(0, 255, 204, 0.4);
        animation: typing-bounce 1.3s ease-in-out infinite;
    }

    .typing-dot:nth-child(1) { animation-delay: 0s; }
    .typing-dot:nth-child(2) { animation-delay: 0.15s; }
    .typing-dot:nth-child(3) { animation-delay: 0.3s; }

    @keyframes typing-bounce {
        0%, 50%, 100% { 
            transform: translateY(0) scale(0.8); 
            opacity: 0.5;
        }
        25% { 
            transform: translateY(-15px) scale(1.15); 
            opacity: 1;
        }
    }

    .typing-text {
        color: #00ffcc;
        font-size: 14px;
        animation: thinking-pulse 1.5s ease-in-out infinite;
    }

    @keyframes thinking-pulse {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }

    .typing-dots {
        display: inline-flex;
        gap: 3px;
        margin-left: 3px;
    }

    .typing-dots span {
        width: 4px;
        height: 4px;
        background: #00ffcc;
        border-radius: 50%;
        animation: dot-load 1.4s ease-in-out infinite;
    }

    .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
    .typing-dots span:nth-child(3) { animation-delay: 0.4s; }

    @keyframes dot-load {
        0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
        40% { transform: scale(1); opacity: 1; }
    }

    /* ==================== CURSOR ==================== */
    .cursor-blink {
        color: #00ffcc;
        animation: cursor-blink 1s step-end infinite;
        text-shadow: 
            0 0 10px rgba(0, 255, 204, 1),
            0 0 20px rgba(0, 255, 204, 0.8),
            0 0 30px rgba(0, 255, 204, 0.5);
        font-weight: bold;
    }

    @keyframes cursor-blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }

    /* ==================== SIDEBAR ==================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #06060a 0%, #0a0a12 50%, #06060a 100%) !important;
        border-right: 1px solid rgba(0, 255, 204, 0.06) !important;
    }

    [data-testid="stSidebar"]::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 300px;
        height: 100vh;
        background: 
            radial-gradient(ellipse at 20% 15%, rgba(0, 255, 204, 0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 85%, rgba(255, 0, 255, 0.05) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(120, 0, 255, 0.03) 0%, transparent 50%);
        pointer-events: none;
        animation: sidebar-aurora 10s ease-in-out infinite;
    }

    @keyframes sidebar-aurora {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }

    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00ffcc, #ff00ff, #00ffcc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: sidebar-shimmer 3s linear infinite;
        text-align: center;
        padding: 20px 0;
        position: relative;
    }

    .sidebar-title::after {
        content: '';
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ffcc, transparent);
        animation: title-line 2s ease-in-out infinite;
    }

    @keyframes title-line {
        0%, 100% { width: 40px; opacity: 0.5; }
        50% { width: 80px; opacity: 1; }
    }

    @keyframes sidebar-shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    /* ==================== SELECT BOX ==================== */
    .stSelectbox > div > div {
        background: rgba(10, 10, 18, 0.9) !important;
        border: 1px solid rgba(0, 255, 204, 0.25) !important;
        border-radius: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: 
            0 5px 20px rgba(0, 0, 0, 0.3),
            0 0 20px rgba(0, 255, 204, 0.05) !important;
        animation: selectbox-border 3s ease-in-out infinite;
    }

    @keyframes selectbox-border {
        0%, 100% { border-color: rgba(0, 255, 204, 0.25); }
        50% { border-color: rgba(255, 0, 255, 0.35); }
    }

    .stSelectbox > div > div:hover {
        border-color: rgba(0, 255, 204, 0.6) !important;
        box-shadow: 
            0 8px 30px rgba(0, 0, 0, 0.4),
            0 0 35px rgba(0, 255, 204, 0.2) !important;
        transform: translateY(-2px);
    }

    .stSelectbox label {
        color: #00ffcc !important;
        font-weight: 600;
        font-size: 14px;
    }

    /* ==================== BUTTONS ==================== */
    .stButton > button {
        background: linear-gradient(135deg, #00ffcc 0%, #00d4aa 33%, #ff00ff 66%, #00ffcc 100%) !important;
        background-size: 300% 100% !important;
        border: none !important;
        border-radius: 16px !important;
        color: #050508 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 
            0 8px 30px rgba(0, 255, 204, 0.3),
            inset 0 2px 0 rgba(255, 255, 255, 0.3) !important;
        animation: btn-gradient 4s ease infinite;
    }

    @keyframes btn-gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 200% 50%; }
    }

    .stButton > button:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 
            0 15px 45px rgba(0, 255, 204, 0.5),
            0 0 60px rgba(0, 255, 204, 0.2),
            inset 0 2px 0 rgba(255, 255, 255, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
        animation: none !important;
    }

    .clear-btn {
        background: linear-gradient(135deg, #ff006e 0%, #ff4d94 33%, #ff00ff 66%, #ff006e 100%) !important;
    }

    .clear-btn:hover {
        box-shadow: 
            0 15px 45px rgba(255, 0, 110, 0.6),
            0 0 60px rgba(255, 0, 110, 0.3),
            inset 0 2px 0 rgba(255, 255, 255, 0.4) !important;
    }

    /* ==================== SCROLLBAR ==================== */
    ::-webkit-scrollbar {
        width: 5px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.02);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00ffcc, #00d4aa, #ff00ff);
        border-radius: 3px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #00ffaa, #00ffcc, #ff66ff);
    }

    /* ==================== MESSAGE TEXT ==================== */
    .stMarkdown p {
        font-family: 'Outfit', sans-serif;
        line-height: 1.8;
        color: #e4e4ec;
        font-size: 15px;
    }

    /* ==================== FOOTER ==================== */
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 20px;
        background: linear-gradient(180deg, transparent 0%, rgba(8, 8, 14, 0.95) 30%, #050508 100%);
        text-align: center;
        z-index: 100;
    }

    .footer-glow-line {
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(0, 255, 204, 0.4) 20%, 
            rgba(255, 0, 255, 0.3) 40%,
            rgba(0, 255, 150, 0.3) 60%,
            rgba(0, 255, 204, 0.4) 80%,
            transparent 100%);
        background-size: 200% 100%;
        margin-bottom: 18px;
        animation: footer-line-move 4s linear infinite;
    }

    @keyframes footer-line-move {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }

    .footer-content {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 18px;
        flex-wrap: wrap;
    }

    .footer-dot {
        width: 4px;
        height: 4px;
        background: #00ffcc;
        border-radius: 50%;
        animation: footer-dot-pulse 2s ease-in-out infinite;
        box-shadow: 0 0 8px rgba(0, 255, 204, 0.8);
    }

    .footer-dot:nth-child(odd) { animation-delay: 0.5s; }

    @keyframes footer-dot-pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.8); }
    }

    .footer-text {
        color: #5a5a6a;
        font-size: 12px;
        transition: all 0.3s ease;
    }

    .footer-heart {
        color: #ff006e;
        animation: heart-beat 1.5s ease-in-out infinite;
        display: inline-block;
        text-shadow: 0 0 10px rgba(255, 0, 110, 0.5);
    }

    @keyframes heart-beat {
        0%, 100% { transform: scale(1); }
        15% { transform: scale(1.4); }
        30% { transform: scale(1); }
        45% { transform: scale(1.25); }
    }

    .footer-link {
        color: #00ffcc;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }

    .footer-link:hover {
        text-shadow: 
            0 0 20px rgba(0, 255, 204, 0.8),
            0 0 40px rgba(0, 255, 204, 0.4);
        transform: scale(1.1);
    }

    /* ==================== DIVIDER ==================== */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(0, 255, 204, 0.2) 30%, 
            rgba(255, 0, 255, 0.15) 50%,
            rgba(0, 255, 204, 0.2) 70%,
            transparent);
        margin: 20px 0;
    }

    /* ==================== MODEL LABEL ==================== */
    .model-label {
        color: #00ffcc !important;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 10px;
        display: block;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
    }
    </style>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new MutationObserver(function(mutations) {
            const sendBtn = document.querySelector('[data-testid="stChatInputSubmitButton"]');
            if (sendBtn && !sendBtn.dataset.animated) {
                sendBtn.dataset.animated = 'true';

                sendBtn.addEventListener('click', function(e) {
                    const ripple = document.createElement('span');
                    ripple.style.cssText = `
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        width: 100px;
                        height: 100px;
                        background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, transparent 70%);
                        border-radius: 50%;
                        animation: ripple-effect 0.6s ease-out forwards;
                        pointer-events: none;
                    `;
                    this.appendChild(ripple);
                    setTimeout(() => ripple.remove(), 600);
                });
            }
        });

        observer.observe(document.body, { childList: true, subtree: true });
    });

    const style = document.createElement('style');
    style.textContent = `
        @keyframes ripple-effect {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(2); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
    </script>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-wrapper">
        <h1 class="main-title">
            <span class="title-text">Umar AI</span>
        </h1>
        <div class="subtitle-wrapper">
            <span class="subtitle-dot"></span>
            <span class="subtitle-dot"></span>
            <span class="subtitle-dot"></span>
            <span class="subtitle-text">Your Intelligent Assistant</span>
            <span class="subtitle-dot"></span>
            <span class="subtitle-dot"></span>
            <span class="subtitle-dot"></span>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<h2 class="sidebar-title">⚙️ Settings</h2>', unsafe_allow_html=True)

    st.markdown('<span class="model-label">🧠 Choose AI Model</span>', unsafe_allow_html=True)
    model_option = st.selectbox(
        "AI Model",
        ("llama-3.3-70b-versatile", "gemma2-9b-it", "llama-3.1-8b-instant", "mixtral-8x7b-32768",
         "deepseek-r1-distill-llama-70b"),
        index=0
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat History", key="clear"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("""
        <div style="text-align: center; padding: 25px 0; opacity: 0.8;">
            <p style="color: #5a5a6a; font-size: 12px; animation: fade-pulse 3s ease-in-out infinite;">
                ⚡ Powered by Groq API
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        padding: 20px 0;
    }
    .chat-bubble {
        max-width: 80%;
        padding: 18px 24px;
        border-radius: 20px;
        position: relative;
        animation: bubble-pop 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        transform-origin: center;
    }
    @keyframes bubble-pop {
        0% { transform: scale(0) rotate(-10deg); opacity: 0; }
        70% { transform: scale(1.1) rotate(3deg); }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    .chat-bubble.user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        align-self: flex-end;
        border-bottom-right-radius: 5px;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4), inset 0 1px 0 rgba(255,255,255,0.2);
    }
    .chat-bubble.assistant {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        align-self: flex-start;
        border-bottom-left-radius: 5px;
        border: 1px solid rgba(0, 255, 204, 0.3);
        box-shadow: 0 10px 40px rgba(0, 255, 204, 0.15), inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .chat-bubble::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: inherit;
        background: linear-gradient(45deg, transparent 40%, rgba(255,255,255,0.1) 50%, transparent 60%);
        background-size: 200% 200%;
        animation: shimmer 3s infinite;
    }
    @keyframes shimmer {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    .chat-bubble .avatar {
        position: absolute;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        animation: avatar-float 3s ease-in-out infinite;
    }
    .chat-bubble.user .avatar {
        right: -48px;
        top: 50%;
        transform: translateY(-50%);
        background: linear-gradient(135deg, #667eea, #764ba2);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
    }
    .chat-bubble.assistant .avatar {
        left: -48px;
        top: 50%;
        transform: translateY(-50%);
        background: linear-gradient(135deg, #00ffcc, #00ff88);
        box-shadow: 0 4px 15px rgba(0, 255, 204, 0.5);
    }
    @keyframes avatar-float {
        0%, 100% { transform: translateY(-50%) translateX(0); }
        50% { transform: translateY(-55%) translateX(3px); }
    }
    .chat-bubble .content {
        position: relative;
        z-index: 1;
        color: #fff;
        line-height: 1.6;
        word-wrap: break-word;
    }
    .chat-bubble.user .content {
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    .typing-3d {
        display: flex;
        gap: 8px;
        padding: 20px;
    }
    .typing-3d .dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        animation: dot-bounce 1.4s ease-in-out infinite both;
    }
    .typing-3d .dot:nth-child(1) { background: #00ffcc; animation-delay: -0.32s; box-shadow: 0 0 10px #00ffcc; }
    .typing-3d .dot:nth-child(2) { background: #00ff88; animation-delay: -0.16s; box-shadow: 0 0 10px #00ff88; }
    .typing-3d .dot:nth-child(3) { background: #ff00ff; animation-delay: 0s; box-shadow: 0 0 10px #ff00ff; }
    @keyframes dot-bounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1); }
    }
    </style>
    <div class="chat-container">
""", unsafe_allow_html=True)

for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    bubble_class = "user" if message["role"] == "user" else "assistant"
    st.markdown(f"""
        <div class="chat-bubble {bubble_class}">
            <div class="avatar">{avatar}</div>
            <div class="content">{message["content"]}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

if prompt := st.chat_input("💬 Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.markdown(f"""
        <div class="chat-container">
            <div class="chat-bubble user">
                <div class="avatar">👤</div>
                <div class="content">{prompt}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    message_placeholder = st.empty()
    message_placeholder.markdown("""
        <div class="typing-3d">
            <div class="dot"></div>
            <div class="dot"></div>
            <div class="dot"></div>
        </div>
    """, unsafe_allow_html=True)

    full_response = ""

    try:
        completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        for chunk in completion:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + '<span class="cursor-blink">▊</span>',
                                             unsafe_allow_html=True)
                time.sleep(0.01)

        message_placeholder.markdown(full_response, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Error: {e}")
        full_response = "Sorry, I encountered an error. Please try again."

    if full_response:
        st.markdown(f"""
            <div class="chat-container">
                <div class="chat-bubble assistant">
                    <div class="avatar">🤖</div>
                    <div class="content">{full_response}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("""
    <div class="custom-footer">
        <div class="footer-glow-line"></div>
        <div class="footer-content">
            <span class="footer-dot"></span>
            <span class="footer-text">Made with <span class="footer-heart">❤</span> by <strong>Umar</strong></span>
            <span class="footer-dot"></span>
            <a href="#" class="footer-link">Umar AI v1.0</a>
            <span class="footer-dot"></span>
            <span class="footer-text">⚡ Powered by Groq</span>
            <span class="footer-dot"></span>
        </div>
    </div>
""", unsafe_allow_html=True)
