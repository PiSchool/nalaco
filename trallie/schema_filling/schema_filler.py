from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=GROQ_API_KEY,
)

def fill_schema(schema, record, system_prompt, model="llama-3.3-70b-versatile"):
    """
    Generate a schema based on the provided description and records.

    Args:
        description (str): A description of the data collection.
        record (str): A record to infer the schema from.
        system_prompt (str): The system prompt to guide the schema generation.
        model (str, optional): The model to use for the chat completion. Defaults to "llama-3.1-70b-versatile".

    Returns:
        str: The extracted attribute in JSON format as generated by the model.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"""
                Following is the record: {record} and the 
                attribute schema for extraction: {schema}
                Provide the extracted attributes.
                Avoid any words at the beginning and end.
                """
            }
        ],
        model=model,
        seed=2456
    )
    return chat_completion.choices[0].message.content

