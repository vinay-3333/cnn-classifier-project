# sh :- shall script this is linux command for enviroment creation
echo [$(date)]:'START'
echo [$(date)]:"creating env with python 3.8 version".
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"activating the enviroment"
source activate ./env
echo [$(date)]:"installing the dev requiremetns"
pip install -r requirements_dev.txt
echo [$(date)]:"END"