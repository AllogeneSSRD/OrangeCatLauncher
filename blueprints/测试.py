import wtforms as wtf


class Sb(wtf.Form):
    aa = 10
    def sb(self, field):
        aa = field.data
        bb = self.field.data
        return aa, bb
    
x = Sb()
# x.sb({aa:"123@ww.com"})

from werkzeug.security import generate_password_hash


for i in range(10):
    q = generate_password_hash("123456")
    print(q)