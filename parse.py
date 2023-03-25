import os
import datetime
import json
from soundMaker import GenerateSound
from chat import GenerateText
import logging
class Parse:
    role_name = ''
    gt = None
    store_path = ''
    begin_time = ''
    file_name = ''
    cnt = 0
    gs = None
    def __init__(self) -> None:
        with open('./config.json', 'r', encoding='utf-8') as inform:
            config = json.load(inform)
            self.role_name = config["name"]
            self.store_path = config["store-path"]
            if not os.path.exists(self.store_path):
                os.mkdir(self.store_path)
        self.gt = GenerateText()
        self.gs = GenerateSound()
        date = datetime.datetime.now()
        self.file_name = date.strftime('%Y-%m-%d-%H-%M-%S')
        self.store_path = self.store_path + '/' + self.file_name
        os.mkdir(self.store_path)
        if not os.path.exists('./data/default.json'):
            logging.error('default file not found')
            exit(-1)
        self.gt.uploadHistory('./data/default.json')
    def loadHistory(self, history_file):
        self.gt.uploadHistory(history_file.name)
        logging.debug("load history successfully!!")
    def logContent(self):
        with open(self.store_path + './content.json', 'w', encoding='utf-8') as fs:
            json.dump(self.gt.message_list, fs, ensure_ascii=False, indent=2)
    def getText(self, text, max_length, top_p, temperature):
        result = self.gt.getText(text, max_length, top_p, temperature)
        if result == None:
            exit()
        return result
    def switchAudio(self, text, ns, nsw, ls):
        audio_path = self.store_path + '/' + str(self.cnt) + '.wav'
        self.cnt += 1
        self.gs.generateSound(text, audio_path, ns, nsw, ls)
        logging.warning('text change to audio successfully!')
        return text, audio_path
    def PipeChat(self, text, max_length, top_p, temperature, ns, nsw, ls):
        return self.switchAudio(self.getText(text, max_length, top_p, temperature), ns, nsw, ls)
if __name__ == '__main__':
    ps = Parse()
    ps.makeChat()