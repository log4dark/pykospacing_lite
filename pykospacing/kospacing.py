class Spacing:
    def __init__(self):
        pass

    def __call__(self, text):
        # 간이 띄어쓰기 보정 예제
        return text.replace("기가인턴 에", "기가 인턴에").replace("유선상품은 일 번", "유선 상품은 1번")
