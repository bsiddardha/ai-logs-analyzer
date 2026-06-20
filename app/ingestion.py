import re
from typing import List


# -----------------------------------
# Clean Logs
# -----------------------------------
def clean_log(log: str) -> str:
    """
    Normalize logs:
    - Remove extra spaces
    - Remove empty lines
    - Preserve line structure
    """
    cleaned_lines = []

    for line in log.splitlines():
        line = re.sub(r"\s+", " ", line.strip())

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


# -----------------------------------
# Chunk Logs
# -----------------------------------
def chunk_logs(log: str, max_length: int = 300) -> List[str]:
    """
    Split logs into chunks while preserving
    complete log lines.
    """
    lines = log.splitlines()

    chunks = []
    current_chunk = []
    current_length = 0

    for line in lines:
        line_length = len(line)

        if current_length + line_length > max_length and current_chunk:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_length = 0

        current_chunk.append(line)
        current_length += line_length

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


# -----------------------------------
# Full Ingestion Pipeline
# -----------------------------------
def ingest(log: str, max_length: int = 300) -> List[str]:
    cleaned = clean_log(log)
    chunks = chunk_logs(cleaned, max_length)
    return chunks


# -----------------------------------
# Example
# -----------------------------------
if __name__ == "__main__":

    sample_log = """
    INFO Service started
    INFO Loading configuration
    ERROR Database connection failed
    INFO Retrying connection
    INFO Retry successful
    WARNING High memory usage
    INFO Service running
    """

    chunks = ingest(sample_log, max_length=100)

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n----- CHUNK {i} -----")
        print(chunk)