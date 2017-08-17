# Text vocabulary enhancer
Enhances an english textsvocabulary using Word2Vec and other NLP tools. This isn't derived from a paper or something like that and I've personally not seen anything similar.

### An example
If I input this.
```
In my freetime I look at some great movie and play lots of piano.
```
It turns into to this!
```
In my freetime I look at some outstanding flick and run heaps of pianoforte.
```
Your teacher will love your use of unecessary words like "pianoforte". :)

### Requirements
* Python 3.*
* Gensim
* NLTK, full installation


### Setup
1. Download GoogleNews or other compatible Word2Vec model.
Can be downloaded from here: https://code.google.com/archive/p/word2vec/
2. Run
```
python3 create_sims_file.py
```
3. Run
```
python3 freq.py
```
4. Done

### Running
To test it, run.
```
python3 main.py "TEXT HERE"
```


### Other
Made by Oliver Edholm, 15 years old.
