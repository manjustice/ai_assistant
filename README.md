## AI Assistant
This is a python AI assistant that use ChatGPT API


## Installation

Python must be already installed

```shell
git clone https://github.com/manjustice/ai_assistant.git
cd ai_assistant
python -m venv venv
source venv/bin/activate (on Linux/maOS)
venv\Scripts\activate (on Windows)
pip install -r requirements.txt
copy .env.sample -> .env and populate with all required data
uvicorn app.main:app --reload
```
To access the application, follow this link: http://localhost:8000
