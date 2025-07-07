from agents import Agent, Runner, function_tool
from main import config
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(city: str) -> str:
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
    data = response.json()
    return f"The current weather in {city} is {data['current']['temp_c']}℃ with {data['current']['condition']['text']}"

agent = Agent(
    name='An Agent',
    instructions="You Are A HelpFull Assistant. Your task is a help the user with their queries.",
    tools=[get_weather]
)

result = Runner.run_sync(agent,
                         'what is weather in karachi today?',
                        run_config=config)

print(result.final_output)

#ye sirf porani chezen batata hai. real time data nhi batata or personal data bhi nhi batata
