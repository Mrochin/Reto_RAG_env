# tests/test_rag_smoke.py
# Verifica que podemos indexar y recuperar un texto relevante con Chroma
# usando embeddings "mock" deterministas (sin API).

import hashlib
from typing import List
from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings

def _hash_vector(text: str, dim: int = 64) -> List[float]:
    h = hashlib.sha256(text.encode("utf-8")).digest()
    b = (h * ((dim + len(h) - 1) // len(h)))[:dim]  # repetir/recortar a 'dim'
    return [x / 255.0 for x in b]  # normalización simple 0..1

class DummyEmbeddings(Embeddings):
    def __init__(self, dim: int = 64):
        self.dim = dim
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [_hash_vector(t, self.dim) for t in texts]
    def embed_query(self, text: str) -> List[float]:
        return _hash_vector(text, self.dim)

def test_rag_pipeline_smoke(tmp_path):
    texts = [
        "La IA generativa permite crear contenido.",
        "ChromaDB es una base vectorial usada en sistemas RAG.",
        "Python 3.11 es estable para usar con LangChain."
    ]
    persist_dir = tmp_path / ".chroma_test"
    emb = DummyEmbeddings(dim=64)

    db = Chroma.from_texts(texts, emb, persist_directory=str(persist_dir))
    retriever = db.as_retriever(search_kwargs={"k": 1})
    results = retriever.get_relevant_documents("¿Qué es ChromaDB en un sistema RAG?")

    assert len(results) >= 1
    assert "ChromaDB" in results[0].page_content