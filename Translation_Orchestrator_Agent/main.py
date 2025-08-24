import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("⚠️ GEMINI_API_KEY not set. Get free from https://aistudio.google.com/apikey")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",   
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


arabic_agent = Agent(
    name="Arabic Agent",
    instructions="Translate the user's message to Arabic.",
    model=model,
)

french_agent = Agent(
    name="French Agent",
    instructions="Translate the user's message to French.",
    model=model,
)

italian_agent = Agent(
    name="Italian Agent",
    instructions="Translate the user's message to Italian.",
    model=model,
)

# Orchestrator agent
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a translation orchestrator. "
        "If asked for a translation, always use the correct tool. "
        "Never translate directly."
    ),
    tools=[
        arabic_agent.as_tool("translate_to_arabic", "Translate to Arabic"),
        french_agent.as_tool("translate_to_french", "Translate to French"),
        italian_agent.as_tool("translate_to_italian", "Translate to Italian"),
    ],
    model=model,
)

result = Runner.run_sync(
    triage_agent,
    "Translate 'Hello' into Arabic and French and italian.",
    run_config=config,
)


print(result.final_output)
