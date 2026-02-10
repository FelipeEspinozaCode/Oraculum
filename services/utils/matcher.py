import unicodedata

def normalize_text(text: str) -> str:
    """Elimina tildes, convierte a minusculas y limpia espacios."""
    if not text:
        return ""
    text = text.lower().strip()
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    return text

def symbolic_match(user_input: str, targets: list) -> str:
    """Busca si alguno de los nombres de la DB está presente en la entrada del motor."""
    clean_input = normalize_text(user_input)
    
    for target in targets:
        clean_target = normalize_text(target)
        # Verificamos si el nombre de la DB (target) está dentro de la frase del motor (input)
        # O si el input está dentro del target (para casos inversos)
        if clean_target in clean_input or clean_input in clean_target:
            return target
    return None
