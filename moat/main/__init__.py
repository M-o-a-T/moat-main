"""
This module contains the entry point to the MOAT command line interface
"""

import asyncclick as click
from moat.util import attrdict, main_


def cmd(backend="trio"):
    """
    The main command entry point, as declared in ``setup.py``.
    """

    # @click.* decorators change the semantics
    # pylint: disable=no-value-for-parameter
    main_.help = """\
This is the main command handler for MoaT, the Master of all Things.
"""

    obj = attrdict(moat=attrdict(ext="moat", name="moat", sub=False))
    main_(obj=obj, _anyio_backend=backend)


@main_.command(short_help="Import the debugger")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
async def pdb(args):  # safe
    """
    This command imports PDB and continues to process arguments.
    """
    breakpoint()  # pylint: disable=forgotten-debug-statement
    if not args:
        return
    return await main_.main(args)
