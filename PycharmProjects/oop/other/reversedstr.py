class ReverseStr(str):
    def __new__(cls, *args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

