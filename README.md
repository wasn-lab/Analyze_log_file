# Analyze_log_file
a small tool which can analyze repeated data in a log file

1.將你的log_file切出一部分(例如8/1~8/31)
2.和此檔案放置在同一資料夾當中
3.將切出來的log_file檔名放入此function的參數中
4.等待數秒
5.執行完畢後會匯出一份export_log_file至此資料夾中，由左至右分別是車機id、時間、重複次數
