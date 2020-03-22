#!/usr/bin/env python
import collections
import sys
def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    print(letter_positions)
    # For each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed.
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    print(letter_positions)
    # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as 
    # expensive as simple iterations as long as 
    # the length of the arrays for each letter is
    # “small”.  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.              
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        print("======>",word)
        pos = 0
        for letter in word:
            print(letter)
            if letter not in letter_positions:
                break
        # Find any remaining valid positions in search string where this
        # letter appears.  It would be better to do this with binary search,
        # but this is very Python-ic.
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            print(possible_positions)
            if not possible_positions:
                pos = 0
                break
            pos = possible_positions[0] + 1
        if pos != 0:
            return word

def test(S,D):
    # create tuple
    t = collections.defaultdict(list)
    for word in D:
        t[word[0]].append((word,0))

    output = []
    # traverse the given string and increment the tuple word and move it to the map.
    for c in S:
        if c in t:
            for i in range(len(t[c])-1,-1,-1):
                w,l = t[c].pop(i)
                if(len(w)==l+1):
                    output.append(w)
                elif l+1 < len(w):
                    t[w[l+1]].append((w,l+1))
    # find the longest subsequence from the output
    result = ""
    for i in output:
        if len(i)>len(result):
            result = i

    return result


if __name__ == '__main__':
    S = "abppplee"
    D = {"able", "ale", "appple", "bale"}
    print(test(S,D))
    # print(find_longest_word_in_string(S,D))