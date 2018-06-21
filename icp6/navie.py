from sklearn.linear_model import LogisticRegression
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB

irisdatasets = datasets.load_iris()
x = irisdatasets.data
y = irisdatasets.target

# split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = GaussianNB()
model.fit(x, y)
y_pred = model.predict(x_test)
print(model.score(x, y))
print('Accuracy',metrics.accuracy_score(y_test, y_pred))
print('Precision',metrics.precision_score(y_test, y_pred,average='weighted'))
print('Recall',metrics.recall_score(y_test, y_pred, average='weighted'))