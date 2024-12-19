class thiSinh():
    name = input()
    date = input()
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input()) 
    
    def tongDiem(self):
        return self.mon1 + self.mon2 + self.mon3
    
    def date_form(self):
        if self.date[1] == '/':
            self.date = '0' + self.date
        if self.date[4] == '/':
            self.date = self.date[:3] + '0' + self.date[3:]
        return self.date
    
sv = thiSinh()
print(sv.name+' '+sv.date_form()+' '+str(sv.tongDiem()))