import sys
import click

@click.command()
@click.version_option("0.1.0", prog_name="tail")
@click.argument('file', nargs=-1, type=click.File("r"))
def tail(file):
    """
    Print the last 10 lines of each FILE to standard output.
    With more than one FILE, precede each with a header giving the file name.

    With no FILE, or when FILE is -, read standard input.
    """

    if not file or file[0].name == "<stdin>":
        while True:
            line = sys.stdin.readline()
    else:
        for f in file:
            if file.index(f) > 0:
                click.echo("\n".rstrip())
            click.echo(f"==> {f.name} <==")
            for line in f.readlines()[-10:]:
                click.echo(line.rstrip())


if __name__ == '__main__':
    tail()