import os
from groq import Groq
# import openai
from agent import Agent, Optimizer
from utils import parse_prompts


def flow():
    conversation_log = ""
    state = 'INITIAL'
    while True:
        if state == 'INITIAL':
            pass
        elif state == 'ASK_REASON':
            pass
        elif state == 'CONNECT':
            break
        elif state == 'UNCLEAR':
            pass
