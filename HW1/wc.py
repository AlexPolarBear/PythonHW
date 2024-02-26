import sys
import click

@click.command()
@click.version_option("0.1.0", prog_name="wc")
@click.argument('file', nargs=-1, type=click.File("r"))
def wc(file):
    """
    Print newline, word, and byte counts for each FILE, and a total line if
    more than one FILE is specified. A word is a non-zero-length sequence of
    characters delimited by white space.

    With no FILE, or when FILE is -, read standard input.
    """
    
    if not file or file[0].name == "<stdin>":
        lines = sys.stdin.readline()
    else:
        total_lines = 0
        total_words = 0
        total_bytes = 0
        
        for f in file:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_bytes = sum(len(line.encode()) for line in lines)
            
            total_lines += num_lines
            total_words += num_words
            total_bytes += num_bytes
            click.echo(f"{num_lines} {num_words} {num_bytes} {f.name}")
        
        if len(file) > 1:
            click.echo(f"{total_lines} {total_words} {total_bytes} total")


if __name__ == '__main__':
    wc()