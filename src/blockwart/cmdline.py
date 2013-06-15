import argparse
from os import getcwd

from . import VERSION_STRING
from . import commands
from .repo import Repository
from .utils import mark_for_translation as _


def bw_nodes(repo, args):
    for node in repo.nodes:
        if args.show_hostnames:
            print(node.hostname)
        else:
            print(node.name)


def bw_run(repo, args):
    print(commands.run(repo, args.target, args.command))


def build_parser_bw():
    parser = argparse.ArgumentParser(prog="bw")
    parser.add_argument(
        "--version",
        action='version',
        version=VERSION_STRING,
    )
    subparsers = parser.add_subparsers(
        title=_("subcommands"),
        help=_("use 'bw <subcommand> --help' for more info"),
    )
    # bw nodes
    parser_nodes = subparsers.add_parser("nodes")
    parser_nodes.set_defaults(func=bw_nodes)
    parser_nodes.add_argument(
        '--hostnames',
        action='store_true',
        dest='show_hostnames',
        help=_("show hostnames instead of node names"),
    )

    # bw run
    parser_run = subparsers.add_parser("run")
    parser_run.set_defaults(func=bw_run)
    parser_run.add_argument(
        'target',
        metavar=_("NODE"),
        type=str,
        help=_("target node"),
    )
    parser_run.add_argument(
        'command',
        metavar=_("COMMAND"),
        type=str,
        help=_("command to run"),
    )
    return parser


def main():
    """
    Entry point for the 'bw' command line utility.
    """
    parser_bw = build_parser_bw()
    args = parser_bw.parse_args()
    repo = Repository(getcwd())
    args.func(repo, args)