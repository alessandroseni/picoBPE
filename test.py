from picoBPE import picoBPE

with open('dune.txt', 'r', encoding='utf-8') as file:
    train_text = file.read()

test_text = "Hello earthlings, welcome to Dune! Let the spice flow through you."

tokenizer = picoBPE([])

tokenizer.train(train_text, num_merges=50)

vocab = tokenizer.vocab
token_count = len(tokenizer.vocab)
merge_ops = tokenizer.merge_ops

print("Vocabulary:", vocab)
print("Total unique tokens:", token_count)
print("Merge operations:", merge_ops)

encoded = tokenizer.encode(test_text)
print("Encoded:", encoded)

decoded = tokenizer.decode(encoded)
print("Decoded:", decoded)

assert decoded == test_text, "Decoded text does not match the original test text."