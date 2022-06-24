class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         products.sort()
#         # print(products)
#         ans = []
#         MAX_RES = 3
        
#         # create the typed words
#         typedWords = ''
#         typedWordList = []
#         for word in searchWord:
#             typedWords += word
#             typedWordList.append(typedWords)
        
#         for word in typedWordList:
#             i = MAX_RES
#             res = []
#             for product in products:            
#                 if word in product and product.startswith(word) and i>0:    
#                     res.append(product)
#                     i -= 1            
#             ans.append(res)           
#         return ans
        
        # alternate solution 60 ms
        products.sort()
        res, cur = [], ''
        for c in searchWord:
            cur += c
            i = bisect.bisect_left(products, cur)
            res.append([w for w in products[i:i+3] if w.startswith(cur)])
        return res