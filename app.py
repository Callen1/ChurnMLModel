from pyexpat import model
from fastapi import FastAPI
import uvicorn
import pickle
from model import Churn        #import model created 

app=FastAPI()

model=pickle.load(open("classifier.pkl","rb"))
@app.get("/{name}")
def hello(name):
    return {"Hello {} and welcome!".format(name)}

# @app.get("/")                   #decorator wraps function around itself
# def greet():
#     return {"Hello World!"}     #creating a basic API

@app.post("/predict")
def predict(req:Churn):       #the function has model that stores values given to server values
    #pass                      #pass attributes of the model as a parameter
    cred=req.CreditScore        #store each feature request in a variable
    age=req.Age
    ten=req.Tenure
    bal=req.Balance
    prod=req.NumOfProducts 
    card=req.HasCrCard
    active=req.IsActiveMember
    estsal=req.EstimatedSalary
    germany=req.Geography_Germany
    spain=req.Geography_Spain
    gender=req.Gender_Male
    #convert the above variables/values to a list
    features=list([cred,age,ten,bal,prod,card,active,estsal,germany,spain,gender])
    predict=model.predict([features])
    probab=model.predict_proba([features])
    if (predict==1):
        return {"Answer":"The client will exit with this {} probability".format(probab[0][1])}
    else:
        return{"Answer":"The client will not exit with this {} probability".format(probab[0][0])}

if __name__=="__main__":
    uvicorn.run(app)            #function tells python interpretor that it is an entry point of the program
