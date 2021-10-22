import re
import pandas
import time

# put the log_file's filename in this function.It'll export a file called log_result.csv in the same directory after a few mins(run time depends on the size of your log file)

def Analyze_log(filename):
    with open(filename,'r') as file:
        _dict=dict(device_id=[],GPS_DATE_TIME=[])
        for line in file:
            if not line:break
            if re.search('0000000000:00:00',line):continue
            if '?' not in line or '&' not in line or ' ' not in line or '=' not in line or "\\x" in line:continue
            ID_data=line.split('?')[1].split(' ')[0].split('&')[0].split('=')[1]
            TIME_data=line.split('?')[1].split(' ')[0].split('&')[4].split('=')[1]
            _dict['device_id'].append(ID_data)
            _dict['GPS_DATE_TIME'].append(TIME_data)
        file.close()
        df=pandas.DataFrame(_dict)
        freq=df.groupby(['device_id','GPS_DATE_TIME']).size().reset_index(name='counts')
        filter=(freq['counts']>1)
        freq[filter].to_csv('log_result.csv',index=False)