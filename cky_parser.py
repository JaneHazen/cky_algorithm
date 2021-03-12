import sys
from nltk import CFG
import nltk.data
from nltk.tree import Tree
import itertools

def get_grammar(grammar_file):
    with open(grammar_file, "r") as grammar_file:
        cfg_input = nltk.data.load(grammar_file.read())
    return CFG.fromstring(cfg_input)

def get_sentences(sentence_file):
    with open(sentence_file, "r") as sentence_file:
        sentences = sentence_file.read()
    return sentences.split("\n")

def getCkyTable(sentence):
    grammar_file = sys.argv[1].strip()
    grammar = nltk.data.load(grammar_file)
    words = nltk.word_tokenize(sentence)
    table = [[set() for i in range(len(words) + 1)] for j in range(len(words) + 1)]
    back_tree = [[[] for i in range(len(words) + 1)] for j in range(len(words) + 1)]

    for col in range(1, len(words) + 1):
        for rule in grammar.productions():
            if rule.rhs() == tuple([words[col - 1]]):
                table[col - 1][col].update([rule.lhs()])
                back_tree[col - 1][col].append(Tree(str(rule.lhs()), [words[col - 1]]))
        for row in range(col - 1, -1, -1):
            for pivot in range(row + 1, col):
                subset_dict = {}
                sub_set_1 = table[row][pivot]
                sub_set_2 = table[pivot][col]
                for s in sub_set_1:
                    subset_dict[s] = [row, pivot]
                for s in sub_set_2:
                    subset_dict[s] = [pivot, col]
                combos = [element for element in itertools.product(sub_set_1, sub_set_2)]
                for item in grammar.productions():
                    for combo in combos:
                        if item.rhs() == combo:
                            table[row][col].update([item.lhs()])
                            sub_set_indices = []
                            rhs_pos_list = []
                            for rhs_pos in item.rhs():
                                rhs_pos_list.append(rhs_pos)
                                sub_set_indices.append(subset_dict[rhs_pos])
                            child_one = back_tree[sub_set_indices[0][0]][sub_set_indices[0][1]]
                            child_two = back_tree[sub_set_indices[1][0]][sub_set_indices[1][1]]
                            back_tree[row][col].append(Tree(str(item.lhs()), [child_one[0], child_two[0]]))
    return back_tree[0][-1]

def main():
    # strip in case the files are dumb
    sentence_file = sys.argv[2].strip()
    output_file = sys.argv[3]
    sentences = get_sentences(sentence_file)
    output = []
    for sentence in sentences:
        if sentence == "":
            continue
        print(sentence)
        output.append(sentence)
        sentence_tree = getCkyTable(sentence)
        for tree in sentence_tree:
            output.append(tree.pformat())
            print(tree.pformat())
        number_sentence = "Number of parses: " + str(len(sentence_tree)) + "\n\n"
        print(number_sentence)
        output.append(number_sentence)
    formatted_list = "\n".join(output)
    with open(output_file, 'x', encoding='utf8') as f:
        f.write(formatted_list)

main()
