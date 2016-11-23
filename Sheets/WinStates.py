
GOLD='gold'
SILVER='silver'
PLATINUM='platinum'

winStates = {GOLD:['B1','B2','B3','B4'],
             SILVER:['Y1','Y2','Y3','Y4'],
             PLATINUM:['G1','G2','G3','G4']}




def check_straight(kind,cases):
      case_list = winStates[kind]
      total = 0
      state = False

      for each in case_list:
          if(cases[each]>0):
              total+=1

          if(total == 4):
                state=True

      return state

def check_num(count,num):
	state = False
	if(count >= num):
	  state = True
	
	return state


def check_wins(user):
        
    if(check_straight(GOLD,user.get_user_cases())):
            #TODO AWARD GOLD BADGE
            print("winner : Gold")

    if(check_straight(SILVER,user.get_user_cases())):
            #TODO AWARD Silver Badge
            print("winner : Silver")

    if(check_straight(PLATINUM,user.get_user_cases())):
            #TODO AWARD Platinum Badge
            print("winner : Platinum")

    if(check_num(user.get_case_count(),8)):
            #TODO AWARD 8 Case Badge
            print("winner : 8")

    if(check_num(user.get_case_count(),10)):
            #TODO AWARD 10 Case Badge
            print("winner : 10")
