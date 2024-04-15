class Code:
    def __init__(self):
        self.code = None
        self.point = None
        self.time = None

code, point, time = map(str, input().split())
result = Code()

result.code = code
result.point = point
result.time = time
print("secret code :", result.code)
print("meeting point :", result.point)
print("time :", result.time)