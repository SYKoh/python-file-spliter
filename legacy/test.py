input_file = "./atfExport.txt"
output_file_1 = "./atfExport 1-800000.txt"
output_file_2 = "./atfExport 800001-1600000.txt"
output_file_3 = "./atfExport 1600001-end.txt"

# 读取输入文件内容
with open(input_file, 'r') as f:
    lines = f.readlines()

# 写入输出文件1
with open(output_file_1, 'w') as f:
    f.writelines(lines[:800000])

# 写入输出文件2
with open(output_file_2, 'w') as f:
    f.writelines(lines[800001:1600000])

# 写入输出文件3
with open(output_file_3, 'w') as f:
    f.writelines(lines[1600001:])
