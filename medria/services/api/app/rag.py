from dataclasses import dataclass


@dataclass
class KnowledgeDocument:
    id: str
    title: str
    content: str
    authority: str = "curated"


KNOWLEDGE_BASE = [
    KnowledgeDocument(
        id="doc-001",
        title="General safety guidance",
        content="Medria AI is an informational tool and does not replace medical diagnosis. For emergency symptoms such as chest pain, severe breathing difficulty, fainting, stroke symptoms, or heavy bleeding, seek immediate emergency care.",
        authority="internal-safety",
    ),
    KnowledgeDocument(
        id="doc-002",
        title="Medication caution",
        content="Do not ask Medria AI to prescribe medicine or instruct a user to stop a medication without clinician review. Any medication-related directions should be verified with a licensed healthcare professional.",
        authority="internal-safety",
    ),
    KnowledgeDocument(
        id="doc-003",
        title="Consultation workflow",
        content="Users should be guided through a structured clinical intake, including symptoms, allergies, medications, and red-flag screening before any follow-up. The system should escalate high-risk cases for human review.",
        authority="internal-safety",
    ),
]


def retrieve_documents(query: str, top_k: int = 3) -> list[KnowledgeDocument]:
    lowered_query = query.lower()
    scored = []
    for doc in KNOWLEDGE_BASE:
        score = 0
        full_text = f"{doc.title} {doc.content}".lower()
        for token in lowered_query.split():
            if token in full_text:
                score += 1
        if score > 0 or lowered_query in doc.title.lower():
            scored.append((score, doc))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]


def build_context(query: str) -> str:
    docs = retrieve_documents(query, top_k=3)
    if not docs:
        return "No curated context found."
    return "\n\n".join([f"[{doc.title}] {doc.content}" for doc in docs])
