📘 Translation Orchestrator Agent (Gemini + Agents SDK) 🚀 Overview

Ye project ek Agentic AI Orchestrator hai jo Google Gemini (free API key) ko use karta hai aur multiple language translation agents ko manage karta hai:

Arabic Agent

French Agent

Italian Agent

Triage Agent (translation orchestrator)

Agents SDK (agents) ka use karke humne ek multi-agent workflow banaya hai jisme orchestrator agent user ke request ko samajhta hai aur correct translation tool ko call karta hai.

🔑 Setup

Clone Project git clone https://github.com/your-repo/translation-orchestrator.git cd translation-orchestrator

Create Virtual Environment python -m venv .venv .venv\Scripts\activate # Windows

or
source .venv/bin/activate # Linux/Mac

Install Dependencies pip install -r requirements.txt
requirements.txt me yeh dependencies hongi:

agents openai google-generativeai python-dotenv

Set Environment Variables
.env file project ke root me banao:

GEMINI_API_KEY=your_free_gemini_api_key_here

👉 Free API key Google AI Studio se lo: https://aistudio.google.com/apikey

▶️ Run Example python main.py

Expected output:

✅ Final Output: Arabic: مرحبا French: Bonjour

🛠 How It Works User Request → Triage Agent → Correct Translation Tool → Gemini Model → Final Output

Triage Agent: User ke prompt ko samajhta hai aur decide karta hai kaunsa translation agent use karna hai.

Language Agents: Arabic, French, Italian translation ke liye specialized agents.

Gemini (1.5 Flash): Fast & cost-efficient model jo free API tier me available hai.

🌍 Extend to More Languages

Naye agents add karna easy hai. Example:

german_agent = Agent( name="German Agent", instructions="Translate the user's message to German.", model=model, )

triage_agent.tools.append( german_agent.as_tool("translate_to_german", "Translate to German") )

⚠️ Notes

Free Gemini API key ke sath rate limits hote hain (requests/minute).

gemini-1.5-flash free tier ke liye best hai (fast aur lightweight).

Agar production use karna hai, toh gemini-1.5-pro use kar sakte ho (zyada accurate, lekin quota limited hai).
