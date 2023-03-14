import os, sys
try:
    __import__("api_enc").menu()
except Exception as e:
    exit(str(e))
