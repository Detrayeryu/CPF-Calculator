#--- CPF rates ---#
MA_Limit = 60000
SA_Limit = 181000
# OA has no limit
MA_Interest = 1.0408
SA_Interest = 1.0408
OA_Interest = 1.025
MA_Salary_Contribution = 0.08
SA_Salary_Contribution = 0.06
OA_Salary_Contribution = 0.23
Add_Interest_Below55_First60k = 1.01 # Capped at 20,000 for OA
Add_Interest_55AndAbove_First30k = 1.02 
Add_Interest_55AndAbove_Next30k = 1.01 # Capped at 20,000 for OA
#--- CPF rates ---#

#---user variables---#
Age = 19
Target_Retirement_Age = 0
MA_Balance = 950
SA_Balance = 520
OA_Balance = 1700
Target_Balance = 1000000
Salary_Monthly = 6000 
#---user variables---#

#--- Pre Defined Variables ---#
Salary_Contribution_Annually = 0

#--- Pre Defined Variables ---#

def CalculateTotalBalance(MA,SA,OA):
    total = MA + SA + OA
    return total

def CalculateSalaryContributionPerYear(salary):
    salary = salary * 0.37 * 12
    return salary

###___main___###
Salary_Contribution_Annually = CalculateSalaryContributionPerYear(Salary_Monthly)
TotalCPFBalance =  MA_Balance + SA_Balance + OA_Balance
years = 0

while(TotalCPFBalance < Target_Balance):
    Predicted_MA_Balance = MA_Interest*(MA_Balance + (MA_Salary_Contribution*Salary_Contribution_Annually))
    Rollover_Amount_to_SA = 0
    
    if(Predicted_MA_Balance > MA_Limit):
        if(Rollover_Amount_to_SA > 0):
            Amount_Needed_To_Reach_Limit_MA = MA_Limit - MA_Balance
            Amount_To_Be_Added_To_MA = Predicted_MA_Balance - MA_Balance
            Rollover_Amount_to_SA = Amount_To_Be_Added_To_MA - Amount_Needed_To_Reach_Limit_MA
            MA_Balance = MA_Limit
        else:
            Rollover_Amount_to_SA = Predicted_MA_Balance - MA_Balance
            MA_Balance = MA_Limit
           
    else:
        Rollover_Amount_to_SA = 0
        MA_Balance = Predicted_MA_Balance
    
    print(f"MA balance : {MA_Limit} \nRollover to SA: {Rollover_Amount_to_SA}")
        
    Predicted_SA_Balance = (SA_Interest*(SA_Balance + (SA_Salary_Contribution*Salary_Contribution_Annually))) + Rollover_Amount_to_SA
    Rollover_Amount_to_OA = 0
    
    if(Predicted_SA_Balance > SA_Limit):
        if(Rollover_Amount_to_OA > 0):
            Amount_Needed_To_Reach_Limit_SA = SA_Limit - SA_Balance
            Amount_To_Be_Added_To_SA = Predicted_SA_Balance - SA_Balance
            Rollover_Amount_to_OA = Amount_To_Be_Added_To_SA - Amount_Needed_To_Reach_Limit_SA
            SA_Balance = SA_Limit
        else:
            Rollover_Amount_to_OA = Predicted_SA_Balance - SA_Balance
            SA_Balance = SA_Limit
    else:
        Rollover_Amount_to_OA = 0
        SA_Balance = Predicted_SA_Balance 

    print(f"SA balance : {SA_Balance} \nRollover to OA: {Rollover_Amount_to_OA}")
    Predicted_OA_Balance = OA_Interest*(OA_Balance + (OA_Salary_Contribution*Salary_Contribution_Annually)) + Rollover_Amount_to_OA
    OA_Balance = Predicted_OA_Balance
    
    years += 1
    TotalCPFBalance = CalculateTotalBalance(MA_Balance, SA_Balance,OA_Balance)
    print(f"OA balance : {OA_Balance}\n\n")
    if TotalCPFBalance >= Target_Balance:
        break
    
    
TotalCPFBalance = format(TotalCPFBalance, ".2f")
print(f"MA = {MA_Balance} \nSA = {SA_Balance} \nOA = {OA_Balance}")
print(f"Required number of years = {years}")
print(f"Final balance = {TotalCPFBalance}")
