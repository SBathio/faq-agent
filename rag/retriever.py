from langchain_core.documents import Document

def get_top_k_chunks(query: str, k: int = 3) -> list[Document]:
    # Dummy chunks for now (mocking vector DB)
    return [
        Document(page_content="To reset your password, go to the login page and click 'Forgot Password'.",
                 metadata={"source": "faq_guide.pdf"}),
        Document(page_content="You will receive an email with a reset link.",
                 metadata={"source": "faq_email_procedure.md"}),
    ]