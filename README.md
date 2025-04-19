# PyKoSpacing Lite

TensorFlow 없이도 작동하는 초경량 한국어 띄어쓰기 보정기입니다.  
원본 [PyKoSpacing](https://github.com/haven-jeon/PyKoSpacing)에서 `TFSMLayer` 의존성을 제거하여 가볍고 설치가 쉬운 형태로 재구성되었습니다.

---

## 특징

- TensorFlow 제거 → Mac/Windows/Linux 어디서나 간편 설치
- STT 후처리, 고객센터 응답 등 간단한 띄어쓰기 보정 용도
- 예제 기반 rule 적용 (ML 기반은 아님)

---

## 설치 방법

```bash
git clone https://github.com/사용자명/pykospacing_lite.git
cd pykospacing_lite
pip install .
```

> PyPI 업로드가 아닌 소스 설치 방식입니다.

---

## 사용 예시

```python
from pykospacing import Spacing

spacing = Spacing()
text = "에이티 고객센터입니다 기가인턴 에 티비 등 유선상품은 일 번"
print(spacing(text))
# 출력: 에이티 고객센터입니다 기가 인턴에 티비 등 유선 상품은 1번
```

---

## 프로젝트 구조

```
pykospacing_lite/
├── pykospacing/
│   ├── __init__.py
│   └── kospacing.py
├── setup.py
└── README.md
```

---

## 참고

- 본 프로젝트는 ML 모델 기반이 아닌 룰 기반 예시입니다.
- 고정된 예제 문장 기준으로만 작동하므로 복잡한 상황에서는 정확도가 낮을 수 있습니다.
- 실사용 모델이 필요한 경우 원본 PyKoSpacing + TensorFlow 사용을 권장합니다.

---

## 라이선스

MIT License
