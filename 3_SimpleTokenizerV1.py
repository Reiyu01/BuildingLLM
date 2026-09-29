import re


file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)

preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
vocab = {token:integer for integer,token in enumerate(all_words)}



class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {integer:token for token, integer in vocab.items()}


    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids



    def decode(self, id):
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([.,?!"()\'])', r'\1', text)

        return text

tokenizer = SimpleTokenizerV1(vocab)
text = """"
It's the last he painted, you know,"
Mrs. Gisburn said with pardonable pride.
"""

text2 = [53, 150, 523]
ids = tokenizer.encode(text)
id2 = tokenizer.decode(ids)
print(ids)
print(id2)