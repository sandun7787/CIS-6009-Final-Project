<img src="https://github.com/Kumar-laxmi/Heart-Disease-Prediction-System/blob/main/SCREEN-SHOTS/Heart-Disease-Prediction-System-banner.png" />

## Abstract 
<p> 
  Now days, Heart disease is the most common disease. But, unfortunately the treatment of heart
disease is somewhat costly that is not affordable by common man. Hence, we can reduce this
problem in some amount just by predicting heart disease before it becomes dangerous
using Heart Disease Prediction System Using Machine Learning and Data mining. If we can
find out heart disease problem in early stages then it becomes very helpful for
treatment. Machine Learning and Data Mining techniques are used for the construction
of Heart Disease Prediction System. In healthcare biomedical field, there is large use of heath
care data in the form of text, images, etc but, that data is hardly visited and is not mined. So,
we can avoid this problem by introducing Heart Disease Prediction System. This system will
help us reduce the costs and to enhance the quality treatment of heart patients. This system can
able to identify complex problems and can able to take intelligent medical decisions. The
system can predict likelihood of patients of getting heart problems by their profiles such as
blood pressure, age, sex, cholesterol and blood sugar. Also, the performance will be compared
by calculation of confusion matrix. This can help to calculate accuracy, precision, and recall.
The overall system provides high performance and better accuracy. 
</p>

## Introduction
<p>
  The health care industries collect huge amounts of data that contain some hidden information,
which is useful for making effective decisions. For providing appropriate results and making
effective decisions on data, some advanced data mining techniques are used. In this study, a
Heart Disease Prediction System (HDPS) is developed using Naives Bayes and Decision Tree
algorithms for predicting the risk level of heart disease. The system uses 13 medical parameters
such as age, sex, blood pressure, cholesterol, and obesity for prediction. The HDPS predicts
the likelihood of patients getting heart disease. It enables significant knowledge. E.g.
Relationships between medical factors related to heart disease and patterns, to be established.
We have employed the multilayer perceptron neural network with back propagation as the
training algorithm. The obtained results have illustrated that the designed diagnostic system
can effectively predict the risk level of heart diseases.
</p>

### Aim
<p> 
  To predict heart disease according to input parameter values provided by user and dataset
stored in database.
</p>

### Objective
<p>
  The main objective of this project is to develop a heart disease prediction system. The system
can discover and extract hidden knowledge associated with diseases from a historical heart data
set Heart disease prediction system aims to exploit data mining techniques on medical data set
to assist in the prediction of the heart diseases.
</p>

### Project Scope
<p>
  The project has a wide scope, as it is not intended to a particular organization. This project is
going to develop generic software, which can be applied by any businesses organization.
Moreover it provides facility to its users. Also the software is going to provide a huge amount
of summary data.
</p>

## System Analysis
### Modules:
- **Patient Login:-** *Patient Login to the system using his ID and Password.*
- **Patient Registration:_** *If Patient is a new user he will enter his personal details and he
will user Id and password through which he can login to the system.*
- **My Details:-** *Patient can view his personal details.*
- **Disease Prediction:-** *- Patient will specify the input parameter values. System will take
input values and predict the disease based on the input data values specified by the
patient and system will also suggest doctors based on the locality*
- **Search Doctor:-** *Patient can search for doctor by specifying name, address or type.*
- **Feedback:-** *Patient will give feedback this will be reported to the admin*
- **Doctor Login:-** *Doctor will access the system using his User ID and Password.*
- **Patient Details:-** *Doctor can view patient’s personal details.*
- **Notification:-** *Admin and doctor will get notification how many people had accessed
the system and what all are the diseases predicted by the system.*
- **Admin Login:-** *Admin can login to the system using his ID and Password.*
- **Add Doctor:-** *Admin can add new doctor details into the database.*
- **Add Dataset:-** *Admin can add dataset file in database.*
- **View Doctor:-** *Admin can view various Doctors along with their personal details.*
- **View Disease:-** *Admin can view various diseases details stored in database.*
- **View Patient:-** *Admin can view various patient details that had accessed the system.*
- **View Feedback:-** *Admin can view feedback provided by various users.*
  
### Technology Used:
- #### Languages:
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
  - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
- #### FrameWork:
  - ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
  - ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
- #### Machine-Learning Algorithms:
  - <a href="https://en.wikipedia.org/wiki/Gradient_boosting">**GRADIENT BOOSTING ALGORITHM**</a>
  - <a href="https://en.wikipedia.org/wiki/Logistic_regression">**LOGISTIC REGRESSION**</a>
- #### ML/DL:
  - ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  - ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
- Database:
  - ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
- #### Data-Set for training:
  - <a href="https://github.com/sandun7787/CIS-6009-Final-Project/blob/main/Machine_Learning/heart.csv">Click here for DATA-SET</a>
  - #### IDE:
  - ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
  - ![pyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
- #### OS used for testing:
  - ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
  - ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
  - ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Run Locally

Clone the project

```bash
  git clone git@github.com:sandun7787/CIS-6009-Final-Project.git
```

Go to the project directory

```bash
  cd Heart-Disease-Prediction-System
```

Start the server

```bash
  python manage.py runserver
```
## Model Training(Machine Learning)

```javascript
def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)
```
## Output Screen-shots
<img width="960" alt="Screenshot 2024-04-17 112103" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/2b8fe61c-8e6e-4f49-9026-88c674fc45a7">
<img width="960" alt="2" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/5b192307-d59e-4283-b9bc-b0a821275bf9">
<img width="960" alt="3" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/8f0241dc-d105-4123-b3ed-68a0ac6383bd">
<img width="960" alt="4" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/e186c3e1-c150-4ea7-b575-02c09379fa1e">
<img width="959" alt="5" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/ffdadedd-c12b-4e1c-b8ed-4131fd13306d">
<img width="960" alt="6" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/0333744f-f0b5-44d2-a2da-d6cd284c078a">
<img width="959" alt="7" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/47d479a7-15a8-4c32-8a31-de2dbfe0a977">

<img width="960" alt="9" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/2b3865e6-41c6-42d8-bc99-6f3cf24487bc">
<img width="960" alt="10" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/2478745e-76fe-475b-a970-311c431eac48">
<img width="960" alt="11" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/9d6f7cc3-250f-497c-a4b2-3368256af63f">
<img width="960" alt="12" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/dfd39de2-0a02-4837-ac8a-19a4000735c2">
<img width="960" alt="13" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/4e23f8f1-c618-45ae-8702-5a62a2bd0f91">
<img width="960" alt="14" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/54da31c0-cff8-4be6-8f7d-df745d2b0039">
<img width="959" alt="15" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/2c4fade7-d08f-48bb-8103-dc3dcf68e7ea">
<img width="959" alt="16" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/98ff8d5f-858c-4160-a706-5cf2555cdf12">
<img width="960" alt="17" src="https://github.com/sandun7787/CIS-6009-Final-Project/assets/75010950/9a44a347-ca95-44ed-833c-594f14450bca">

## NOTE: GitHub Pages is not working
