class question2:
    def __init__(self,strings):
        self.strings=strings
    def sort(self):
        n=len(self.strings)
        for i in range(n-1):
            pos=i
            for j in range(i+1,n):
                if self.strings[j]<self.strings[pos]:
                    pos=j
            self.strings[i],self.strings[pos]=self.strings[pos],self.strings[i]
        return self.strings