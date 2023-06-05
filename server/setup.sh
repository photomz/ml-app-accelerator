#!/bin/bash

pip install annoy flask
curl -O -L https://huggingface.co/stanfordnlp/glove/resolve/main/glove.6B.zip
mkdir -p data/glove
unzip glove.6B.zip -d data/glove/
rm -f glove.6B.zip