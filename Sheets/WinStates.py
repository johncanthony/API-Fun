winStates = {'gold':['B1','B2','B3','B4'],
             'silver':['Y1','Y2','Y3','Y4'],
             'platinum':['G1','G2','G3','G4']}




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

        
