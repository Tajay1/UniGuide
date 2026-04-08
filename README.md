# UniGuide
# UniGuide AI

A simple AI assistant for universities in Jamaica.

## Overview

UniGuide AI is a Streamlit-based web application that helps students in Jamaica find information about universities, including admissions, programs, and general guidance. It provides a clean chat interface where users can ask questions and receive responses powered by an AI backend.

## Backend

This application uses a backend AI service powered by AnythingLLM (running via Docker). The backend handles all AI processing and returns responses to the Streamlit frontend.

The backend setup requires:
- AnythingLLM running locally using Docker
- A valid API key from AnythingLLM
- A configured workspace (e.g. "uniguild")
- Base URL (e.g. http://localhost:3001)

All communication with the backend is handled in `anythingllm_client.py`, which sends user messages to the AnythingLLM API and returns AI-generated responses.

## How to Run

1. Make sure you have Python installed  
2. Install dependencies:


## Features

- Home: Overview of the application  
- Chat: Ask questions about Jamaican universities (powered by AI backend)  
- About: Information about the project  

## Important Note

This application is not fully offline. It requires an active connection to the AnythingLLM backend service to generate responses. Without the backend running, the chat feature will not work.
