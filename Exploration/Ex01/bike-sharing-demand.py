# (1) 데이터 가져오기
import pandas as pd

file_path = "~/data/data/bike-sharing-demand/train.csv"
train = pd.read_csv(file_path)

print(train.info())
print(train.head())

#(2) datetime 컬럼을 datetime 자료형으로 변환
train['datetime'] = pd.to_datetime(train['datetime'])

train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second

print(train[['datetime', 'year', 'month', 'day', 'hour', 'minute', 'second']].head())

# (3) year, month, day, hour, minute, second 데이터 개수 시각화하기
import seaborn as sns
import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 2, figsize=(12, 12))

sns.countplot(x='year', data=train, ax=axes[0, 0])
axes[0, 0].set_title('Year Count')

sns.countplot(x='month', data=train, ax=axes[0, 1])
axes[0, 1].set_title('Month Count')

sns.countplot(x='day', data=train, ax=axes[1, 0])
axes[1, 0].set_title('Day Count')

sns.countplot(x='hour', data=train, ax=axes[1, 1])
axes[1, 1].set_title('Hour Count')

sns.countplot(x='minute', data=train, ax=axes[2, 0])
axes[2, 0].set_title('Minute Count')

sns.countplot(x='second', data=train, ax=axes[2, 1])
axes[2, 1].set_title('Second Count')

plt.tight_layout()
plt.show()

# (4) X, y 컬럼 선택 및 train/test 데이터 분리
from sklearn.model_selection import train_test_split

X = train[['temp', 'humidity', 'windspeed', 'year', 'month', 'day', 'hour']]
y = train['count']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

#(5) LinearRegression 모델 학습
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

#(6) 학습된 모델로 X_test에 대한 예측값 출력 및 손실함수값 계산
from sklearn.metrics import mean_squared_error
import numpy as np

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MSE:", mse)
print("RMSE:", rmse)

#(7) x축은 temp 또는 humidity로, y축은 count로 예측 결과 시각화하기
# temp
plt.figure(figsize=(10, 5))
plt.scatter(X_test['temp'], y_test, label="Actual", alpha=0.5)
plt.scatter(X_test['temp'], y_pred, label="Predicted", alpha=0.5)
plt.title('Temperature vs Count')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.legend()
plt.show()

# humidity
plt.figure(figsize=(10, 5))
plt.scatter(X_test['humidity'], y_test, label="Actual", alpha=0.5)
plt.scatter(X_test['humidity'], y_pred, label="Predicted", alpha=0.5)
plt.title('Humidity vs Count')
plt.xlabel('Humidity')
plt.ylabel('Count')
plt.legend()
plt.show()
