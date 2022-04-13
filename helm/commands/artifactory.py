import click
from subprocess import run,PIPE

@click.command()
@click.option('-f','--flags',default="")
#@click.option("-i", "--input", "input_file", type=click.File(), help="Input file") //The Next Feature is to add an option to add file in the flags
def artifactory(flags):

    arguments=["helm" ,"repo", "add", "jfrog","https://charts.jfrog.io"]
    p=run(arguments, capture_output=True )
    error_handling(p)

    arguments=["helm","repo","update"]
    p=run(arguments, capture_output=True )#Updating the repo to the latest version
    error_handling(p)

    arguments=["helm","install","artifactory" ,"jfrog/artifactory"]
    if flags != "":
        arguments.append(flags)
    

    p=run(arguments, capture_output=True )
    error_handling(p)


    

def error_handling(p):
    if p.returncode < 0 :
        print(p.stderr.decode())
    else:
        print(p.stdout.decode())
