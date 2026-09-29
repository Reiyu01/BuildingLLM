"""
讀取文字檔用
"""

file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))
print(raw_text[:99])