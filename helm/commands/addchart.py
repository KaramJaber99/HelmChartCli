from subprocess import run,PIPE
import click

@click.command()
@click.option('-cn','--chartname',help="Please provide the Chart name")
@click.option('-cu','--charturl',help="Please provide the Chart url")

def addchart(chartname,charturl):

    ##helm repo add [NAMURL] [flags]
    arguments=["helm", "repo","add", f"{chartname}", f"{charturl}"] 
    run(arguments, capture_output=True) #Updating the repo to the latest version
    p = run(arguments, capture_output=True )
    print( p.stdout.decode() )
    print( p.stderr.decode() )


