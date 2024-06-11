from groq import Groq
import os
import time
# import openai


class Agent:
    def __init__(self, content):
        self.content = content
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.messages = [
        {
            "role": "system",
            "content": self.content
        },
        # {
        #     "role": "assistant",
        #     "content": "Hello! I'm reaching out from [Your Real Estate Company]. We've got some exciting new listings in your area that offer great amenities at competitive prices. Are you currently interested in exploring new home options?"
        # }
        ]

    def chat(self, user_input):

        self.messages.append({
            "role": "user",
            "content": user_input
        })

        # Send the updated conversation to the API
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="llama3-70b-8192",
        )

        # Retrieve the response from the bot and print it
        bot_response = chat_completion.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": bot_response
        })
        # self.messages.append({
        #     "role": "system",
        #     "content": self.content
        # })

        return bot_response
    
class Optimizer:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def optimize_prompts(self, andrew_content, jamie_content, conversation_logs):
        prompt = (
            f"Analyze the following conversation logs and improve "
            f"both agents' prompts. Output only the new prompts and nothing else Here are the current prompts:\n\n"
            f"Andrew's prompt:\n{andrew_content}\n\n"
            f"Jamie's prompt:\n{jamie_content}\n\n"
            f"Conversation logs:\n{conversation_logs}"
        )
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "system", "content": prompt}], model="llama3-70b-8192"
        )
        return chat_completion.choices[0].message.content
        
    
