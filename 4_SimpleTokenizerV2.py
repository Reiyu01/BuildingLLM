"""
加入了特殊token，
<|unk|> 代表輸入資料中，詞彙表裡沒有對應的字
<|endoftext|> 用來區隔輸入資料中兩個不相關來源的文本，即若有兩篇文章以連在一起方式作為輸入資料，則endoftext為兩篇文章之間的區隔，幫助LLM理解文章的段落

研究人員也會考慮加入其他額外的特殊token
[BOS] 序列開始：標註文本的開始，讓llm能識別一段內容的起點
[EOS] 序列結束：標住在文本的結尾，類似於<|endoftext|>的功能
[PAD]填充：批次訓練會包含不同長度的文本，為了確保訓練效果與效率，會用[PAD]來填充較短的文本，使每個文本的長度一致
GPT斷詞器不需要以上的特殊標記，他只使用ENDOFTEXT。
通常批次訓練時或使用遮罩這代表模型不會去處理填充功能的TOKEN
GPT也不使用unk表示未知的新字詞，而是使用字節對編碼(BPE, Byte Pair Encoding)來進行斷詞，是一種將字詞分割為更小單位的斷詞方法
"""

import re


file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
all_words.extend(["<|endoftext|>", "<|unk|>"])

vocab_size = len(all_words)
print("========================")
print("詞彙量總數", vocab_size)
vocab = {token:integer for integer,token in enumerate(all_words)}



class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {integer:token for token, integer in vocab.items()}


    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        #將不在詞彙表的字轉成unk
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        #轉換後的字再轉成token id
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids



    def decode(self, id):
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([.,?!"()\'])', r'\1', text)

        return text

tokenizer = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text3 = " <|endoftext|> ".join((text1,text2))

print(text3)

ids = tokenizer.encode(text3)

print(tokenizer.decode(ids))


# text = """"
# It's the last he painted, you know,"
# Mrs. Gisburn said with pardonable gay.
# """

# text2 = [53, 150, 523]
# ids = tokenizer.encode(text)
# id2 = tokenizer.decode(ids)
# print(ids)
# print(id2)