import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from schema import PersonInfo  # Importing your schema

def build_extractor_chain():
    # 1. Initialize Model
    # It's best to keep temperature at 0 for data extraction tasks
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # 2. Setup Parser
    parser = JsonOutputParser(pydantic_object=PersonInfo)

    # 3. Create Prompt with format instructions
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert data extractor. Extract the following information from the provided text. \n{format_instructions}"),
        ("human", "{input_text}")
    ]).partial(format_instructions=parser.get_format_instructions())

    # 4. Construct Chain (LCEL)
    return prompt | model | parser

def extract_data(text: str):
    chain = build_extractor_chain()
    try:
        # Invoke the chain
        result = chain.invoke({"input_text": text})
        
        # Validation: Verify the output is valid JSON and print
        print("--- Extraction Result ---")
        print(json.dumps(result, indent=4))
        return result
    except Exception as e:
        print(f"Failed to parse output: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    raw_text = """
    My name is Alaa, a student at the Faculty of Engineering. 
    I'm 21 years old. Reach me at alaa.dev@example.com.
    """
    extract_data(raw_text)