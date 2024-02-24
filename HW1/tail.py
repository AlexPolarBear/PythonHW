import sys
import click

@click.command()
# @click.version_option("0.1.0", prog_name="nl")
# @click.argument('file', nargs=-1, type=click.File("r"))
def tail(file):
    """
    Write each FILE to standard output, with line numbers added.
    With no FILE, or when FILE is -, read standard input.
    """
    
    

if __name__ == '__main__':
    tail()