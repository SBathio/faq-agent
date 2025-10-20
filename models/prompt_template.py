def get_prompt_template(style: str = "default") -> str:
    templates = {
        "default": "You are a helpful assistant answering questions from a FAQ knowledge base. Use the retrieved context if relevant.",
        "friendly": "You're a helpful and friendly assistant. Answer with a cheerful tone using the context below.",
        "formal": "Respond in a professional and formal tone using the following context when necessary."
    }

    if style not in templates:
        raise ValueError(f"Unknown prompt style: '{style}'")

    return templates[style]