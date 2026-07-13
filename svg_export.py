# svg_export.py

def save_svg_response(llm_response: str, filepath: str) -> None:
    """Salva la risposta grezza del modello come file SVG."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(llm_response)


def generate_and_save(prompt: str, filepath: str, model_call) -> str:
    """Chiama il modello per generare un componente SVG e lo salva su file."""
    response = model_call(prompt, max_tokens=800)
    save_svg_response(response, filepath)
    return response
