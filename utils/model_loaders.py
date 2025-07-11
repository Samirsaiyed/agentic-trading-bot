import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from config.config_loader import load_config

class ModelLoader:
    """
    A utility class to load emnedding model and LLM model
    """

    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config = load_config()

    def _validate_env(self):
        """
        Validate neccesary environment variables.
        """
        required_vars = ["OPENAI_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    def load_embeddings(self):
        """
        Load and return the embedding model
        """
        print("Loading Embedding model")
        model_name = self.config["embedding_model"]["model_name"]
        return OpenAIEmbeddings(model=model_name)

    def load_llm(self):
        """
        Load and return the LLM model.
        """
        print("LLM loading...")
        model_name = self.config["llm"]["model_name"]
        openai_model = ChatOpenAI(model_name=model_name)
        return openai_model