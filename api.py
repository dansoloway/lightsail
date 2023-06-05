from fastapi import FastAPI

app = FastAPI()

@app.get("/process_string/")
def process_string(input_string: str):
    # Perform string processing or any desired operations here
    processed_string = input_string.upper()  # Example: Convert input string to uppercase
    
    return {"processed_string": processed_string}