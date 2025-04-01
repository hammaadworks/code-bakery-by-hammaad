from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel


def get_ollama_agent(**kwargs):
    return Agent(OllamaModel(model_name="mistral"), **kwargs, retries=3)
