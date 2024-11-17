# text-to-talk

**Text-to-Talk** is a FastAPI application providing APIs for text summarization and text-to-speech conversion. It utilizes pre-trained models from Hugging Face's Transformers library using the Facebook's BART and the Suno Bark model for TTS.

## Features

- Summarize text using the BART model.
- Convert text to speech using the Bark model.
- Combine text summarization and text-to-speech into one endpoint.

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- **Node.js** (for the client)
- **Python 3.9+** (for the server)
- **Git** (for cloning the repository)

Follow these steps to set up and run the application:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/iAmmar7/text-to-talk.git
cd text-to-talk
```

### 2. Server (Backend)

#### Navigate to the Server Directory

```bash
cd server
```

#### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

#### Install Server Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Server

```bash
uvicorn app.main:app --reload
```

The server will be available at <http://localhost:8000>

#### Access the API

Once the application is running, you can access the API documentation at:

Swagger UI: <http://127.0.0.1:8000/docs>
ReDoc: <http://127.0.0.1:8000/redoc>

### 3. Client (Frontend)

#### Navigate to the Client Directory

```bash
cd client
```

#### Install Client Dependencies

```bash
npm install
```

#### Run the client

```bash
npm run dev
```

The client will be available at <http://localhost:5173>.

## Usage

1. Start the backend server first.
2. Start the frontend client.
3. Open <http://localhost:5173> in your browser to interact with the application.
