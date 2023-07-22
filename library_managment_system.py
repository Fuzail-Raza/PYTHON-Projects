

class library:
    def __init__(self):
        self.books=[]
        self.total_books=0
        f=open('file.txt','r')
        while True:
            line=f.readline()
            if not line:
                break
            self.add_books(line.strip())
        f.close()
    def add_books(self,book):
        self.books.append(book)
        self.total_books+=1
    def save_books(self):
        f=open('file.txt','w')
        for i in range(len(self.books)):
            f.write(self.books[i]+'\n')
        f.close()
    def check_validity(self):
        if (self.total_books==len(self.books)):
            print("Books are Accurately Marked")
        else:
            print("Books are not Accurately Marked")
    def print_books(self):
        for i in range(len(self.books)):
            print(f"{i+1}-{self.books[i]}")

if __name__=='__main__':
    compter_lab=library()
    compter_lab.add_books('Computer')
    compter_lab.add_books('English')
    compter_lab.check_validity()
    compter_lab.print_books()
    # print(compter_lab.books)
    print(len(compter_lab.books))
    compter_lab.save_books()
