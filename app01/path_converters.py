class MonthConverter:
    regex = '\d{2}'

    def to_python(self, value):
        print('===>to_python run')
        return int(value)

    def to_url(self, value):
        print('===>to_url run')
        return value

