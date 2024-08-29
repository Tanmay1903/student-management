from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os 
import json
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0.9)

# Prompt template
prompt = PromptTemplate(
    input_variables=["instruction"],
    template="""
    You are an assistant that helps manage student data. Your job is to interpret the instructions provided by the professor and return the intent of the instruction along with relevant entities in JSON format.

    Here is how you should structure your response:
    {{
        "intent": "<Intent>",
        "entities": {{
            "name": "<Student Name>",
            "id": "<Student ID>",
            "subject": "<Subject>",
            "score": "<Score>"
        }}
    }}

    If a specific entity is not mentioned in the instruction, you can omit it from the JSON.

    Also, join the intent with underscore and all in lowercase, e.g. "add_student", "add_score", "get_subject", "summarize_scores"

    Example:
    {{
        intent: "add_student",
        entities: {{
            "name": "John",
            "id": 123
        }}
    }}

    Instruction: {instruction}

    Respond with the intent and entities in the exact JSON format as described above.
    """
)

    
# Create an LLMChain with the prompt
chain = LLMChain(llm=llm, prompt=prompt)

def process_instruction(instruction: str) -> dict:
    """
    Process the professor's instruction and extract intent and entities.
    """
    try:
        # Pass the instruction as a dictionary with the key "instruction"
        response = chain.run({"instruction": instruction})

        # Attempt to parse the response as JSON
        result = json.loads(response.strip())
        
        # Check if 'entities' is already a dict
        entities = result.get('entities')
        if isinstance(entities, str):
            entities = json.loads(entities)  # Parse if it's a JSON string

        result['entities'] = entities
        print(result, "result")
        return result

    except json.JSONDecodeError:
        # Fallback: Handle non-JSON responses gracefully
        return {"error": "Failed to parse the response as JSON."}

    except Exception as e:
        return {"error": str(e)}
