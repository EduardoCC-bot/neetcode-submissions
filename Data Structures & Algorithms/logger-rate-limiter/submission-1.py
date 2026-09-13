class Logger:

    def __init__(self):
        self.hashMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hashMap:
            if self.hashMap[message] <= timestamp:
                self.hashMap[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.hashMap[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

"""
{
    "foo" : 21,
    "bar" : 12
}

validate if the key exist O(1)

value of the key plus 10 is <= timestamp
    "foo" : 3
     11 <= 3

    "bar" : 8
    12 <= 8

    "foo" : 11
    11 <= 11 

"""