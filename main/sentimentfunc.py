import pickle as pkl

file1 = "models.pkl"
fileobj1 = open(file1, 'rb')
data = pkl.load(fileobj1)
model = data['model']
vectorizer = data['vectorizer']