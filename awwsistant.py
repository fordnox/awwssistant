import time
import json
import logging
from openai import OpenAI
from functions import Functions

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# https://platform.openai.com/docs/assistants/tools/defining-functions
class Awwsistant:

    def __init__(self):
        self.id = None
        self.assistant = None
        self.client = OpenAI()

    # When the AI uses a function, this method will send the output to the run
    def run_action(self, run):
        tool_outputs = []
        for tool_call in run.required_action.submit_tool_outputs.tool_calls:
            tool_call_id = tool_call.id
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            logging.info(f'Assistant requested {name}({arguments})')
            output = getattr(Functions, name)(**arguments)
            tool_outputs.append({"tool_call_id": tool_call_id, "output": json.dumps(output)})
            logging.debug(f'Returning {output}')
        self.client.beta.threads.runs.submit_tool_outputs(thread_id=run.thread_id,
                                                          run_id=run.id,
                                                          tool_outputs=tool_outputs)

    def chat(self, message):
        if self.assistant is None:
            raise Exception("No assistant set")
        assistant = self.assistant
        thread = self.client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ]
        )
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        while run.status != 'completed':
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run.status == 'requires_action':
                self.run_action(run)
            elif run.status == "failed":
                logger.error(f"The run failed... API probably down again...")
                break

            logger.info("Run status: %s", run.status)
            time.sleep(3)

        self.client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        thread_messages = self.client.beta.threads.messages.list(thread_id=thread.id, order="asc")
        for m in thread_messages:
            logger.warning("message: %s", m.content[0].text.value)
        return thread_messages.data[1].content[0].text.value

    def refresh_assistant(self):
        if self.id is None:
            raise Exception("No assistant id set")
        assistant = self.client.beta.assistants.retrieve(self.id)
        self.assistant = assistant
        return assistant

    def get_assistant(self, assistant_id):
        return self.client.beta.assistants.retrieve(assistant_id)

    def get_assistants(self, prompt, **kwargs):
        my_assistants = self.client.beta.assistants.list(
            order="desc",
            limit="20",
        )
        return my_assistants

    def create_assistant(self):
        assistant = self.client.beta.assistants.create(
            model="gpt-4-1106-preview",
            name="API Ninja",
            instructions="""
            As an advanced chatbot Assistant, your primary goal is to assist users to the best of your ability. 
            This may involve answering questions, providing helpful information, or completing tasks based on user input. 
            In order to effectively assist users, it is important to be detailed and thorough in your responses. 
            Use examples and evidence to support your points and justify your recommendations or solutions. 
            Remember to always prioritize the needs and satisfaction of the user. 
            Your ultimate goal is to provide a helpful and enjoyable experience for the user.
            When asked about a topic related to the functions - always ask functions for help.
            """,
            tools=[
                {"type": "function", "function": Functions.get_iban_info_JSON},
                {"type": "function", "function": Functions.get_quote_JSON},
                {"type": "function", "function": Functions.get_whois_info_JSON},
                {"type": "function", "function": Functions.get_vin_info_JSON},
            ],
        )
        logging.info("new assistant id: %s", assistant.id)
        self.assistant = assistant
        self.id = assistant.id
        return assistant
