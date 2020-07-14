from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("TurkuNLP/wikibert-base-vi-cased")
tokens = tokenizer("Phim Kẻ Trộm Mặt Trăng – Despicable Me Full HD thuyết minh nhân vật tâm điểm của bộ phim là Gru,\
     một tên tội phạm khét tiếng. Gru và đám tay chân robot tí hon chuyên đi đánh cắp những biểu tượng nổi tiếng của thế giới.")
print(tokens)
#model = AutoModel.from_pretrained("TurkuNLP/wikibert-base-vi-cased")