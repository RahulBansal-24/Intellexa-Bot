# Intellexa Bot 🤖

✨ **Intellexa Bot** is an AI-powered, agentic customer support assistant built using **LangGraph**, **LangChain**, and **Groq** models.  
🤖 It classifies user issues into **Billing**, **Technical**, or **Feedback** and routes them to specialized agents.  
🧩 The project is **modular**, **extendable**, and easily deployable using **FastAPI** ⚡ and **Render** ☁️.


------------------------------------------------------------------------

## 📁 Project Structure

    Intellexa-Bot/
    ├── agents/
    │   ├── billing.py          # Billing issue handler agent
    │   ├── feedback.py         # Feedback processing agent
    │   ├── interface.py        # Router / interface logic
    │   ├── technical.py        # Technical issue handler agent
    │
    ├── chatbot/
    │   ├── bot.ipynb           # Basic chatbot prototype
    │   ├── botwithtools.ipynb  # Extended bot with tools (Tavily, memory, etc.)
    │   ├── customerbot.ipynb   # Main architecture: routing Billing/Technical/Feedback
    │
    ├── graph.py                # LangGraph workflow for issue routing
    ├── main.py                 # FastAPI server integrating all agents
    ├── requirements.txt        # Project dependencies
    ├── .gitignore
    ├── README.md
    └── .env (sample)           # Environment variables (API keys)

------------------------------------------------------------------------

## ⭐ Features

-   🔎 **Issue Classification**\
    Automatically detects whether a message is Billing, Technical, or
    Feedback.

-   🤖 **Agent-Based Architecture**\
    Each issue type has a dedicated agent in the `agents/` folder.

-   🔗 **LangGraph Workflow**\
    Graph-based flow for better state management and control.

-   🌐 **External Search Tools**\
    Integrated **Tavily search** and can be extended with custom tools.

-   🚀 **FastAPI Backend**\
    Exposes APIs to interact with the chatbot programmatically.

-   🧠 **Memory Support**\
    Implemented in `botwithtools.ipynb` using `MemorySaver`.

-   🧪 **Multiple Bot Versions**\
    Includes simple, intermediate, and advanced bot implementations in
    Jupyter notebooks.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python 3**
-   **LangChain**
-   **LangGraph**
-   **Groq API**
-   **Tavily Search API**
-   **FastAPI**
-   **Uvicorn**
-   **Jupyter Notebook**

------------------------------------------------------------------------

## 📦 Installation & Setup

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/RahulBansal-24/Intellexa-Bot.git
cd Intellexa-Bot
```

### 2️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Create your `.env` file

    groq_api_key=your_api_key_here
    tavily_api_key=your_api_key_here

------------------------------------------------------------------------

## 🚀 Running the Project Locally

### Start FastAPI server

``` bash
uvicorn main:app --reload
```

Server runs at:\
👉 http://127.0.0.1:8000

------------------------------------------------------------------------

## 🌐 Deployment on Render

### 1️⃣ Create a new Render Web Service

-   Connect your GitHub repo\
-   Select **Python** environment\
-   Add build command:

```
    pip install -r requirements.txt
```

-   Add start command:


```
    uvicorn main:app --host 0.0.0.0 --port $PORT
```
### 2️⃣ Add environment variables in Render Dashboard

    groq_api_key=your_key
    tavily_api_key=your_key

### 3️⃣ Deploy

Render will start the FastAPI app and give you a public URL.

------------------------------------------------------------------------

## ⚙️ Render Configuration Notes

-   Runtime: **Python 3.11+ recommended**
-   Ports: Must expose the dynamically assigned port from Render (`$PORT`)
-   Set **root directory** to project root
-   Ensure `.env` vars are added in Render → Environment section
-   Auto deploy on commit can be enabled

------------------------------------------------------------------------

## 🧪 Testing

You can test your API using tools like:

-   **Thunder Client (VSCode)**
-   **Postman**
-   **curl**
-   FastAPI's interactive docs at:

```
    http://127.0.0.1:8000/docs
```

Example request:

``` json
{
  "messages": "I was charged twice for my bill"
}
```

------------------------------------------------------------------------

## 🔮 Future Improvements

-   💻 **Frontend Web UI** (React or Next.js)
-   🧠 **Better memory management**
-   🛠️ **More agent types** (Shipping, Orders, General Queries)
-   🧩 **Vector database integration**
-   🎨 **Dashboard to monitor user queries**
-   👤 **User authentication system**
-   🪄 **Multi-turn tool-use agent**

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **GNU General Public License
(GPL)**.\
You may modify and distribute it under GPL terms.

------------------------------------------------------------------------

## 👤 Author

**Rahul Bansal**  
💻 A driven developer with a strong passion for building intelligent systems and exploring diverse areas of **Computer Science**.  
🌱 Continuously growing through practical projects, experimentation, and contributing meaningful work to the tech community.

📬 **GitHub:** [RahulBansal-24](https://github.com/RahulBansal-24)  
🔗 **LinkedIn:** [Rahul Bansal](https://www.linkedin.com/in/itsrahulbansal24)


------------------------------------------------------------------------
