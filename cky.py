class CKY():
    
    def __init__(self):
        pass

    size = 50

    ACC = ['' for i in range(20)]
    BCC = ['' for i in range(20)]
    ACC1 = ['' for i in range(20)]
    ACC2 = ['' for i in range(20)]

    grammar = {}

    #read grammar from grammar.txt file and reimplement the following methods
    def readGrammar(self,path):
        ls = []
        file = open(path, "r")
        for line in file.readlines():
            ls.append(line.strip())

        for elem in ls:
            elem = elem.split("->")
            self.grammar[elem[0].strip()] = elem[1].split("|")

        for key,value in self.grammar.items():
            self.grammar[key] = [i.strip() for i in value]

    
    def search(self, str):
        
        ACC = ['' for i in range(self.size)]
        k = 0
        
        for key,value in self.grammar.items():
            for i in range(len(value)):
                if str == value[i]:
                    ACC[k] = key
                    k += 1
        return ACC
        
        """
        for i in range(len(self.S)):
            if str == self.S[i]:
                ACC[k] = "S"
                k += 1
        for i in range(len(self.A)):
            if str == self.A[i]:
                ACC[k] = "A"
                k += 1
        for i in range(len(self.B)):
            if str == self.B[i]:
                ACC[k] = "B"
                k += 1
        for i in range(len(self.C)):
            if str == self.C[i]:
                ACC[k] = "C"
                k += 1
        return ACC
        """
        
    def lenc(self,str):
        i = 0
        while str[i] != '':
            i += 1
        return i

    def concat(self,str1 ,str2):
        l1 = self.lenc(str1)
        l2 = self.lenc(str2)
        ACC = ['' for i in range(self.size)]
        k = 0
        for i in range(l1):
            for j in range(l2):
                ACC[k] = str1[i] + str2[j]
                k += 1
        return ACC

    def append(self, str1 ,str2):
        l1 = self.lenc(str1)
        l2 = self.lenc(str2)
        ACC = ['' for i in range(l1+l2+1)]
        j = 0
        if l1 == 0:
            ACC = str2
        elif l2 == 0:
            ACC = str1
        else:
            for i in range(l1+l2):
                if i < l1:
                    ACC[i] = str1[i]
                else:
                    ACC[i] = str2[j]
                    j += 1
        return ACC

    def clear(self, str):
        l = self.lenc(str)
        for i in range(l):
            str[i] = ''
        return str

    def isIn(self, str, str1):
        b = False
        l = len(str)
        i = 0
        while i < l and str[i] != '':
            if str[i] == str1:
                b = True
            i += 1
        return b



    def removeDups(self,str):
        k = 0
        l = len(str)
        acc = ['' for i in range(l)]
        i = 0
        while str[i] != '':
            if not self.isIn(acc,str[i]):
                acc[k] = str[i]
                k += 1
            i += 1
        return acc

    
    def ckyAlg(self,str,filepath):
        index = len(str) +1
        l = len(str)
        b = False

        
        #String [][][] T = new String[index][index][50];
        # change above java code to python code
        T = [[['' for i in range(50)] for j in range(index)] for k in range(index)]

        self.readGrammar(filepath)
     

        for i in range(len(str)):
            T[i][i+1] = self.search(str[i])
        
        for u in range(2,index):
            for m in range(index-u):
                for i in range(1,u):
                    self.BCC = self.concat(T[m][m+i],T[m+i][m+u])
                    self.ACC = self.append(self.ACC,self.BCC)
                j = 0
                while self.ACC[j] != '':
                    ACC1 = self.search(self.ACC[j])
                    if (ACC1[0] != ''):
                        self.ACC2 = self.append(self.ACC2,ACC1)
                    j += 1
                self.ACC2 = self.removeDups(self.ACC2)
                T[m][m+u] = self.ACC2[:]
                self.clear(self.ACC2)
                self.clear(self.ACC)
                self.clear(self.BCC)
        
        print("list of non-terminals generating s (may contain dups): ")
        m = 0
        print()
        while T[0][l][m] != '':
            print(T[0][l][m], end = " ")
            if T[0][l][m] == "S":
                b = True
            m += 1
        print()
        print()
        return b


            