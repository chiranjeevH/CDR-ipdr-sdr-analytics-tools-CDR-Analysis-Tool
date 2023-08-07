#%%
import os
import zipfile
import csv
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CHIRANJEEV;'
                      'Database=SAMPLE 1;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
# cursor.execute('SELECT * FROM ETC')



# for i in cursor:
#     print(i)

csvRows = []
my_dir=os.getcwd()
total=0
for path, dir_list, file_list in os.walk(my_dir+"/"):
    for file_name in file_list:

        if file_name.endswith(".zip"):
            abs_file_path = os.path.join(path, file_name)
            parent_path = os.path.split(abs_file_path)[0]
            # /media/tectum-4/Tectum/truecaller/Merged Truecaller.csv
            output_folder_name = os.path.splitext(abs_file_path)[0]
            output_path = os.path.join(parent_path, output_folder_name)
            zip_obj = zipfile.ZipFile(abs_file_path, 'r')
            csv_file=zip_obj.extractall(output_path)
            for root,subdr,files in os.walk(output_path+"/"):
                for filename_csv in files:
                    with open(os.path.join(output_path+"/")+filename_csv, newline='') as csvfile:
                        datareader = csv.reader(csvfile)
                        for row in datareader:
                            print(row)
                            total+=1
                            print(total)
                        
                        
                        phone_no, source_ip_address,	source_port,	public_ip_address,	public_ip_port	,destination_ip_address, destination_port,	start_date_time,	end_date_time,	ip_address_allocation,	user_id_iaa,	imei_no,	imsi_no,	pgw_ip_address,	access_point_name	,cell_id,	generated_time,	roaming_circle_type,	roaming_circle, session_duration, application_name,	subscriber_detail, operator_name,	is_voip = []



                        
                        for index, row in enumerate(datareader):
                            dict_data = {"phone_no": "", "source_ip_address": "", "source_port": "", "public_ip_address": "", "public_ip_port": "",
                                         "destination_ip_address": "", "destination_port": "", "start_date_time": "", "end_date_time": "", "ip_address_allocation": "",
                                         "user_id_iaa": "", "imei_no": "","imsi_no": "","pgw_ip_address": "","access_point_name": "","cell_id": "","generated_time": "","roaming_circle_type": "","roaming_circle": "","session_duration": "","application_name": "","subscriber_detail": "","operator_name": "","is_voip": "", 'phone_no': row[0], 'source_ip_address': row[1], 'source_port': row[2]}
                            try:
                                try:
                                    dict_data['phone_no']= row[0]
                                except:
                                    dict_data['phone_no']=  ""
                                try:
                                    dict_data['source_ip_address']= row[1]
                                except:
                                    dict_data['source_ip_address']= ""
                                try:
                                    dict_data['source_port']= row[2]
                                except:
                                    dict_data['source_port']= ""
                                try:
                                    dict_data['public_ip_address'] = row[3]
                                except:
                                    dict_data['public_ip_address']= ""
                                try:
                                    dict_data['public_ip_port'] = row[4]
                                except:
                                    dict_data['public_ip_port']= ""
                                try:
                                    dict_data['destination_ip_address'] = row[5]
                                except:
                                    dict_data['destination_ip_address'] = ""
                                try:
                                    dict_data['destination_port'] = row[6]
                                except:
                                    dict_data['destination_port'] = ""
                                try:
                                    dict_data['start_date_time'] = row[7]
                                except:
                                    dict_data['start_date_time'] = ""
                                try:
                                    dict_data['end_date_time'] = row[8]
                                except:
                                    dict_data['end_date_time'] = ""
                                try:
                                    dict_data['ip_address_allocation'] = row[9]
                                except:
                                    dict_data['ip_address_allocation'] = ""
                                try:
                                    dict_data['user_id_iaa'] = row[10]
                                except:
                                    dict_data['user_id_iaa'] = ""
                                try:
                                    dict_data['imei_no'] = row[11]
                                except:
                                    dict_data['imei_no'] = ""
                                try:
                                    dict_data['imsi_no'] = row[12]
                                except:
                                    dict_data['imsi_no'] = ""
                                try:
                                    dict_data['pgw_ip_address'] = row[13]
                                except:
                                    dict_data['pgw_ip_address'] = ""
                                try:
                                    dict_data['access_point_name'] = row[14]
                                except:
                                    dict_data['access_point_name'] = ""
                                try:
                                    dict_data['cell_id'] = row[15]
                                except:
                                    dict_data['cell_id'] = row[15]

                                try:
                                    dict_data['generated_time'] = row[15]
                                except:
                                    dict_data['generated_time'] = row[15]

                                try:
                                    dict_data['roaming_circle_type'] = row[15]
                                except:
                                    dict_data['roaming_circle_type'] = row[15]    
                                
                                try:
                                    dict_data['roaming_circle'] = row[15]
                                except:
                                    dict_data['roaming_circle'] = row[15]   
                                
                                try:
                                    dict_data['session_duration'] = row[15]
                                except:
                                    dict_data['session_duration'] = row[15]   
                                
                                try:
                                    dict_data['application_name'] = row[15]
                                except:
                                    dict_data['application_name'] = row[15]   
                                
                                try:
                                    dict_data['subscriber_detail'] = row[15]
                                except:
                                    dict_data['subscriber_detail'] = row[15]   
                                
                                try:
                                    dict_data['operator_name'] = row[15]
                                except:
                                    dict_data['operator_name'] = row[15]   

                                try:
                                    dict_data['is_voip'] = row[15]
                                except:
                                    dict_data['is_voip'] = row[15]       


                                
                                #print(dict_data)
                                csvRows.insert_one(dict_data)
                                #print(index)
                                print(index)

                            except Exception as e:
                                print(row)


                        conn.commit()
                        conn.close()







