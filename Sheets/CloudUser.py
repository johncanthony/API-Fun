class CloudUser():

    username=''
    user_cases={}
    case_count=0
    case_types = ['W','B','Y','G']

    
    def __init__(self,uname):
        self.username = uname
        self.init_user_cases()

    def get_username(self):
        return self.username

    def set_case_count(self, cc):
        if self.case_count != cc:
            self.case_count = cc

    def get_case_count(self):
        return self.case_count

    def init_user_cases(self):
        for each in self.case_types:
            for i in range(1,5):
                label=each+str(i)
                self.user_cases[label]=0

    def set_user_cases(self,case_list):
        for each in case_list:
            self.user_cases[each]+=1


    def get_user_cases(self):
        return self.user_cases


   



#Test Code
'''
user = CloudUser("anthonyjo")
cases = ['B1','B1','B2','G3']
user.set_case_count(len(cases))

print(user.get_user_cases())

user.set_user_cases(cases)

print(user.get_user_cases())
'''
