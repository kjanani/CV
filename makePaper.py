import os,sys

filename = 'cv_teaching';
string_latex = 'latex '+filename+'.tex'
string_dviToPDF = 'dvipdf '+filename+'.dvi'
string_remove1 = 'rm *.aux'
#string_remove2 = 'rm *.bbl'
string_remove2 = ''
string_remove3 = 'rm *.log'
string_remove4 = 'rm *.out'
string_remove5 = 'rm *.blg'

os.system(string_latex);
os.system(string_latex);
os.system(string_dviToPDF);
os.system(string_remove1);
os.system(string_remove2);
os.system(string_remove3);
os.system(string_remove4);
os.system(string_remove5);