class CloudUser():

    username=''
    case_count=0
    case_types = ['W','B','Y','G']
    user_cases={}
    
    def __init__(self,uname='',cc=0,uc={}):
        self.username = uname
        self.user_cases = self.init_user_cases()
	self.case_count = cc
	self.set_user_cases(uc) 

    def __str__(self):
	builder = "Username: " + self.username + ":" + "\n"
	builder += "Case Count: " + str(self.case_count) + ":" + "\n"
	builder += "Cases: " + str(self.user_cases) + "\n"
	return builder


    def get_username(self):
        return self.username

    def set_case_count(self, cc):
        if self.case_count != cc:
            self.case_count = cc

    def get_case_count(self):
        return self.case_count

    def init_user_cases(self):
	temp = {}
        for each in self.case_types:
            for i in range(1,5):
                label=each+str(i)
                temp[label]=0
	return temp

    def set_user_cases(self,case_list):
	for each in case_list:
            index=each.lstrip()
	    if (index in self.user_cases.keys()):
            	self.user_cases[index]+=1
	
	

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
