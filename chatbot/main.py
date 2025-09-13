from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

#defining the five different  personalities
Personalities = {
    "1": ("Sherlock Holmes", "You are Sherlock Holmes. You explain things with deduction, logic, and precision."),
    "2": ("Yoda", "You are Jedi Master Yoda. Speak in short, wise, inverted sentences."),
    "3": ("Gandalf", "You are Gandalf the Grey. You explain concepts as if guiding a fellowship on a great quest."),
    "4": ("Tony Stark", "You are Tony Stark. You reply with wit, sarcasm, and a tech genius flair."),
    "5": ("Wonderland Guide", "You are a guide in Alice's Wonderland. You explain everything with whimsical, curious metaphors.")
}


def choose_personality():
    print("\n Choose your chatbot personality:")
    for key, (name, _) in Personalities.items():
        print(f"{key}. {name}")
    choice = input("\nEnter the number of your choice: ").strip()
    return Personalities.get(choice, Personalities["1"]) 

def chat_using_gpt(prompt, system_prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    name, system_prompt = choose_personality()
    print(f"\n {name}  Type 'quit', 'exit', or 'bye' to leave.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print(f"\n {name} Chatbot: Farewell! ")
        response = chat_using_gpt(user_input, system_prompt)
        print(f" {name} Chatbot:", response)
