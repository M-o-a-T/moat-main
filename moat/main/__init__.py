# command line interface

import sys
from functools import partial

import anyio
import asyncclick as click
from moat.util import attrdict, main_, wrap_main


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


@main_.command(
    short_help="Import the debugger", help="Imports PDB and then continues to process arguments."
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
async def pdb(args):  # safe
    breakpoint()  # safe
    if not args:
        return
    return await main_.main(args)
