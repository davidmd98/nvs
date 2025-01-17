import argparse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

RANDOM_STATE = 0
N_NEIGHBORS = 3

X_train, X_test, y_train, y_test, y_pred = (None,) * 5
model = KNeighborsClassifier(n_neighbors=N_NEIGHBORS)

def load(dataset=load_iris):
    global X_train, X_test, y_train, y_test
    x, y = dataset(return_X_y=True, as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=RANDOM_STATE)
    
def fit():
    global model, X_train, y_train
    print(X_test.head())
    print(y_test.head())
    model.fit(X_train, y_train)

def predict():
    global y_pred
    if X_test is None: raise TypeError("Test data (X_test) is None.")
    if model is None: raise TypeError("Model is None.")
    y_pred = model.predict(X_test)
    
def main():
    parser = argparse.ArgumentParser(description="") 
    parser.add_argument('function', type=str, help="The function to execute") 
    args = parser.parse_args() 
    
    if args.function == 'train': 
        fit() 
    elif args.function == 'pred': 
        predict() 
    elif args.function == 'load':
        load()
    else: 
        print(f"Unknown function: {args.function}")

if __name__=="__main__":
    main()