from pathlib import Path
import regex as reg

# Pattern matching "Ch" or "ch" followed by numbers 1 through 22
PATTERN = r"\b[Cc]h([1-9]|1[0-9]|2[0-2])\b"

def formatChapterName(text: str) -> str:
    return reg.sub(PATTERN, r"**\g<0>**", text)

if __name__ == "__main__":
    file_path = Path("markdown_files/aSmallOutline.md")

    # 1. Read file contents with explicit encoding
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # 2. Format chapter names
    formatted_text = formatChapterName(text)

    # 3. Write back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(formatted_text)

    print(f"Successfully updated chapter formatting in {file_path}")