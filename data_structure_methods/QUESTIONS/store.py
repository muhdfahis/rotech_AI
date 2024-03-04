

base=declarative_base()


class stor(base):
    __tablename__="table"
    id= column(Integer,primary_key=True)
    name=column(Integer, primary_key=True)
    name= column(string(10))
    quantity = column(Integer)
    price=column(String(255))
    category= column(string(255))
    
    def __repr__(self):
        return f"({self.id}),{self.name},{self.price},({self.age})"
    
    usernamme= "fahis_usr"
    password= "Fhs@12345"
    encoded_password= quot_plus(password)
    
    