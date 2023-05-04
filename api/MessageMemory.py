from collections import deque

class Memory:
    def __init__(self, maxlen=20):
        pass
        self.maxlen = maxlen
        self.memory = deque(maxlen=self.maxlen)

    def add_message(self, new_message):
        self.memory.append(new_message)
    
    def generate_prompt(self):
        return list(self.memory)


if __name__=="__main__":
    memory = Memory(maxlen=5)
    msg_list = ["一鄉二里", "共有三父子", "不識四書五經", "竟敢教七八九子", "十分大膽", "十室九貧", "湊得八兩七錢六分五毫四里", "尚且三心二意", "一等下流"]
    for msg in msg_list:
        memory.add_message(msg)
        print(memory.memory)
        print(memory.generate_prompt())