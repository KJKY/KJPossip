import pandas as pd
import os
from openpyxl import load_workbook
import xlsxwriter
from shutil import copyfile

file=input('File Path: ')
extension = os.path.splitext(file)[1]
filename = os.path.splitext(file)[0]
pth=os.path.dirname(file)
newfile=os.path.join(pth,filename+'_2'+extension)
df=pd.read_excel(file, engine="openpyxl")
colpick='school'
cols=list(set(df[colpick].values))

def sendtofile(cols):
    for i in cols:
        new_df = df[['first_name', 'last_name', 'email', 'phone_number', 'child_grades', 'child_first_name','child_last_name','guardianship','language',]]
        new_df[df[colpick] == i].to_excel("{}/Clean/{}.xlsx".format(pth, i), sheet_name=i, index=False)
    print('\nCompleted')
    print('Thanks for using this program.')
    return
print(cols)
print('The Values are {} and which is {} total. Type "Y" to proceed or "N" to cancle: '.format(', '.join(cols),len(cols)))
while True:
    x=input('Ready to Proceed (Y/N): ').lower()
    if x == 'y':
        os.mkdir('{}/Clean'.format(pth))
        sendtofile(cols)
        break
    elif x=='n':
        print('\nDone!')
        break
    else: continue