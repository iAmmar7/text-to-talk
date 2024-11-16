# text-to-talk

**Text-to-Talk** is a FastAPI application providing APIs for text summarization and text-to-speech conversion. It utilizes pre-trained models from Hugging Face's Transformers library and the Bark model for TTS.

## Features

- Summarize text using the BART model.
- Convert text to speech using the Bark model.
- Combine text summarization and text-to-speech into one endpoint.

- Summarize your text
- Convert your text into speech
- Get the text summary in audio

## Installation and Setup

Follow these steps to set up and run the application:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/iAmmar7/text-to-talk.git
```

### 2. Navigate to the Project Directory

```bash
cd text-to-talk
```

### 3. Set Up a Virtual Environment

```bash
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

### 6. Access the API

Once the application is running, you can access the API documentation at:

Swagger UI: <http://127.0.0.1:8000/docs>
ReDoc: <http://127.0.0.1:8000/redoc>
