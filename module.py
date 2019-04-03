class cal:
    def __init__(self, former, latter):
        self.former = former
        self.latter = latter

    def add(self):
        result = self.former+self.latter
        return result

    def sub(self):
        result = self.former-self.latter
        return result

    def mul(self):
        result = self.former*self.latter
        return result

    def div(self):
        try:
            result = self.former/self.latter
            return result
        except ZeroDivisionError:
            return "0으로는 숫자를 나눌 수 없습니다."
