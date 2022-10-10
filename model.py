from pydantic import BaseModel

class Churn(BaseModel):
    CreditScore:int
    Age:int
    Tenure:int
    Balance:float
    NumOfProducts:int 
    HasCrCard:int
    IsActiveMember:int
    EstimatedSalary:int
    Geography_Germany:int
    Geography_Spain:int
    Gender_Male:int