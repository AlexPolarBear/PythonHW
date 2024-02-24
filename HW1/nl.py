import sys
import click

@click.command()
@click.version_option("0.1.0", prog_name="nl")
@click.argument('file', nargs=-1, type=click.File("r"))
def nl(file):
    """
    Write each FILE to standard output, with line numbers added.
    With no FILE, or when FILE is -, read standard input.
    """
    
    i = 1
    if not file or file[0].name == "<stdin>":
        while True:
            line = sys.stdin.readline()
            click.echo(f"\t{'{:>3s}'.format(str(i))} {line.rstrip()}")
            i += 1
    else:
        for f in file:
            for line in f.readlines():
                click.echo(f"\t{'{:>3s}'.format(str(i))} {line.rstrip()}")
                i += 1

if __name__ == '__main__':
    nl()