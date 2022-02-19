class myRange:
    def __init__(self,start,end,step=1):
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            num=self.start
            self.start += self.step
            return num
        else:
            raise StopIteration
    def __len__(self):
        return self.end


x=myRange(10,50,5)

iter(x)

for num in x:
    print(num)

