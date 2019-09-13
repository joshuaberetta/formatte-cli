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

    # from .formatte import add_subcommand_formatte
    add_subcommand_formatte(subparsers)

    # Parse all command line arguments
    args = parser.parse_args(args)

    # This is not a good way to handle the cases
    # where help should be printed.
    # TODO: there must be a better way?
    if hasattr(args, 'func'):
        # Call the desired subcommand function
        logging.basicConfig(level=args.loglevel.upper())
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 0

    # log.debug('some debug')
    # log.info('some info')
    # log.warning('some warning')

