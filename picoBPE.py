from collections import Counter

class picoBPE:
    def __init__(self, tokens):
        self.vocab = self.build_vocab(tokens)
        self.merge_ops = []

    def build_vocab(self, tokens):
        return {token: count for token, count in Counter(tokens).most_common()}

    def train(self, text, num_merges):
        tokens = list(text)
        for _ in range(num_merges):
            if len(tokens) <= 1:
                break
            bigrams = Counter(a + b for a, b in zip(tokens, tokens[1:]))
            if not bigrams:
                break
            merge_op = max(bigrams, key=bigrams.get)
            self.merge_ops.append(merge_op)
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] + tokens[i + 1] == merge_op:
                    new_tokens.append(merge_op)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens

        self.vocab = self.build_vocab(tokens)

    def encode(self, text):
        tokens = list(text)
        for merge_op in self.merge_ops:
            new_tokens = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] + tokens[i + 1] == merge_op:
                    new_tokens.append(merge_op)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1
            tokens = new_tokens
        return tokens

    def decode(self, tokens):
        return ''.join(tokens)
