from app.services.memory_extractor import MemoryExtractor

extractor = MemoryExtractor()

result = extractor.extract(
    "My favorite color is blue."
)

print(result)