from langchain_community.document_loaders import CSVLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_data(file_path: str) -> list[Document]:
    loader = CSVLoader(
        file_path=file_path,
        encoding="utf-8",
    )
    return loader.load()


def split_documents(
    docs: list[Document], chunk_size: int = 1000, chunk_overlap: int = 150
) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[".", "\n", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return text_splitter.split_documents(docs)
