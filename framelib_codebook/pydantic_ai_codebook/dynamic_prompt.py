from datetime import date
from constants import get_ollama_agent
from pydantic_ai import RunContext

agent = get_ollama_agent(system_prompt="Use the customer's name while replying to them.")

@agent.system_prompt  
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.system_prompt
def add_the_date() -> str:  
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Alhamdulillah')
print(result.data)
#> Hello Frank, the date today is 2032-01-02.