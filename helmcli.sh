#!/usr/bin/env bash
git clone https://github.com/KaramJaber99/HelmChartCli.git
cd HelmChartCli

for commandname in python3 virtualenv pip3 
do
if ! command -v $commandname &> /dev/null
then
    echo "$commandname could not be found"
    echo "Install the $commandname that is misssing"
    exit 1 
fi
done 


if [ -d "/venv-helmcli" ]; then
  # Virtualenv Exists
  source venv-helmcli/bin/activate
  pip install -r requirements.txt
  python3 setup.py develop

else
  # Virtualenv created
  virtualenv --python=python3. venv-helmcli
  sleep 1
  source venv-helmcli/bin/activate
  pip install -r requirements.txt
  python3 setup.py develop
fi


helmcli

cat <<INSTRUCTIONS


Please run the following command  $ source jpd/venv-helmcli/bin/activate


INSTRUCTIONS
