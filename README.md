# picoBPE

A minimalistic Byte Pair Encoding (BPE) tokenizer for simple text processing.

## Overview

picoBPE is inspired by the simplicity of [minBPE](https://github.com/karpathy/minbpe/) and [picoGPT](https://github.com/jaymody/picogpt/) - aiming to provide a straightforward implementation of the BPE algorithm, focusing solely on text tokenization. This project is for educational purposes.

## Features

- Simple BPE text tokenization
- Trainable on any text corpus
- Encode and decode functionalities

## Usage

The algorithm is implemented in `picoBPE.py`. You can run `test.py` to see an example of how picoBPE works. It is trained on a Dune excerpt stored in `dune.txt`.

```python
python test.py
```