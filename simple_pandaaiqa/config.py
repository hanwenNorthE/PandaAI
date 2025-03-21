"""
Configuration settings for the PandaAIQA application
"""

import os

# server settings
HOST = "localhost"
PORT = 8000
DEBUG = True

# text processing settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_TEXT_LENGTH = 30000000  # increased for video processing

# embedding settings
EMBEDDING_DIMENSION = 1536

# search settings
DEFAULT_TOP_K = 3
SIMILARITY_THRESHOLD = 0.0

# storage settings
DEFAULT_STORAGE_DIR = os.path.join(os.getcwd(), "knowledge_base")
KB_PERSISTENCE_ENABLED = True

# LM Studio settings
LM_STUDIO_API_BASE = "http://127.0.0.1:1234"
LM_STUDIO_MODEL = "default"
LM_STUDIO_MAX_TOKENS = 1024
LM_STUDIO_TEMPERATURE = 0.7

#ANYTHINGLLM
ANYTHINGLLM_API_BASE = "http://localhost:3001/api"
ANYTHINGLLM_KEY = "77WZ5NE-XEX4T4X-GVZ74EK-J43FRVP"
ANYTHINGLLM_MODEL = "default"
ANYTHINGLLM_MAX_TOKENS = 1024
ANYTHINGLLM_TEMPERATURE = 0.7