"""
BPE備用在訓練GPT2、GPT3之類的模型以及ChatGPT的原始模型
BPE將以tiktoken實現，tiktoken基於Rust語言開發
BPE基礎演算法能夠將不在原先詞彙表中的字詞拆成更小的子詞或是拆成單個字元
"""

import tiktoken

#與SimpleTokenizerV2類似
tokenizer = tiktoken.get_encoding("gpt2")

text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace."
text2 = "Akwirw ier"
integer = tokenizer.encode(text2, allowed_special={"<|endoftext|>"})
print(integer)

strings = tokenizer.decode(integer)
print(strings)

#輸出可以發現BPE能夠處理未知詞someunknownPlace