import logging
import argparse
from .formatte import add_subcommand_formatte

log = logging.getLogger(__name__)


def main(args=None):

    parser = argparse.ArgumentParser(prog='formatte', description='Command line interface for the formatte package')
    parser.add_argument(
        '--loglevel', default='info', help='Log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
    )
    subparsers = parser.add_subparsers(help='Sub-commands')
    add_subcommand_formatte(subparsers)

    # Parse all command line arguments
    args = parser.parse_args(args)

    if hasattr(args, 'func'):
        # Call the desired subcommand function
        logging.basicConfig(level=args.loglevel.upper())
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0

