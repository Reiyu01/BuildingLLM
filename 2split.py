import re
text = "Hello, world. This, is a test."
text2 = "Hello, world. Is this-- a test?"

"""
陽春版Tokenizer
無法分割逗號

result = re.split(r'(\s)', text)
print(result)
"""



"""
V2
result = re.split(r'([,.]|\s)',text)
result = [item for item in result if item.strip()]
print (result)
"""


"""
V3處理其他的標點符號
result = re.split(r'([,.:;?_!"()\']|--|\s)', text2)
result = [item.strip() for item in result if item.strip()]
print(result)
"""

file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

preprocessed = [item.strip() for item in preprocessed if item.strip()]

print("==========提取token數==========")
print(len(preprocessed))
print(preprocessed[:30])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("==========詞彙表總數字==========")
print(vocab_size)

vocab = {token:integer for integer,token in enumerate(all_words)}

print("==========詞彙表前50筆==========")
for i, item in enumerate(vocab.items()):
    print(item)
    if i >=50:
        break