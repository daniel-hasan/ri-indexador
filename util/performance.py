import tracemalloc
from datetime import datetime
from IPython.display import clear_output
import math

class CheckTime:
    def __init__(self, count_total=None):
        self.time = datetime.now()
        self.count_total = count_total
        self.total_seconds = 0

    def reset(self):
        self.time = datetime.now()
        self.total_seconds = 0
    def finish_time(self):
        delta = datetime.now()-self.time
        self.time = datetime.now()
        return delta
    def print_delta(self, task:str ,count_done:int =None):
        delta = self.finish_time()
        str_prefix = ""
        self.total_seconds += delta.total_seconds()
        if count_done is not None:
            str_prefix = f"#{count_done} itens - "
            if self.count_total is not None :
                porc_complete = math.floor(count_done/self.count_total*100)
                print(f"{task} {porc_complete} done")
            print(f"Items per second: {count_done/self.total_seconds}")
        print(f"{str_prefix} {task} done in "+str(self.total_seconds))
        print(f"Total time elapsed: {self.total_seconds} s")
        
        


class CheckMemory:
    MEGA = 2**20
    GIGA = 2**30
    
    def __init__(self):
        tracemalloc.start()
    
    def finish(self):
        tracemalloc.stop()
    def memory_str_format(self,memory:float) -> str:
        if memory<CheckMemory.GIGA:
            return f"{memory / CheckMemory.MEGA:,} MB"
        else:
            return f"{memory / CheckMemory.GIGA:,} GB"

    def print_usage(self):
        current, peak = tracemalloc.get_traced_memory()
   
        print(f"Memoria usada: {self.memory_str_format(current)};"
                +f" Máximo {self.memory_str_format(peak)}")


class CheckPerformance:
    def __init__(self, count_total=None, clear_output=False):
        self.memory = CheckMemory()
        self.time = CheckTime(count_total)
    
    def print_step(self, task:str ,count_done:int =None):
        clear_output(wait=True)
        self.time.print_delta(task, count_done)
        self.memory.print_usage()
    
    def finish(self):
        self.memory.finish()
        self.time.reset()

