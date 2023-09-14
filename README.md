# JupyterLab in Buisness Application Studio by Edgar

to run this script from command line use "jupyter nbconvert --to notebook --execute notebook.ipynb"

## preprocessing


```python
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
```

    WORKSPACE: /home/user/projects/de.edgarit.bas.jupyterlab
    PATH: /home/user/projects/de.edgarit.bas.jupyterlab/local/.bin:/home/user/.local/bin:/home/user/.node_modules_global/bin:/home/user/.local/bin:/extbin/bin:/extbin/npm/docker/bin:/extbin/npm/globals/bin:/extbin/globals/pnpm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin





    0



## user vim as code editor


```python
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"export GIT_EDITOR=vim\n")
os.system('export GIT_EDITOR=vim')
```




    0



## download pip package management


```python
os.system('curl -LO https://bootstrap.pypa.io/get-pip.py')
os.system('python3 get-pip.py')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"export PATH=/home/user/.local/bin:$PATH\n")
os.system('export PATH=/home/user/.local/bin:$PATH')
```

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100 2544k  100 2544k    0     0  44.5M      0 --:--:-- --:--:-- --:--:-- 44.3M


    Defaulting to user installation because normal site-packages is not writeable
    Collecting pip
      Obtaining dependency information for pip from https://files.pythonhosted.org/packages/50/c2/e06851e8cc28dcad7c155f4753da8833ac06a5c704c109313b8d5a62968a/pip-23.2.1-py3-none-any.whl.metadata
      Using cached pip-23.2.1-py3-none-any.whl.metadata (4.2 kB)
    Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 23.2.1
        Uninstalling pip-23.2.1:
          Successfully uninstalled pip-23.2.1
    Successfully installed pip-23.2.1





    0



## install jupyter


```python
os.system('pip install jupyter')
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: jupyter in /home/user/.local/lib/python3.9/site-packages (1.0.0)
    Requirement already satisfied: notebook in /home/user/.local/lib/python3.9/site-packages (from jupyter) (7.0.3)
    Requirement already satisfied: qtconsole in /home/user/.local/lib/python3.9/site-packages (from jupyter) (5.4.4)
    Requirement already satisfied: jupyter-console in /home/user/.local/lib/python3.9/site-packages (from jupyter) (6.6.3)
    Requirement already satisfied: nbconvert in /home/user/.local/lib/python3.9/site-packages (from jupyter) (7.8.0)
    Requirement already satisfied: ipykernel in /home/user/.local/lib/python3.9/site-packages (from jupyter) (6.25.2)
    Requirement already satisfied: ipywidgets in /home/user/.local/lib/python3.9/site-packages (from jupyter) (8.1.0)
    Requirement already satisfied: comm>=0.1.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.4)
    Requirement already satisfied: debugpy>=1.6.5 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (1.8.0)
    Requirement already satisfied: ipython>=7.23.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (8.15.0)
    Requirement already satisfied: jupyter-client>=6.1.12 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (8.3.1)
    Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.3.1)
    Requirement already satisfied: matplotlib-inline>=0.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.6)
    Requirement already satisfied: nest-asyncio in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (1.5.7)
    Requirement already satisfied: packaging in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (23.1)
    Requirement already satisfied: psutil in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.9.5)
    Requirement already satisfied: pyzmq>=20 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (25.1.1)
    Requirement already satisfied: tornado>=6.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (6.3.3)
    Requirement already satisfied: traitlets>=5.4.0 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.9.0)
    Requirement already satisfied: widgetsnbextension~=4.0.7 in /home/user/.local/lib/python3.9/site-packages (from ipywidgets->jupyter) (4.0.8)
    Requirement already satisfied: jupyterlab-widgets~=3.0.7 in /home/user/.local/lib/python3.9/site-packages (from ipywidgets->jupyter) (3.0.8)
    Requirement already satisfied: prompt-toolkit>=3.0.30 in /home/user/.local/lib/python3.9/site-packages (from jupyter-console->jupyter) (3.0.39)
    Requirement already satisfied: pygments in /home/user/.local/lib/python3.9/site-packages (from jupyter-console->jupyter) (2.16.1)
    Requirement already satisfied: beautifulsoup4 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (4.12.2)
    Requirement already satisfied: bleach!=5.0.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (6.0.0)
    Requirement already satisfied: defusedxml in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.7.1)
    Requirement already satisfied: importlib-metadata>=3.6 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (6.8.0)
    Requirement already satisfied: jinja2>=3.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (3.1.2)
    Requirement already satisfied: jupyterlab-pygments in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.2.2)
    Requirement already satisfied: markupsafe>=2.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (2.1.3)
    Requirement already satisfied: mistune<4,>=2.0.3 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (3.0.1)
    Requirement already satisfied: nbclient>=0.5.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.8.0)
    Requirement already satisfied: nbformat>=5.7 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (5.9.2)
    Requirement already satisfied: pandocfilters>=1.4.1 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (1.5.0)
    Requirement already satisfied: tinycss2 in /home/user/.local/lib/python3.9/site-packages (from nbconvert->jupyter) (1.2.1)
    Requirement already satisfied: jupyter-server<3,>=2.4.0 in /home/user/.local/lib/python3.9/site-packages (from notebook->jupyter) (2.7.3)
    Requirement already satisfied: jupyterlab-server<3,>=2.22.1 in /home/user/.local/lib/python3.9/site-packages (from notebook->jupyter) (2.25.0)
    Requirement already satisfied: jupyterlab<5,>=4.0.2 in /home/user/.local/lib/python3.9/site-packages (from notebook->jupyter) (4.0.5)
    Requirement already satisfied: notebook-shim<0.3,>=0.2 in /home/user/.local/lib/python3.9/site-packages (from notebook->jupyter) (0.2.3)
    Requirement already satisfied: ipython-genutils in /home/user/.local/lib/python3.9/site-packages (from qtconsole->jupyter) (0.2.0)
    Requirement already satisfied: qtpy>=2.4.0 in /home/user/.local/lib/python3.9/site-packages (from qtconsole->jupyter) (2.4.0)
    Requirement already satisfied: six>=1.9.0 in /home/user/.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert->jupyter) (1.16.0)
    Requirement already satisfied: webencodings in /home/user/.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert->jupyter) (0.5.1)
    Requirement already satisfied: zipp>=0.5 in /home/user/.local/lib/python3.9/site-packages (from importlib-metadata>=3.6->nbconvert->jupyter) (3.16.2)
    Requirement already satisfied: backcall in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.2.0)
    Requirement already satisfied: decorator in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.19.0)
    Requirement already satisfied: pickleshare in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.7.5)
    Requirement already satisfied: stack-data in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.6.2)
    Requirement already satisfied: typing-extensions in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.7.1)
    Requirement already satisfied: exceptiongroup in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (1.1.3)
    Requirement already satisfied: pexpect>4.3 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.8.0)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/user/.local/lib/python3.9/site-packages (from jupyter-client>=6.1.12->ipykernel->jupyter) (2.8.2)
    Requirement already satisfied: platformdirs>=2.5 in /home/user/.local/lib/python3.9/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel->jupyter) (3.10.0)
    Requirement already satisfied: anyio>=3.1.0 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (4.0.0)
    Requirement already satisfied: argon2-cffi in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (23.1.0)
    Requirement already satisfied: jupyter-events>=0.6.0 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.7.0)
    Requirement already satisfied: jupyter-server-terminals in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.4.4)
    Requirement already satisfied: overrides in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (7.4.0)
    Requirement already satisfied: prometheus-client in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.17.1)
    Requirement already satisfied: send2trash>=1.8.2 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (1.8.2)
    Requirement already satisfied: terminado>=0.8.3 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.17.1)
    Requirement already satisfied: websocket-client in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (1.6.3)
    Requirement already satisfied: async-lru>=1.0.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.0.4)
    Requirement already satisfied: jupyter-lsp>=2.0.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.2.0)
    Requirement already satisfied: tomli in /home/user/.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.0.1)
    Requirement already satisfied: babel>=2.10 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.12.1)
    Requirement already satisfied: json5>=0.9.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.9.14)
    Requirement already satisfied: jsonschema>=4.18.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (4.19.0)
    Requirement already satisfied: requests>=2.31 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.31.0)
    Requirement already satisfied: fastjsonschema in /home/user/.local/lib/python3.9/site-packages (from nbformat>=5.7->nbconvert->jupyter) (2.18.0)
    Requirement already satisfied: wcwidth in /home/user/.local/lib/python3.9/site-packages (from prompt-toolkit>=3.0.30->jupyter-console->jupyter) (0.2.6)
    Requirement already satisfied: soupsieve>1.2 in /home/user/.local/lib/python3.9/site-packages (from beautifulsoup4->nbconvert->jupyter) (2.5)
    Requirement already satisfied: idna>=2.8 in /home/user/.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /home/user/.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (1.3.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in /home/user/.local/lib/python3.9/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyter) (0.8.3)
    Requirement already satisfied: attrs>=22.2.0 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (23.1.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2023.7.1)
    Requirement already satisfied: referencing>=0.28.4 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.30.2)
    Requirement already satisfied: rpds-py>=0.7.1 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.10.2)
    Requirement already satisfied: python-json-logger>=2.0.4 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (2.0.7)
    Requirement already satisfied: pyyaml>=5.3 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (6.0.1)
    Requirement already satisfied: rfc3339-validator in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (0.1.4)
    Requirement already satisfied: rfc3986-validator>=0.1.1 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (0.1.1)
    Requirement already satisfied: ptyprocess>=0.5 in /home/user/.local/lib/python3.9/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel->jupyter) (0.7.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (3.2.0)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2023.7.22)
    Requirement already satisfied: argon2-cffi-bindings in /home/user/.local/lib/python3.9/site-packages (from argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (21.2.0)
    Requirement already satisfied: executing>=1.2.0 in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (1.2.0)
    Requirement already satisfied: asttokens>=2.1.0 in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (2.4.0)
    Requirement already satisfied: pure-eval in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (0.2.2)
    Requirement already satisfied: fqdn in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.5.1)
    Requirement already satisfied: isoduration in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (20.11.0)
    Requirement already satisfied: jsonpointer>1.13 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.4)
    Requirement already satisfied: uri-template in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.3.0)
    Requirement already satisfied: webcolors>=1.11 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.13)
    Requirement already satisfied: cffi>=1.0.1 in /home/user/.local/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (1.15.1)
    Requirement already satisfied: pycparser in /home/user/.local/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (2.21)
    Requirement already satisfied: arrow>=0.15.0 in /home/user/.local/lib/python3.9/site-packages (from isoduration->jsonschema>=4.18.0->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.2.3)





    0



## generate jupyter config


```python
os.system('echo y | jupyter notebook --generate-config')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"alias jupyterlab='jupyter-lab --ip=127.0.0.1 --port 8702'\n")
os.system('alias jupyterlab="jupyter-lab --ip=127.0.0.1 --port 8702"')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),'''alias baslab='if [[ $(netstat -tulpn | grep LISTEN | grep :8702) ]]; then echo jupyterlab is running && jupyter notebook list; else python3 /home/user/projects/de.edgarit.bas.jupyterlab/install.py && jupyterlab; fi'\n''')
os.system('''alias baslab='if [[ $(netstat -tulpn | grep LISTEN | grep :8702) ]]; then echo jupyterlab is running && jupyter notebook list; else python3 /home/user/projects/de.edgarit.bas.jupyterlab/install.py && jupyterlab; fi'\n''')
```

    Overwrite /home/user/.jupyter/jupyter_notebook_config.py with default config? [y/N]Writing default config to: /home/user/.jupyter/jupyter_notebook_config.py





    0



## add access url config to jupyter config


```python
import os
import socket
print("hostname: "+socket.gethostname())
hostname_array = socket.gethostname().split('-')
origin = 'https://port8702-'+hostname_array[0]+'-'+hostname_array[1]+'-'+hostname_array[2]+'.eu10.applicationstudio.cloud.sap'
print("origin: "+origin)
with open(os.path.expanduser('~/.jupyter/jupyter_notebook_config.py'), 'a') as file:
    file.write('\nc.ServerApp.allow_origin = \''+origin+'\'')
```

    hostname: workspaces-ws-gv86h-deployment-6d4ffc56b9-njlgt
    origin: https://port8702-workspaces-ws-gv86h.eu10.applicationstudio.cloud.sap


## install jupyterlab


```python
os.system('pip install jupyterlab')
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: jupyterlab in /home/user/.local/lib/python3.9/site-packages (4.0.5)
    Requirement already satisfied: async-lru>=1.0.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (2.0.4)
    Requirement already satisfied: importlib-metadata>=4.8.3 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (6.8.0)
    Requirement already satisfied: ipykernel in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (6.25.2)
    Requirement already satisfied: jinja2>=3.0.3 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (3.1.2)
    Requirement already satisfied: jupyter-core in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (5.3.1)
    Requirement already satisfied: jupyter-lsp>=2.0.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (2.2.0)
    Requirement already satisfied: jupyter-server<3,>=2.4.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (2.7.3)
    Requirement already satisfied: jupyterlab-server<3,>=2.19.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (2.25.0)
    Requirement already satisfied: notebook-shim>=0.2 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (0.2.3)
    Requirement already satisfied: packaging in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (23.1)
    Requirement already satisfied: tomli in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (2.0.1)
    Requirement already satisfied: tornado>=6.2.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (6.3.3)
    Requirement already satisfied: traitlets in /home/user/.local/lib/python3.9/site-packages (from jupyterlab) (5.9.0)
    Requirement already satisfied: typing-extensions>=4.0.0 in /home/user/.local/lib/python3.9/site-packages (from async-lru>=1.0.0->jupyterlab) (4.7.1)
    Requirement already satisfied: zipp>=0.5 in /home/user/.local/lib/python3.9/site-packages (from importlib-metadata>=4.8.3->jupyterlab) (3.16.2)
    Requirement already satisfied: MarkupSafe>=2.0 in /home/user/.local/lib/python3.9/site-packages (from jinja2>=3.0.3->jupyterlab) (2.1.3)
    Requirement already satisfied: anyio>=3.1.0 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (4.0.0)
    Requirement already satisfied: argon2-cffi in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (23.1.0)
    Requirement already satisfied: jupyter-client>=7.4.4 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (8.3.1)
    Requirement already satisfied: jupyter-events>=0.6.0 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.7.0)
    Requirement already satisfied: jupyter-server-terminals in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.4.4)
    Requirement already satisfied: nbconvert>=6.4.4 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (7.8.0)
    Requirement already satisfied: nbformat>=5.3.0 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (5.9.2)
    Requirement already satisfied: overrides in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (7.4.0)
    Requirement already satisfied: prometheus-client in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.17.1)
    Requirement already satisfied: pyzmq>=24 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (25.1.1)
    Requirement already satisfied: send2trash>=1.8.2 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (1.8.2)
    Requirement already satisfied: terminado>=0.8.3 in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.17.1)
    Requirement already satisfied: websocket-client in /home/user/.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (1.6.3)
    Requirement already satisfied: platformdirs>=2.5 in /home/user/.local/lib/python3.9/site-packages (from jupyter-core->jupyterlab) (3.10.0)
    Requirement already satisfied: babel>=2.10 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (2.12.1)
    Requirement already satisfied: json5>=0.9.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (0.9.14)
    Requirement already satisfied: jsonschema>=4.18.0 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (4.19.0)
    Requirement already satisfied: requests>=2.31 in /home/user/.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (2.31.0)
    Requirement already satisfied: comm>=0.1.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (0.1.4)
    Requirement already satisfied: debugpy>=1.6.5 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (1.8.0)
    Requirement already satisfied: ipython>=7.23.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (8.15.0)
    Requirement already satisfied: matplotlib-inline>=0.1 in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (0.1.6)
    Requirement already satisfied: nest-asyncio in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (1.5.7)
    Requirement already satisfied: psutil in /home/user/.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (5.9.5)
    Requirement already satisfied: idna>=2.8 in /home/user/.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (3.4)
    Requirement already satisfied: sniffio>=1.1 in /home/user/.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (1.3.0)
    Requirement already satisfied: exceptiongroup>=1.0.2 in /home/user/.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (1.1.3)
    Requirement already satisfied: backcall in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.2.0)
    Requirement already satisfied: decorator in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.19.0)
    Requirement already satisfied: pickleshare in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.7.5)
    Requirement already satisfied: prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (3.0.39)
    Requirement already satisfied: pygments>=2.4.0 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (2.16.1)
    Requirement already satisfied: stack-data in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.6.2)
    Requirement already satisfied: pexpect>4.3 in /home/user/.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (4.8.0)
    Requirement already satisfied: attrs>=22.2.0 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (23.1.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (2023.7.1)
    Requirement already satisfied: referencing>=0.28.4 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (0.30.2)
    Requirement already satisfied: rpds-py>=0.7.1 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (0.10.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in /home/user/.local/lib/python3.9/site-packages (from jupyter-client>=7.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (2.8.2)
    Requirement already satisfied: python-json-logger>=2.0.4 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (2.0.7)
    Requirement already satisfied: pyyaml>=5.3 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (6.0.1)
    Requirement already satisfied: rfc3339-validator in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (0.1.4)
    Requirement already satisfied: rfc3986-validator>=0.1.1 in /home/user/.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (0.1.1)
    Requirement already satisfied: beautifulsoup4 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (4.12.2)
    Requirement already satisfied: bleach!=5.0.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (6.0.0)
    Requirement already satisfied: defusedxml in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.7.1)
    Requirement already satisfied: jupyterlab-pygments in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.2.2)
    Requirement already satisfied: mistune<4,>=2.0.3 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (3.0.1)
    Requirement already satisfied: nbclient>=0.5.0 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.8.0)
    Requirement already satisfied: pandocfilters>=1.4.1 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.5.0)
    Requirement already satisfied: tinycss2 in /home/user/.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.2.1)
    Requirement already satisfied: fastjsonschema in /home/user/.local/lib/python3.9/site-packages (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab) (2.18.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.19.0->jupyterlab) (3.2.0)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.19.0->jupyterlab) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in /home/user/.local/lib/python3.9/site-packages (from requests>=2.31->jupyterlab-server<3,>=2.19.0->jupyterlab) (2023.7.22)
    Requirement already satisfied: ptyprocess in /home/user/.local/lib/python3.9/site-packages (from terminado>=0.8.3->jupyter-server<3,>=2.4.0->jupyterlab) (0.7.0)
    Requirement already satisfied: argon2-cffi-bindings in /home/user/.local/lib/python3.9/site-packages (from argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (21.2.0)
    Requirement already satisfied: six>=1.9.0 in /home/user/.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.16.0)
    Requirement already satisfied: webencodings in /home/user/.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.5.1)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in /home/user/.local/lib/python3.9/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyterlab) (0.8.3)
    Requirement already satisfied: fqdn in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.5.1)
    Requirement already satisfied: isoduration in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (20.11.0)
    Requirement already satisfied: jsonpointer>1.13 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (2.4)
    Requirement already satisfied: uri-template in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.3.0)
    Requirement already satisfied: webcolors>=1.11 in /home/user/.local/lib/python3.9/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.13)
    Requirement already satisfied: wcwidth in /home/user/.local/lib/python3.9/site-packages (from prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30->ipython>=7.23.1->ipykernel->jupyterlab) (0.2.6)
    Requirement already satisfied: cffi>=1.0.1 in /home/user/.local/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (1.15.1)
    Requirement already satisfied: soupsieve>1.2 in /home/user/.local/lib/python3.9/site-packages (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (2.5)
    Requirement already satisfied: executing>=1.2.0 in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (1.2.0)
    Requirement already satisfied: asttokens>=2.1.0 in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (2.4.0)
    Requirement already satisfied: pure-eval in /home/user/.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (0.2.2)
    Requirement already satisfied: pycparser in /home/user/.local/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (2.21)
    Requirement already satisfied: arrow>=0.15.0 in /home/user/.local/lib/python3.9/site-packages (from isoduration->jsonschema>=4.18.0->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.2.3)





    0



## create README.md


```python
os.system('jupyter nbconvert --to Markdown notebook.ipynb && cp notebook.md README.md')
```

    [NbConvertApp] Converting notebook notebook.ipynb to Markdown
    [NbConvertApp] Writing 35267 bytes to notebook.md





    0



## create install.py


```python
os.system('jupyter nbconvert --to python notebook.ipynb && cp notebook.py install.py')
```

    [NbConvertApp] Converting notebook notebook.ipynb to python
    [NbConvertApp] Writing 3654 bytes to notebook.py





    0



## run jupyterlab

run jupyter-lab with port 8702 using command "jupyterlab"
