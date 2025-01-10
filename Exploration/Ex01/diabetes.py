#(1) 데이터 가져오기
from sklearn.datasets import load_diabetes
import numpy as np

diabetes = load_diabetes()

#(2~3) 모델에 입력할 데이터 X, Y 준비하기
df_X=diabetes.data
df_y=diabetes.target

df_X.shape,df_y.shape

df_X=np.array(df_X)
df_y=np.array(df_y)

#(4) train 데이터와 test 데이터로 분리하기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=42
                                                   
num_features = X_train.shape[1]

W = np.random.rand(num_features)
b = np.random.rand())

#(5) 모델 준비하기
def model(X, W, b):
  predictions = 0
  for i in range(len(W)):
    predictions += X[:, i] * W[i]
  predictions += b
  return predictions

#(6) 손실함수 loss 정의하기
def MSE(a,b):
  mse=((a-b)**2).mean()
  return mse

def loss(X, W, b, y):
    predictions = model(X, W, b)
    L = MSE(predictions, y)
    return L

# (7) 기울기를 구하는 gradient 함수 구현하기
def gradient(X, W, b, y):
    N = len(y)

    y_pred = model(X, W, b)

    dW = 1/N * 2 * X.T.dot(y_pred - y)

    db = 2 * (y_pred - y).mean()
    return dW, db

dW, db = gradient(X_train, W, b, y_train)
print("dW:", dW)
print("db:", db)

#(8) 하이퍼 파라미터인 학습률 설정하기
learning_rate=0.5

# (9) 모델 학습하기
losses=[]

for i in range(1,1001):
  dw,db=gradient(X_train,W,b,y_train)
  W -= learning_rate*dw
  b -= learning_rate*db
  L = loss(X_train, W, b, y_train)
  losses.append(L)
  if i % 100 == 0:
    print('Iteration %d : Loss %0.4f' % (i, L))
    
#(10) test 데이터에 대한 성능 확인하기
#(11) 정답 데이터와 예측한 데이터 시각화하기
import matplotlib.pyplot as plt
plt.plot(losses)
plt.show()

prediction = model(X_test, W, b)
mse = loss(X_test, W, b, y_test)
mse

plt.scatter(X_test[:, 0], y_test)
plt.scatter(X_test[:, 0], prediction)
plt.show()
