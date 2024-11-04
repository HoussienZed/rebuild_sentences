def rebuild_sentences(words, length):
    for i in range(len(words)):
        if len(words[i]) != length[i]:
            target_word = list(words[i])
            for j in range(len(words[i]) - length[i]):
                target_word.pop()
            words[i] = ''.join(target_word)

    rebuilt_sentence = ' '.join(words)
    return print(rebuilt_sentence)


rebuild_sentences(["the", "sky", "is", "blue"], [3, 3, 2, 4])
