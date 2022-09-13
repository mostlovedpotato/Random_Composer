import random
import string
from graph import Vertex, Graph


def get_words(text_path):
    with open(text_path, 'r') as reader:
        text = reader.read()
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    return words


def make_graph(words):
    G = Graph()

    prev_word = None
    for word in words:
        curr_vertex = G.get_vertex(word)

        if prev_word:
            prev_word.increment_edge(curr_vertex)

        prev_word = curr_vertex

    G.generate_prob_mappings()
    return G


def create(G, words, length=10):
    quote = []
    word = G.get_vertex(random.choice(words))

    for _ in range(length):
        quote.append(word.value)
        word = G.get_next_word(word)

    return quote


def main():
    words = get_words('files/random_quote.txt')
    G = make_graph(words)

    quote = create(G, words, 15)

    return ' '.join(quote)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(main())
    # pass
