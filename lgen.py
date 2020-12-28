import click

from libgen.libgen import Libgen


@click.command()
@click.argument("search", type=str)
@click.option("-p", "--results-per-page", "results", type=str)
@click.option("-i", "--info", "info", type=int)
def cli(search, results, info):
    if info:
        libgen = Libgen(search, results)
        libgen.list_search_result()
        libgen.info(2)


if __name__ == "__main__":
    cli()
