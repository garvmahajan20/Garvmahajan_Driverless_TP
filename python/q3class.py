class question3:
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
class question31:
    def __init__(self,strings):
        self.strings=strings

    def binary(self,word):
        word1=word.lower()
        n=len(self.strings)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if word1==self.strings[mid]:
                return True
            if word1>self.strings[mid]:
                low=mid+1
            else:
                high=mid-1
        return False
