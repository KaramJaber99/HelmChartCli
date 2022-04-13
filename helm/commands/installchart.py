import click
from subprocess import run,Popen


@click.command()
@click.option('-cn','--chartname',help="Please provide the Chart name")
@click.option('-cu','--charturl',help="Please provide the Chart url")
@click.option('-f','--flags',default="",help="Please provide what flag you want to add,you can see all the flags avilable at the helm site ")

def installchart(chartname,charturl,flags):

    arguments=["helm", "install", f"{chartname}", f"{charturl}"]

    if flags != "":
        arguments.append(flags)
    

    p = run(arguments, capture_output=True )

    print(p.stdout.decode()) #Printing the stdout of the commands


    #Catching the erros and printing a soloution for some 
    print(p.stderr.decode())

    if "re-use" in p.stderr.decode():
        print("The name you are using is already in helm chart, i will run 'helm ls' to check that \n")
        Popen(["helm","ls"])
    elif "download" in p.stderr.decode():
        print("Check if the input is correct and you are downloading the right chart and that its exists \n")
        print(f"you wanted to download {chartname} ??? \n")
        print(f"and this is the correct chart url ?  {charturl} \n")
