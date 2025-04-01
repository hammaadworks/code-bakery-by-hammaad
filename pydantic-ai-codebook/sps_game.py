from dataclasses import dataclass
from pprint import pprint
import random
from constants import get_ollama_agent
from pydantic_ai import RunContext, Tool, Agent


@dataclass
class Player:
    name: str


def ai_choice() -> str:
    """choose one among stone, paper, scissor.

    Args: None

    Returns:
    str: One among "stone", "paper", "scissor".
    """
    return random.choice(["stone", "paper", "scissor"])


def get_player_name(ctx: RunContext[Player]) -> str:
    """Get the player's name.

    Args: None

    Returns:
    str: The player's name."""
    return ctx.deps.name


agent: Agent[None, str] = get_ollama_agent(
    deps_type=Player,
    result_type=str,
    system_prompt=(
        """Play stone, paper and scissors game with the user. 
        Steps:
        1. Get users name and use ai_choice to choose.
        2. Decide who won based on the following rules.
            a. Same choice draw.
            b. Stone beats Scissors.
            c. Paper beats Stone.
            d. Scissors beats Paper.
        3. Say a joke if user wins.
        4. Taunt the user if AI wins.
        Note:
        1. Display player name, your choice and result. 
        2. You must follow the rules, never deviate from the rules."""
    ),
    tools=[Tool(ai_choice, takes_ctx=False), Tool(get_player_name, takes_ctx=True)],
)


toss_result = agent.run_sync("I choose paper, bro", deps=Player(name="hammaad"))
print(toss_result.data, end="\n\n")

pprint(toss_result.all_messages())
# > Congratulations Anne, you guessed correctly! You're a winner!
