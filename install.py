#!/usr/bin/env python
# coding: utf-8

# # JupyterLab in Buisness Application Studio by Edgar
# 
# to run this script from command line use "jupyter nbconvert --to notebook --execute notebook.ipynb"

# ## preprocessing

# In[1]:


import os
import shutil
import re
import socket
from pathlib import Path

#TOOLS
#
#use this to remove lines containing a specific string in a file
def fileremovelinescontainingstring(myfile,mystring):
    # Writing to file
    file1 = open(myfile, 'r')
    file1lines = file1.readlines()
    file1.close()
    file1 = open(myfile, 'w')
    for line in file1lines:
        if not mystring in line:
            file1.write(line)
    file1.close()
   
def fileaddlineifnotinfile(filename,needle):
    Path(filename).touch(exist_ok=True)
    with open(filename, "r+") as file:
        for line in file:
            if needle in line:
               break
        else: # not found, we are at the eof
            file.write(needle) # append missing data

def getnpmpackageversion(packagename):
    return re.findall('('+packagename+'@(\d+\.\d+\.\d+))+|$', os.popen("npm list").read())[0][1]

def getpippackageversion(packagename):
    return re.findall('('+packagename+'==(\d+\.\d+\.\d+))+|$', os.popen("pip freeze").read())[0][1]

def gettoolversion(command):
    return re.findall('(\d+\.\d+\.\d+)+|$', os.popen(command).read())[0]

if not "WORKSPACE" in os.environ:
    os.environ["WORKSPACE"] = os.getcwd()
os.chdir(os.environ["WORKSPACE"])
os.system("echo WORKSPACE: "+os.environ["WORKSPACE"])

if not os.environ["WORKSPACE"]+"/.local/.bin" in os.environ["PATH"]: 
    os.environ["PATH"] = os.environ["WORKSPACE"]+"/local/.bin" + os.pathsep + os.environ["PATH"]
os.system("echo PATH: "+os.environ["PATH"])


# ## user vim as code editor

# In[2]:


fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"export GIT_EDITOR=vim\n")
os.system('export GIT_EDITOR=vim')


# ## download pip package management

# In[3]:


os.system('curl -LO https://bootstrap.pypa.io/get-pip.py')
os.system('python3 get-pip.py')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"export PATH=/home/user/.local/bin:$PATH\n")
os.system('export PATH=/home/user/.local/bin:$PATH')


# ## install jupyter

# In[4]:


os.system('pip install jupyter')


# ## generate jupyter config

# In[5]:


os.system('echo y | jupyter notebook --generate-config')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"alias jupyterlab='jupyter-lab --ip=127.0.0.1 --port 8702'\n")
os.system('alias jupyterlab="jupyter-lab --ip=127.0.0.1 --port 8702"')


# ## add access url config to jupyter config

# In[6]:


import os
import socket
print("hostname: "+socket.gethostname())
hostname_array = socket.gethostname().split('-')
origin = 'https://port8702-'+hostname_array[0]+'-'+hostname_array[1]+'-'+hostname_array[2]+'.eu10.applicationstudio.cloud.sap'
print("origin: "+origin)
with open(os.path.expanduser('~/.jupyter/jupyter_notebook_config.py'), 'a') as file:
    file.write('\nc.ServerApp.allow_origin = \''+origin+'\'')


# ## install jupyterlab

# In[7]:


os.system('pip install jupyterlab')


# ## create README.md

# In[8]:


os.system('jupyter nbconvert --to Markdown notebook.ipynb && cp notebook.md README.md')


# ## create install.py

# In[9]:


os.system('jupyter nbconvert --to python notebook.ipynb && cp notebook.py install.py')


# ## run jupyterlab
# 
# run jupyter-lab with port 8702 using command "jupyterlab"
