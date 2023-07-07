import psutil as ps
import pandas as pd
class Process_kill:
    def __init__(self, process_name):
        self.process_name = process_name

    def when_started(self):

        try:
            p = []
            for proc in ps.process_iter():
            # check whether the process name matches
                if proc.name() == self.process_name:
                    pass
                    
                    # print(f"{proc}")
                    # print(f"The process is {proc.status()}")
            # var = p.split("")
                    p.append(str(proc))
            table = []
            for event in p:
                new_event = event.split("(")[1]
                new_event = new_event.split(")")[0]
                new_event_list = new_event.split(",")
                pid = new_event_list[0].split("=")[1]
                name = new_event_list[1].split("=")[1]
                status = new_event_list[2].split("=")[1]
                started = new_event_list[3].split("=")[1]
                data = {"pid": pid,
                            "name": name,
                            "status": status,
                            "started": started}
                table.append(data)
            df = pd.DataFrame(table)
            print(df)
                # print(f"{pid}, {new_event_list[1]}, {new_event_list[3]}")
            # print(f"data needed --> {type(proc)}")
            # print(f"data needed --> {proc}")
        except ps.NoSuchProcess:
            return print(f"Process {self.process_name} is not running ")
           
    def get_pid(self):   
        try:
            pids = [p for p in ps.pids() if ps.Process(p).name() == self.process_name] 
            print(f"The Process id of {self.process_name} is {pids}")
        except Exception as e:
            print(f"the process is in exeption {e}")

    def __str__(self,m):
        # print(f"The process is kill and the status of {self.process_name.__name__}")
        print(f"The process to {m.__name__}")
        self.kill_process_id()

    
    def get_process_name(self):
        try:
            for proc in ps.process_iter():
            # check whether the process name matches
                if proc.name() == self.process_name:
                    print(f"The Process name id {proc.name()}")
                    print(f"The process is {proc.status()}")
        except ps.NoSuchProcess:
            return print(f"No Process is running {self.process_name}")
        # try:
        #     process = ps.Process(pid)
        #     process_name = process.name()
        #     print("Process Name:", process_name)
        # except ps.NoSuchProcess:
        #     print("Process not found.")
    def kill_process_id(self):
        for proc in ps.process_iter():
        # check whether the process name matches
            if proc.name() == self.process_name:
                proc.kill()
                print(f"{proc.status}")
                # print(f"{proc.name()}")


pname = Process_kill("SourceTree.exe")
pname.when_started()
pname.get_pid()
pname.get_process_name() 
pname.kill_process_id()

# pname.process_name