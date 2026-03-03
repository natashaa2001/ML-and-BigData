import time
class Profiler:
    def __init__(self):
        self.logs=[]
    def start(self,name):
        self.logs.append({'name':name,'start':time.time()})
    def stop(self):
        self.logs[-1]['end']=time.time()
        self.logs[-1]['duration']=self.logs[-1]['end']-self.logs[-1]['start']
    def report(self):
        for l in self.logs:
            print(f"{l['name']}: {l['duration']:.2f}s")
