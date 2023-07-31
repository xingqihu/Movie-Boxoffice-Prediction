from flask import request, Flask,render_template
import pickle
import pandas as pd


file1=open('Movie_BoxOffice_model.pkl','rb')
rf=pickle.load(file1)
file1.close()

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        my_dict=request.form

        rating=str(my_dict['rating'])
        region=str(my_dict['region'])
        genre=str(my_dict['genre'])
        year=int(my_dict['year'])
        month=str(my_dict['month'])
        score=float(my_dict['score'])
        budget=float(my_dict['budget'])
        runtime=float(my_dict['runtime'])
        Total_Gross_Bankability=float(my_dict['Total_Gross_Bankability'])

        input_features=pd.DataFrame({'rating':rating,'region':region,'genre':genre,
                                     'year':year,'month':month,'score':score,'budget':budget
                                     ,'runtime':runtime,'Total_Gross_Bankability':Total_Gross_Bankability})
        prediction=rf.predict(input_features)
        
        string='The Predicted Movie BoxOffice is: '+str(float(prediction))

        return render_template('show.html',string=string)
    return render_template('home,html')

if __name__=="__main__":
    app.run(debug=True)
