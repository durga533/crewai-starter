from crewai import Agent, Task, Crew, Process, LLM
import os 

from dotenv import load_dotenv

load_dotenv()

LLM = LLM(model="gemini/gemini-2.0-flash", api_key= os.getenv("GOOGLE_API_KEY"))

#agent definition

post_generator = Agent(
    name = "Post Generator",
    role = "Technical Content creator ",
    goal = "Generate a LinkedIn post with hash tags with simple language like humans",
    backstory="You are en experienced professional who is good at writing your thoughts on LinkedIn",
    llm= LLM
)

#initializing task

task = Task(
    
            agent = post_generator,
            name = "Post Generation",
            description = "Generate a post on Agentic AI and its benefits",
            expected_output= " Clean and readable human post"
)

#crew invocation
crew = Crew(
    
            agents= [post_generator],
            tasks= [task]
)

print(crew.kickoff())