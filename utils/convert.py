
import pandas as pd
import shutil
import os

def pack_all_to_excel(folder: str, save_as: str):
    if True == os.path.exists(save_as):
        os.remove(save_as)

    writer = pd.ExcelWriter(save_as, engine = 'xlsxwriter')
    for csv_name in os.listdir(folder):
        csv_path = folder + '/' + csv_name
        if '.DS_Store' == csv_name:
            continue
        if '__log__.csv' == csv_name:
            continue

        if os.path.isfile(csv_path):
            sheet_name = csv_name[:-4]
            if 30 < len(csv_path):
                temp_path = folder + '/__temp__.csv'
                shutil.copy(csv_path, temp_path)

                csv = pd.read_csv(temp_path)
                csv.to_excel(writer, sheet_name = sheet_name)
                ##print('!!!!!!!: ' + csv_path)
                os.remove(temp_path)
            else:
                csv = pd.read_csv(csv_path)
                csv.to_excel(writer, sheet_name = sheet_name)
                ##print('         ' + csv_path)

    log_path = folder + '/__log__.csv'
    csv = pd.read_csv(log_path)
    csv.to_excel(writer, sheet_name = 'LOG')
            
    writer.save()

def csv_to_xlsx():
    # 列出指定路徑底下所有檔案(包含資料夾)
    result_folder = os.getcwd() + '/result/'
    for folder_name in os.listdir(result_folder):
        from_folder = 'result/' + folder_name
        if os.path.isdir(from_folder):
            save_to_file = from_folder + '.xlsx'
            pack_all_to_excel(from_folder, save_to_file)

            
    #csv = pd.read_csv('1.csv', encoding='utf-8')
    #csv.to_excel('1.xlsx', sheet_name='data')
