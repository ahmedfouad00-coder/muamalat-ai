from langchain_core.documents import Document


def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(
        f"""
{doc.page_content}

التصنيف: {doc.metadata.get("category", "غير معروف")}
رقم الفتوى: {doc.metadata.get("id", "غير متوفر")}
"""
        for doc in docs
    )

