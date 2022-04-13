Helm cli for adding and installing helm charts and deploying the JFrog Artifactory.
## How to Install
1. curl -fl https://github.com/KaramJaber99/HelmChartCli/blob/main/helmcli.sh | bash 
3. execute ‘helmcli’ commands `helmcli` See [Examples](#Examples) section for commands to run.
## Documentation for required libraries
- https://click.palletsprojects.com/en/8.0.x/
- https://docs.python-requests.org/en/latest/
- https://cryptography.io/en/latest/
## Examples for ‘Helmcli’ commands
The helmcli cli installing helm charts and deploying JFrog Artifactory chart: <br />

-For adding any chart repo to install it after <br />
 ``` sh
$ helmcli addchart 
````
 -For installing any chart you want <br />
 ``` sh
$ helmcli install chart 
````
For installing and deploying JFrog Artifactory: <br />
``` sh
$ helmcli artifactory 
````


```commandline
Usage: helmcli [OPTIONS] COMMAND [ARGS]...

  You can use this cli to add and install any helm chart you need

  and you can install the chart of the best Company JFROG :) by Typing helmcli
  artifactory

Options:
  --help  Show this message and exit.

Commands:
  addchart
  artifactory
  installchart
  ```
