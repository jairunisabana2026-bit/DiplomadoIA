import os
import warnings
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

warnings.filterwarnings("ignore")

# 🔐 Cargar variables desde .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")

# 🤖 Modelo OpenRouter
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    model_name="openai/gpt-oss-20b:free",
    temperature=0.7,
)

Meta_prompt = """
Tus instrucciones aquí.
"""

print("💬 Chat sin memoria (escribe 'salir' para terminar)\n")

while True:
    user_input = input("👤 Tú: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break

    try:
        prompt = f"""
{Meta_prompt}

Usuario:
{user_input}
"""

        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        print(f"🤖 Bot: {response.content.strip()}\n")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Error: {e}\n")