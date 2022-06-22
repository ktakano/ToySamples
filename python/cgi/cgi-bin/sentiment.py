# -*- coding: utf-8 -*-
from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer

bert_model_ja = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
tokenizer_ja = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
analyzer_ja = pipeline("sentiment-analysis",model=bert_model_ja,tokenizer=tokenizer_ja)

print ("Content-Type: text/plain")
print ("\n")

print(analyzer_ja("今日のセミナーは楽しい"))
print(analyzer_ja("先生がいなくて悲しい"))