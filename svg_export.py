# svg_export.py

import re

_SVG_FENCE_RE = re.compile(r"^```(?:svg|xml)?\s*\n?(.*?)\n?```$", re.DOTALL)


def _strip_markdown_fence(llm_response: str) -> str:
    """Rimuove gli eventuali delimitatori markdown (```svg ... ```) attorno al codice SVG."""
    text = llm_response.strip()
    match = _SVG_FENCE_RE.match(text)
    return match.group(1).strip() if match else text


def save_svg_response(llm_response: str, filepath: str) -> None:
    """Salva la risposta del modello come file SVG, ripulita da eventuali fence markdown."""
    svg_content = _strip_markdown_fence(llm_response)
    if "</svg>" not in svg_content:
        raise ValueError(
            "Risposta SVG incompleta o troncata: manca il tag di chiusura </svg>."
        )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)


def generate_and_save(prompt: str, filepath: str, model_call) -> str:
    """Chiama il modello per generare un componente SVG e lo salva su file."""
    response = model_call(prompt, max_tokens=4000)
    save_svg_response(response, filepath)
    return response
