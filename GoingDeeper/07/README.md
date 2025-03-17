# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김유은
- 리뷰어 : 정상헌


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - MLM, NSP task를 통해 사전학습된 BERT 모델을 만드는데 성공하셨습니다.
      ![Image](https://github.com/user-attachments/assets/13108f25-24ba-476b-bf9e-ef3f9b794d71)  
    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - BERT 학습을 위한 is_next 라벨, 마스크 인덱스와 라벨을 적절히 구성하셨습니다.
      ![Image](https://github.com/user-attachments/assets/cd73d1fb-d62b-430b-ae40-f170e2c17da5)  
        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - validation set으로 정확도와 loss를 계산하셨습니다.
      ![Image](https://github.com/user-attachments/assets/7e864568-32a7-4b22-8747-b45b78d6fa11)  
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 훈련 결과와 분석 내용을 잘 정리해주셨습니다.
      ![Image](https://github.com/user-attachments/assets/afbcbcca-74ee-4757-8631-79eb0de70296)  
        
- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 학습 샘플 인스턴스를 생성하는 함수를 pythonic하게 구현하셨습니다.
      ![Image](https://github.com/user-attachments/assets/0eb788c8-0f90-4d4a-8714-abdc948c98e2)  


# 회고(참고 링크 및 코드 개선)
```
BERT를 학습하는 과정에서 pre-trained LM에 대해 많은 공부와 분석을 하신 것 같았습니다.
고생 많으셨습니다!
```

```bash
AIFFEL_quest_rs
├── MainQuest
│   ├── Quest01
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest02
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest03
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest04
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest05
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest06
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest07
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Quest08
│   │   ├── .ipynb
│   │   └── README.md
│   └── Quest09
│       ├── .ipynb
│       └── README.md
├── Exploration
│   ├── Ex01
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Ex02
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Ex03
│   │   ├── .ipynb
│   │   └── README.md
│   ├── Ex04
│   │   ├── .ipynb
│   │   └── README.md
│   └── Ex05
│       ├── .ipynb
│       └── README.md
└──Going Deper
.
.
.
```
