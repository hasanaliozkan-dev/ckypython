from cky import CKY

s = "aba"

c = CKY()
print("input string s: ", s)
print()
path = "./palindrome_grammar.txt"

b = c.ckyAlg(s,filepath = path)

if b: print("s in L(G):  YES" ) 
else : print("s in L(G):  NO" )

