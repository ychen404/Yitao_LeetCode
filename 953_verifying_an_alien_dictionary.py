class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}
        print(order_index)
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            # Find the first difference word1[k] != word2[k]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    # If the char in word1 is behind that of word2, these two words are not sorted
                    # based on the order
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
            
        return True