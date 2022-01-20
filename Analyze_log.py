import re
import pandas
import asyncio
import time

# put the log_file's filename in this function.It'll export a file called log_result.csv in the same directory after a few mins(run time depends on the size of your log file)

class Analyzer:
    def __init__(self,filename):
        self.file = filename
        self._dict = dict(device_id=[],GPS_DATE_TIME=[])

    async def str_process(self,line):
        await asyncio.sleep(0.5)
        if not line:return
        if re.search('0000000000:00:00',line):return
        if '?' not in line or '&' not in line or ' ' not in line or '=' not in line or "\\x" in line:return
        ID_data=line.split('?')[1].split(' ')[0].split('&')[0].split('=')[1]
        TIME_data=line.split('?')[1].split(' ')[0].split('&')[4].split('=')[1]
        self._dict['device_id'].append(ID_data)
        self._dict['GPS_DATE_TIME'].append(TIME_data)
        return


    async def Analyze_log(self):
        with open(self.file,'r') as file:
            for line in file:
                self.str_process(line)
            file.close()
            df=pandas.DataFrame(self._dict)
            freq=df.groupby(['device_id','GPS_DATE_TIME']).size().reset_index(name='counts')
            filter=(freq['counts']>1)
            freq[filter].to_csv('log_result.csv',index=False)

if __name__=="__main__":
    start = time.time()
    analyzer = Analyzer("nginx_log_export_20210926.txt")
    try:
        asyncio.run(analyzer.Analyze_log())
    except Exception as e:
        print(e)
    end = time.time()
    print("Time spend: ",end-start)