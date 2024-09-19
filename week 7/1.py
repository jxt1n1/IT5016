class Whitecliffe():
    def __init__(self,studentid, name,program):
        self.studentid = studentid
        self.name = name
        self.program = program
        self.membershipid = 400001
    def member(self):
        self.membershipid+=1
        return self.membershipid

    def display(self):
        print(f"Student ID : {self.studentid} \n Last Name : {self.name} \n Student Program : {self.program} \n Membership ID : {self.membershipid}")

info = Whitecliffe(20240746,"Sardana","Bachelor")
info.member()
info.display()