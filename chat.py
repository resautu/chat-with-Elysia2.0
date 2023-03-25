import json
import os
import logging
import platform
from transformers import AutoTokenizer, AutoModel
import json
#logging.setLevel(logging.WARNING)
class GenerateText:
    model = None
    tokenizer = None
    history = []
    message_list = []
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("chatglm-model", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("chatglm-model", trust_remote_code=True).half().cuda()
        self.model = self.model.eval()
    def updateMessageList(self, history: list):
        if history == None:
            return
        new_text, new_message = history[-1]
        self.message_list.append({'user' : new_text, "chater": new_message})
    def uploadHistory(self, historyFile):
        try:
            with open(historyFile, 'r', encoding='utf-8') as fs:
                self.message_list = json.load(fs)
            self.history = [(item['user'], item['chater']) for item in self.message_list]
        except FileNotFoundError:
            logging.error('history not found!!!')
    def getText(self, text : str, max_length, top_p, temperature) -> str:
        try:
            response, self.history = self.model.chat(self.tokenizer, text, history=self.history, max_length=max_length, top_p=top_p, temperature=temperature)
        except:
            logging.error('interaction with chat error!!')
            return '好像出错了...'
        self.message_list.append({"user": text, "chater" : response})
        return response
#if __name__ == '__main__':
#    gt = GenerateText()
#    print(gt.getText('请做一下自我介绍'))
