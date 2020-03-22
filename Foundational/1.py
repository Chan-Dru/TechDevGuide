'''
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
'''
# O(N*W) check each dictionary word with S
def LongestSubsequencewithSortedDictionary(S,D):
    # sort the dictionary word in descending word length, find first occurance - which is longest subsequence 
    D = sorted(D,key=len)[::-1]
    output = "none"
    max_ = 0
    w = len(S)
    for word in D:
        i = 0
        n = len(word)
        j = 0
        while(j<w and i <n):
            if(word[i] == S[j]):
                i += 1
            j += 1
        if i==n and n > max_:
            output = word
            max_ = n
            return output
    return output

def LongestSubsequencewithBinarySearch(S,D):
    S_processed = PreprocessString(S)
    D = sorted(D,key=len)[::-1]
    for word in D:
        if(SubSequence(S_processed,word)!=-1):
            return word
        
# Preprocess the String S - character index dict
def PreprocessString(S):
    S_processed = dict()
    for i in range(len(S)):
        if S[i] in S_processed:
            S_processed[S[i]].append(i)
        else:
            S_processed[S[i]] = [i]
    return S_processed

def SubSequence(S_processed, word):
    x = -1
    for w in word:
            if w in S_processed:
                a = S_processed[w]
                t = BinarySearch(a,x,0,len(a)-1)
                if t == -1:
                    return -1
                x = a[t]
            if x == -1:
                return -1
    return x

# Return next maximum of x in the array
def BinarySearch(arr,x,l,h):
    if(x<arr[0]):
        return 0
    if(l<h):
        mid = l + (h-l)//2
        if(mid-1 >=l and arr[mid-1]<= x and arr[mid] > x):
            return mid
        elif(mid+1 <=h and arr[mid]<= x and arr[mid+1] > x):
            return mid+1
        if(arr[mid] < x):
            l = mid+1
        elif(arr[mid] > x and arr[mid-1]<x):
            return mid
            h = mid-1
        return BinarySearch(arr,x,l,h)
    return -1



if __name__ == "__main__":
    S = "abppplee"
    D = {"able", "ale", "appple", "bale", "kangaroo"}
    # subsequence = LongestSubsequencewithSortedDictionary(S,D)
    subsequence = LongestSubsequencewithBinarySearch(S,D)
    print("The longest subsequence is {}".format(subsequence))
