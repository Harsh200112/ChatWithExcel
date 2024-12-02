import os
import faiss
import warnings
import nest_asyncio
from llama_parse import LlamaParse
from llama_index.core import Settings
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext

nest_asyncio.apply()
warnings.filterwarnings("ignore")

def get_data(file_path):
    parser = LlamaParse(
        api_key=os.environ.get('LLAMA_CLOUD_API_KEY'),
        result_type="markdown"
    )

    docs = parser.load_data(file_path)

    d = 384
    faiss_index = faiss.IndexFlatL2(d)
    embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.embed_model = embedding_model

    vector_store = FaissVectorStore(faiss_index=faiss_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        docs, storage_context=storage_context
    )

    index.storage_context.persist()
    print("Data Parsed Successfully!!")
