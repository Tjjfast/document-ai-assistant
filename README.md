# Document AI Assistant
## This project demonstrates a conversational AI assistant built using the Agno framework. The agent uses Google Gemini for language understanding and performs semantic search over a PDF document using LanceDB. All chat sessions are stored locally using SQLite.

---

### Features

- Loads and embeds PDFs from URLs (Thai recipe PDF by default)
- Vector search using LanceDB + Gemini Embeddings
- Gemini LLM (gemini-1.5-flash) responds only using document data
- Persistent chat history stored in SQLite
- Markdown formatting and tool visibility enabled

---

## Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/Tjjfast/document-ai-assistant
cd document-ai-assistant
```
### 2. Create .env File
Create a file named .env in the root directory and add your Gemini API key:
```
GOOGLE_API_KEY="exampleAPIkey"
```
Do not share your API key publicly.
### 3. Install Requirements
```
pip install -r requirements.txt
```
### 4. Run the Agent
```
python agent.py
```
The agent will launch a terminal chat where you can ask questions based on the Thai Recipes PDF.

### Example Prompt :
```
How do I make Thai green curry?
```
The agent will search the PDF and answer only using its embedded knowledge.

### Project Structure :
```
📁 document-ai-assistant/
├── agent.py              # Main agent logic
├── knowledgebase.py      # Loads and embeds the PDF into LanceDB
├── agent.db              # SQLite DB for chat history (auto-created)
├── .env                  # API key
├── requirements.txt      # Dependencies
└── README.md             # This file
```
### Demo Video :
Watch the demo video [here](https://drive.google.com/file/d/14wySShbcZVO-UGQ_--m-e0WNU1mD0Sp8/view?usp=sharing)
