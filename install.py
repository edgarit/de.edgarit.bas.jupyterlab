#!/usr/bin/env python
# coding: utf-8

# # JupyterLab in Buisness Application Studio by Edgar

# ## user vim as code editor

# In[ ]:


import os
os.chdir(os.path.expanduser('~'))
os.system('echo "export GIT_EDITOR=vim" >> .bashrc')
os.system('source ~/.bashrc')


# ## download pip package management

# In[ ]:


os.system('curl -LO https://bootstrap.pypa.io/get-pip.py')
os.system('python3 get-pip.py')
os.system('echo "export PATH=/home/user/.local/bin:$PATH" >> .bashrc')
os.system('source ~/.bashrc')


# ## install jupyter

# In[ ]:


os.system('pip install jupyter')


# ## generate jupyter config

# In[ ]:


os.system('jupyter notebook --generate-config')


# ## add access url config to jupyter config

# In[ ]:


import os
import socket
print("hostname: "+socket.gethostname())
hostname_array = socket.gethostname().split('-')
origin = 'https://port8702-'+hostname_array[0]+'-'+hostname_array[1]+'-'+hostname_array[2]+'.eu10.applicationstudio.cloud.sap'
print("origin: "+origin)
with open(os.path.expanduser('~/.jupyter/jupyter_notebook_config.py'), 'a') as file:
    file.write('\nc.ServerApp.allow_origin = \''+origin+'\'')


# ## install jupyterlab

# In[ ]:


os.system('pip install jupyterlab')


# ## create README.md

# In[ ]:


#jupyter nbconvert --to Markdown notebook.ipynb
#cp notebook.md README.md 


# ## create install.py

# In[ ]:


#jupyter nbconvert --to python notebook.ipynb
#cp notebook.py install.py


# ## run jupyterlab

# In[ ]:


os.system('jupyter-lab')

