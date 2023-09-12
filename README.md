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

    WORKSPACE: /home/user
    PATH: /home/user/local/.bin:/home/user/local/.bin:/home/user/node_modules/.bin:/home/user/.local/bin:/home/user/.local/bin:/home/user/.node_modules_global/bin:/home/user/.local/bin:/extbin/bin:/extbin/npm/docker/bin:/extbin/npm/globals/bin:/extbin/globals/pnpm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin





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
    100 2544k  100 2544k    0     0  72.3M      0 --:--:-- --:--:-- --:--:-- 73.0M


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
    Requirement already satisfied: jupyter in ./.local/lib/python3.9/site-packages (1.0.0)
    Requirement already satisfied: notebook in ./.local/lib/python3.9/site-packages (from jupyter) (7.0.3)
    Requirement already satisfied: qtconsole in ./.local/lib/python3.9/site-packages (from jupyter) (5.4.4)
    Requirement already satisfied: jupyter-console in ./.local/lib/python3.9/site-packages (from jupyter) (6.6.3)
    Requirement already satisfied: nbconvert in ./.local/lib/python3.9/site-packages (from jupyter) (7.8.0)
    Requirement already satisfied: ipykernel in ./.local/lib/python3.9/site-packages (from jupyter) (6.25.2)
    Requirement already satisfied: ipywidgets in ./.local/lib/python3.9/site-packages (from jupyter) (8.1.0)
    Requirement already satisfied: comm>=0.1.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.4)
    Requirement already satisfied: debugpy>=1.6.5 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (1.7.0)
    Requirement already satisfied: ipython>=7.23.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (8.15.0)
    Requirement already satisfied: jupyter-client>=6.1.12 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (8.3.1)
    Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.3.1)
    Requirement already satisfied: matplotlib-inline>=0.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (0.1.6)
    Requirement already satisfied: nest-asyncio in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (1.5.7)
    Requirement already satisfied: packaging in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (23.1)
    Requirement already satisfied: psutil in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.9.5)
    Requirement already satisfied: pyzmq>=20 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (25.1.1)
    Requirement already satisfied: tornado>=6.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (6.3.3)
    Requirement already satisfied: traitlets>=5.4.0 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyter) (5.9.0)
    Requirement already satisfied: widgetsnbextension~=4.0.7 in ./.local/lib/python3.9/site-packages (from ipywidgets->jupyter) (4.0.8)
    Requirement already satisfied: jupyterlab-widgets~=3.0.7 in ./.local/lib/python3.9/site-packages (from ipywidgets->jupyter) (3.0.8)
    Requirement already satisfied: prompt-toolkit>=3.0.30 in ./.local/lib/python3.9/site-packages (from jupyter-console->jupyter) (3.0.39)
    Requirement already satisfied: pygments in ./.local/lib/python3.9/site-packages (from jupyter-console->jupyter) (2.16.1)
    Requirement already satisfied: beautifulsoup4 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (4.12.2)
    Requirement already satisfied: bleach!=5.0.0 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (6.0.0)
    Requirement already satisfied: defusedxml in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.7.1)
    Requirement already satisfied: importlib-metadata>=3.6 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (6.8.0)
    Requirement already satisfied: jinja2>=3.0 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (3.1.2)
    Requirement already satisfied: jupyterlab-pygments in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.2.2)
    Requirement already satisfied: markupsafe>=2.0 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (2.1.3)
    Requirement already satisfied: mistune<4,>=2.0.3 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (3.0.1)
    Requirement already satisfied: nbclient>=0.5.0 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (0.8.0)
    Requirement already satisfied: nbformat>=5.7 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (5.9.2)
    Requirement already satisfied: pandocfilters>=1.4.1 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (1.5.0)
    Requirement already satisfied: tinycss2 in ./.local/lib/python3.9/site-packages (from nbconvert->jupyter) (1.2.1)
    Requirement already satisfied: jupyter-server<3,>=2.4.0 in ./.local/lib/python3.9/site-packages (from notebook->jupyter) (2.7.3)
    Requirement already satisfied: jupyterlab-server<3,>=2.22.1 in ./.local/lib/python3.9/site-packages (from notebook->jupyter) (2.24.0)
    Requirement already satisfied: jupyterlab<5,>=4.0.2 in ./.local/lib/python3.9/site-packages (from notebook->jupyter) (4.0.5)
    Requirement already satisfied: notebook-shim<0.3,>=0.2 in ./.local/lib/python3.9/site-packages (from notebook->jupyter) (0.2.3)
    Requirement already satisfied: ipython-genutils in ./.local/lib/python3.9/site-packages (from qtconsole->jupyter) (0.2.0)
    Requirement already satisfied: qtpy>=2.4.0 in ./.local/lib/python3.9/site-packages (from qtconsole->jupyter) (2.4.0)
    Requirement already satisfied: six>=1.9.0 in ./.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert->jupyter) (1.16.0)
    Requirement already satisfied: webencodings in ./.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert->jupyter) (0.5.1)
    Requirement already satisfied: zipp>=0.5 in ./.local/lib/python3.9/site-packages (from importlib-metadata>=3.6->nbconvert->jupyter) (3.16.2)
    Requirement already satisfied: backcall in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.2.0)
    Requirement already satisfied: decorator in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.19.0)
    Requirement already satisfied: pickleshare in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.7.5)
    Requirement already satisfied: stack-data in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (0.6.2)
    Requirement already satisfied: typing-extensions in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.7.1)
    Requirement already satisfied: exceptiongroup in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (1.1.3)
    Requirement already satisfied: pexpect>4.3 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyter) (4.8.0)
    Requirement already satisfied: python-dateutil>=2.8.2 in ./.local/lib/python3.9/site-packages (from jupyter-client>=6.1.12->ipykernel->jupyter) (2.8.2)
    Requirement already satisfied: platformdirs>=2.5 in ./.local/lib/python3.9/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel->jupyter) (3.10.0)
    Requirement already satisfied: anyio>=3.1.0 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (4.0.0)
    Requirement already satisfied: argon2-cffi in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (23.1.0)
    Requirement already satisfied: jupyter-events>=0.6.0 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.7.0)
    Requirement already satisfied: jupyter-server-terminals in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.4.4)
    Requirement already satisfied: overrides in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (7.4.0)
    Requirement already satisfied: prometheus-client in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.17.1)
    Requirement already satisfied: send2trash>=1.8.2 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (1.8.2)
    Requirement already satisfied: terminado>=0.8.3 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (0.17.1)
    Requirement already satisfied: websocket-client in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->notebook->jupyter) (1.6.3)
    Requirement already satisfied: async-lru>=1.0.0 in ./.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.0.4)
    Requirement already satisfied: jupyter-lsp>=2.0.0 in ./.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.2.0)
    Requirement already satisfied: tomli in ./.local/lib/python3.9/site-packages (from jupyterlab<5,>=4.0.2->notebook->jupyter) (2.0.1)
    Requirement already satisfied: babel>=2.10 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.12.1)
    Requirement already satisfied: json5>=0.9.0 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.9.14)
    Requirement already satisfied: jsonschema>=4.17.3 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (4.19.0)
    Requirement already satisfied: requests>=2.28 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.31.0)
    Requirement already satisfied: fastjsonschema in ./.local/lib/python3.9/site-packages (from nbformat>=5.7->nbconvert->jupyter) (2.18.0)
    Requirement already satisfied: wcwidth in ./.local/lib/python3.9/site-packages (from prompt-toolkit>=3.0.30->jupyter-console->jupyter) (0.2.6)
    Requirement already satisfied: soupsieve>1.2 in ./.local/lib/python3.9/site-packages (from beautifulsoup4->nbconvert->jupyter) (2.5)
    Requirement already satisfied: idna>=2.8 in ./.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (3.4)
    Requirement already satisfied: sniffio>=1.1 in ./.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (1.3.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in ./.local/lib/python3.9/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyter) (0.8.3)
    Requirement already satisfied: attrs>=22.2.0 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (23.1.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2023.7.1)
    Requirement already satisfied: referencing>=0.28.4 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.30.2)
    Requirement already satisfied: rpds-py>=0.7.1 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (0.10.2)
    Requirement already satisfied: python-json-logger>=2.0.4 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (2.0.7)
    Requirement already satisfied: pyyaml>=5.3 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (6.0.1)
    Requirement already satisfied: rfc3339-validator in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (0.1.4)
    Requirement already satisfied: rfc3986-validator>=0.1.1 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->notebook->jupyter) (0.1.1)
    Requirement already satisfied: ptyprocess>=0.5 in ./.local/lib/python3.9/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel->jupyter) (0.7.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (3.2.0)
    Requirement already satisfied: urllib3<3,>=1.21.1 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2023.7.22)
    Requirement already satisfied: argon2-cffi-bindings in ./.local/lib/python3.9/site-packages (from argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (21.2.0)
    Requirement already satisfied: executing>=1.2.0 in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (1.2.0)
    Requirement already satisfied: asttokens>=2.1.0 in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (2.4.0)
    Requirement already satisfied: pure-eval in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyter) (0.2.2)
    Requirement already satisfied: fqdn in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.5.1)
    Requirement already satisfied: isoduration in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (20.11.0)
    Requirement already satisfied: jsonpointer>1.13 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (2.4)
    Requirement already satisfied: uri-template in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.3.0)
    Requirement already satisfied: webcolors>=1.11 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.13)
    Requirement already satisfied: cffi>=1.0.1 in ./.local/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (1.15.1)
    Requirement already satisfied: pycparser in ./.local/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->notebook->jupyter) (2.21)
    Requirement already satisfied: arrow>=0.15.0 in ./.local/lib/python3.9/site-packages (from isoduration->jsonschema>=4.17.3->jupyterlab-server<3,>=2.22.1->notebook->jupyter) (1.2.3)





    0



## generate jupyter config


```python
os.system('echo y | jupyter notebook --generate-config')
fileaddlineifnotinfile(os.path.expanduser('~/.bashrc'),"alias jupyterlab='jupyter-lab --ip=127.0.0.1 --port 8702'\n")
os.system('alias jupyterlab="jupyter-lab --ip=127.0.0.1 --port 8702"')
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

    hostname: workspaces-ws-gv86h-deployment-6d4ffc56b9-vlt9k
    origin: https://port8702-workspaces-ws-gv86h.eu10.applicationstudio.cloud.sap


## install jupyterlab


```python
os.system('pip install jupyterlab')
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: jupyterlab in ./.local/lib/python3.9/site-packages (4.0.5)
    Requirement already satisfied: async-lru>=1.0.0 in ./.local/lib/python3.9/site-packages (from jupyterlab) (2.0.4)
    Requirement already satisfied: importlib-metadata>=4.8.3 in ./.local/lib/python3.9/site-packages (from jupyterlab) (6.8.0)
    Requirement already satisfied: ipykernel in ./.local/lib/python3.9/site-packages (from jupyterlab) (6.25.2)
    Requirement already satisfied: jinja2>=3.0.3 in ./.local/lib/python3.9/site-packages (from jupyterlab) (3.1.2)
    Requirement already satisfied: jupyter-core in ./.local/lib/python3.9/site-packages (from jupyterlab) (5.3.1)
    Requirement already satisfied: jupyter-lsp>=2.0.0 in ./.local/lib/python3.9/site-packages (from jupyterlab) (2.2.0)
    Requirement already satisfied: jupyter-server<3,>=2.4.0 in ./.local/lib/python3.9/site-packages (from jupyterlab) (2.7.3)
    Requirement already satisfied: jupyterlab-server<3,>=2.19.0 in ./.local/lib/python3.9/site-packages (from jupyterlab) (2.24.0)
    Requirement already satisfied: notebook-shim>=0.2 in ./.local/lib/python3.9/site-packages (from jupyterlab) (0.2.3)
    Requirement already satisfied: packaging in ./.local/lib/python3.9/site-packages (from jupyterlab) (23.1)
    Requirement already satisfied: tomli in ./.local/lib/python3.9/site-packages (from jupyterlab) (2.0.1)
    Requirement already satisfied: tornado>=6.2.0 in ./.local/lib/python3.9/site-packages (from jupyterlab) (6.3.3)
    Requirement already satisfied: traitlets in ./.local/lib/python3.9/site-packages (from jupyterlab) (5.9.0)
    Requirement already satisfied: typing-extensions>=4.0.0 in ./.local/lib/python3.9/site-packages (from async-lru>=1.0.0->jupyterlab) (4.7.1)
    Requirement already satisfied: zipp>=0.5 in ./.local/lib/python3.9/site-packages (from importlib-metadata>=4.8.3->jupyterlab) (3.16.2)
    Requirement already satisfied: MarkupSafe>=2.0 in ./.local/lib/python3.9/site-packages (from jinja2>=3.0.3->jupyterlab) (2.1.3)
    Requirement already satisfied: anyio>=3.1.0 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (4.0.0)
    Requirement already satisfied: argon2-cffi in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (23.1.0)
    Requirement already satisfied: jupyter-client>=7.4.4 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (8.3.1)
    Requirement already satisfied: jupyter-events>=0.6.0 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.7.0)
    Requirement already satisfied: jupyter-server-terminals in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.4.4)
    Requirement already satisfied: nbconvert>=6.4.4 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (7.8.0)
    Requirement already satisfied: nbformat>=5.3.0 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (5.9.2)
    Requirement already satisfied: overrides in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (7.4.0)
    Requirement already satisfied: prometheus-client in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.17.1)
    Requirement already satisfied: pyzmq>=24 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (25.1.1)
    Requirement already satisfied: send2trash>=1.8.2 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (1.8.2)
    Requirement already satisfied: terminado>=0.8.3 in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (0.17.1)
    Requirement already satisfied: websocket-client in ./.local/lib/python3.9/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab) (1.6.3)
    Requirement already satisfied: platformdirs>=2.5 in ./.local/lib/python3.9/site-packages (from jupyter-core->jupyterlab) (3.10.0)
    Requirement already satisfied: babel>=2.10 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (2.12.1)
    Requirement already satisfied: json5>=0.9.0 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (0.9.14)
    Requirement already satisfied: jsonschema>=4.17.3 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (4.19.0)
    Requirement already satisfied: requests>=2.28 in ./.local/lib/python3.9/site-packages (from jupyterlab-server<3,>=2.19.0->jupyterlab) (2.31.0)
    Requirement already satisfied: comm>=0.1.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (0.1.4)
    Requirement already satisfied: debugpy>=1.6.5 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (1.7.0)
    Requirement already satisfied: ipython>=7.23.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (8.15.0)
    Requirement already satisfied: matplotlib-inline>=0.1 in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (0.1.6)
    Requirement already satisfied: nest-asyncio in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (1.5.7)
    Requirement already satisfied: psutil in ./.local/lib/python3.9/site-packages (from ipykernel->jupyterlab) (5.9.5)
    Requirement already satisfied: idna>=2.8 in ./.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (3.4)
    Requirement already satisfied: sniffio>=1.1 in ./.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (1.3.0)
    Requirement already satisfied: exceptiongroup>=1.0.2 in ./.local/lib/python3.9/site-packages (from anyio>=3.1.0->jupyter-server<3,>=2.4.0->jupyterlab) (1.1.3)
    Requirement already satisfied: backcall in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.2.0)
    Requirement already satisfied: decorator in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.19.0)
    Requirement already satisfied: pickleshare in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.7.5)
    Requirement already satisfied: prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (3.0.39)
    Requirement already satisfied: pygments>=2.4.0 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (2.16.1)
    Requirement already satisfied: stack-data in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (0.6.2)
    Requirement already satisfied: pexpect>4.3 in ./.local/lib/python3.9/site-packages (from ipython>=7.23.1->ipykernel->jupyterlab) (4.8.0)
    Requirement already satisfied: attrs>=22.2.0 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (23.1.0)
    Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (2023.7.1)
    Requirement already satisfied: referencing>=0.28.4 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (0.30.2)
    Requirement already satisfied: rpds-py>=0.7.1 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (0.10.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in ./.local/lib/python3.9/site-packages (from jupyter-client>=7.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (2.8.2)
    Requirement already satisfied: python-json-logger>=2.0.4 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (2.0.7)
    Requirement already satisfied: pyyaml>=5.3 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (6.0.1)
    Requirement already satisfied: rfc3339-validator in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (0.1.4)
    Requirement already satisfied: rfc3986-validator>=0.1.1 in ./.local/lib/python3.9/site-packages (from jupyter-events>=0.6.0->jupyter-server<3,>=2.4.0->jupyterlab) (0.1.1)
    Requirement already satisfied: beautifulsoup4 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (4.12.2)
    Requirement already satisfied: bleach!=5.0.0 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (6.0.0)
    Requirement already satisfied: defusedxml in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.7.1)
    Requirement already satisfied: jupyterlab-pygments in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.2.2)
    Requirement already satisfied: mistune<4,>=2.0.3 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (3.0.1)
    Requirement already satisfied: nbclient>=0.5.0 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.8.0)
    Requirement already satisfied: pandocfilters>=1.4.1 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.5.0)
    Requirement already satisfied: tinycss2 in ./.local/lib/python3.9/site-packages (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.2.1)
    Requirement already satisfied: fastjsonschema in ./.local/lib/python3.9/site-packages (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab) (2.18.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.19.0->jupyterlab) (3.2.0)
    Requirement already satisfied: urllib3<3,>=1.21.1 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.19.0->jupyterlab) (2.0.4)
    Requirement already satisfied: certifi>=2017.4.17 in ./.local/lib/python3.9/site-packages (from requests>=2.28->jupyterlab-server<3,>=2.19.0->jupyterlab) (2023.7.22)
    Requirement already satisfied: ptyprocess in ./.local/lib/python3.9/site-packages (from terminado>=0.8.3->jupyter-server<3,>=2.4.0->jupyterlab) (0.7.0)
    Requirement already satisfied: argon2-cffi-bindings in ./.local/lib/python3.9/site-packages (from argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (21.2.0)
    Requirement already satisfied: six>=1.9.0 in ./.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (1.16.0)
    Requirement already satisfied: webencodings in ./.local/lib/python3.9/site-packages (from bleach!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (0.5.1)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in ./.local/lib/python3.9/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyterlab) (0.8.3)
    Requirement already satisfied: fqdn in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.5.1)
    Requirement already satisfied: isoduration in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (20.11.0)
    Requirement already satisfied: jsonpointer>1.13 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (2.4)
    Requirement already satisfied: uri-template in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.3.0)
    Requirement already satisfied: webcolors>=1.11 in ./.local/lib/python3.9/site-packages (from jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.13)
    Requirement already satisfied: wcwidth in ./.local/lib/python3.9/site-packages (from prompt-toolkit!=3.0.37,<3.1.0,>=3.0.30->ipython>=7.23.1->ipykernel->jupyterlab) (0.2.6)
    Requirement already satisfied: cffi>=1.0.1 in ./.local/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (1.15.1)
    Requirement already satisfied: soupsieve>1.2 in ./.local/lib/python3.9/site-packages (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab) (2.5)
    Requirement already satisfied: executing>=1.2.0 in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (1.2.0)
    Requirement already satisfied: asttokens>=2.1.0 in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (2.4.0)
    Requirement already satisfied: pure-eval in ./.local/lib/python3.9/site-packages (from stack-data->ipython>=7.23.1->ipykernel->jupyterlab) (0.2.2)
    Requirement already satisfied: pycparser in ./.local/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server<3,>=2.4.0->jupyterlab) (2.21)
    Requirement already satisfied: arrow>=0.15.0 in ./.local/lib/python3.9/site-packages (from isoduration->jsonschema>=4.17.3->jupyterlab-server<3,>=2.19.0->jupyterlab) (1.2.3)





    0



## create README.md


```python
os.system('jupyter nbconvert --to Markdown notebook.ipynb && cp notebook.md README.md')
```

    This application is used to convert notebook files (*.ipynb)
            to various other formats.
    
            WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.
    
    Options
    =======
    The options below are convenience aliases to configurable class-options,
    as listed in the "Equivalent to" description-line of the aliases.
    To see all configurable class-options for some <cmd>, use:
        <cmd> --help-all
    
    --debug
        set log level to logging.DEBUG (maximize logging output)
        Equivalent to: [--Application.log_level=10]
    --show-config
        Show the application's configuration (human-readable format)
        Equivalent to: [--Application.show_config=True]
    --show-config-json
        Show the application's configuration (json format)
        Equivalent to: [--Application.show_config_json=True]
    --generate-config
        generate default config file
        Equivalent to: [--JupyterApp.generate_config=True]
    -y
        Answer yes to any questions instead of prompting.
        Equivalent to: [--JupyterApp.answer_yes=True]
    --execute
        Execute the notebook prior to export.
        Equivalent to: [--ExecutePreprocessor.enabled=True]
    --allow-errors
        Continue notebook execution even if one of the cells throws an error and include the error message in the cell output (the default behaviour is to abort conversion). This flag is only relevant if '--execute' was specified, too.
        Equivalent to: [--ExecutePreprocessor.allow_errors=True]
    --stdin
        read a single notebook file from stdin. Write the resulting notebook with default basename 'notebook.*'
        Equivalent to: [--NbConvertApp.from_stdin=True]
    --stdout
        Write notebook output to stdout instead of files.
        Equivalent to: [--NbConvertApp.writer_class=StdoutWriter]
    --inplace
        Run nbconvert in place, overwriting the existing notebook (only
                relevant when converting to notebook format)
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory=]
    --clear-output
        Clear output of current file and save in place,
                overwriting the existing notebook.
        Equivalent to: [--NbConvertApp.use_output_suffix=False --NbConvertApp.export_format=notebook --FilesWriter.build_directory= --ClearOutputPreprocessor.enabled=True]
    --no-prompt
        Exclude input and output prompts from converted document.
        Equivalent to: [--TemplateExporter.exclude_input_prompt=True --TemplateExporter.exclude_output_prompt=True]
    --no-input
        Exclude input cells and output prompts from converted document.
                This mode is ideal for generating code-free reports.
        Equivalent to: [--TemplateExporter.exclude_output_prompt=True --TemplateExporter.exclude_input=True --TemplateExporter.exclude_input_prompt=True]
    --allow-chromium-download
        Whether to allow downloading chromium if no suitable version is found on the system.
        Equivalent to: [--WebPDFExporter.allow_chromium_download=True]
    --disable-chromium-sandbox
        Disable chromium security sandbox when converting to PDF..
        Equivalent to: [--WebPDFExporter.disable_sandbox=True]
    --show-input
        Shows code input. This flag is only useful for dejavu users.
        Equivalent to: [--TemplateExporter.exclude_input=False]
    --embed-images
        Embed the images as base64 dataurls in the output. This flag is only useful for the HTML/WebPDF/Slides exports.
        Equivalent to: [--HTMLExporter.embed_images=True]
    --sanitize-html
        Whether the HTML in Markdown cells and cell outputs should be sanitized..
        Equivalent to: [--HTMLExporter.sanitize_html=True]
    --log-level=<Enum>
        Set the log level by value or name.
        Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        Default: 30
        Equivalent to: [--Application.log_level]
    --config=<Unicode>
        Full path of a config file.
        Default: ''
        Equivalent to: [--JupyterApp.config_file]
    --to=<Unicode>
        The export format to be used, either one of the built-in formats
                ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf']
                or a dotted object name that represents the import path for an
                ``Exporter`` class
        Default: ''
        Equivalent to: [--NbConvertApp.export_format]
    --template=<Unicode>
        Name of the template to use
        Default: ''
        Equivalent to: [--TemplateExporter.template_name]
    --template-file=<Unicode>
        Name of the template file to use
        Default: None
        Equivalent to: [--TemplateExporter.template_file]
    --theme=<Unicode>
        Template specific theme(e.g. the name of a JupyterLab CSS theme distributed
        as prebuilt extension for the lab template)
        Default: 'light'
        Equivalent to: [--HTMLExporter.theme]
    --sanitize_html=<Bool>
        Whether the HTML in Markdown cells and cell outputs should be sanitized.This
        should be set to True by nbviewer or similar tools.
        Default: False
        Equivalent to: [--HTMLExporter.sanitize_html]
    --writer=<DottedObjectName>
        Writer class used to write the
                                            results of the conversion
        Default: 'FilesWriter'
        Equivalent to: [--NbConvertApp.writer_class]
    --post=<DottedOrNone>
        PostProcessor class used to write the
                                            results of the conversion
        Default: ''
        Equivalent to: [--NbConvertApp.postprocessor_class]
    --output=<Unicode>
        Overwrite base name use for output files.
                    Supports pattern replacements '{notebook_name}'.
        Default: '{notebook_name}'
        Equivalent to: [--NbConvertApp.output_base]
    --output-dir=<Unicode>
        Directory to write output(s) to. Defaults
                                      to output to the directory of each notebook. To recover
                                      previous default behaviour (outputting to the current
                                      working directory) use . as the flag value.
        Default: ''
        Equivalent to: [--FilesWriter.build_directory]
    --reveal-prefix=<Unicode>
        The URL prefix for reveal.js (version 3.x).
                This defaults to the reveal CDN, but can be any url pointing to a copy
                of reveal.js.
                For speaker notes to work, this must be a relative path to a local
                copy of reveal.js: e.g., "reveal.js".
                If a relative path is given, it must be a subdirectory of the
                current directory (from which the server is run).
                See the usage documentation
                (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow)
                for more details.
        Default: ''
        Equivalent to: [--SlidesExporter.reveal_url_prefix]
    --nbformat=<Enum>
        The nbformat version to write.
                Use this to downgrade notebooks.
        Choices: any of [1, 2, 3, 4]
        Default: 4
        Equivalent to: [--NotebookExporter.nbformat_version]
    
    Examples
    --------
    
        The simplest way to use nbconvert is
    
                > jupyter nbconvert mynotebook.ipynb --to html
    
                Options include ['asciidoc', 'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'qtpdf', 'qtpng', 'rst', 'script', 'slides', 'webpdf'].
    
                > jupyter nbconvert --to latex mynotebook.ipynb
    
                Both HTML and LaTeX support multiple output templates. LaTeX includes
                'base', 'article' and 'report'.  HTML includes 'basic', 'lab' and
                'classic'. You can specify the flavor of the format used.
    
                > jupyter nbconvert --to html --template lab mynotebook.ipynb
    
                You can also pipe the output to stdout, rather than a file
    
                > jupyter nbconvert mynotebook.ipynb --stdout
    
                PDF is generated via latex
    
                > jupyter nbconvert mynotebook.ipynb --to pdf
    
                You can get (and serve) a Reveal.js-powered slideshow
    
                > jupyter nbconvert myslides.ipynb --to slides --post serve
    
                Multiple notebooks can be given at the command line in a couple of
                different ways:
    
                > jupyter nbconvert notebook*.ipynb
                > jupyter nbconvert notebook1.ipynb notebook2.ipynb
    
                or you can specify the notebooks list in a config file, containing::
    
                    c.NbConvertApp.notebooks = ["my_notebook.ipynb"]
    
                > jupyter nbconvert --config mycfg.py
    
    To see all available configurables, use `--help-all`.
    


    [NbConvertApp] WARNING | pattern 'notebook.ipynb' matched no files





    65280



## create install.py


```python
os.system('jupyter nbconvert --to python notebook.ipynb && cp notebook.py install.py')
```

## run jupyterlab

run jupyter-lab with port 8702 using command "jupyterlab"
