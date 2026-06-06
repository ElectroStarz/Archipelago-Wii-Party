import asyncio
import multiprocessing

import Utils
from CommonClient import get_base_parser, gui_enabled, handle_url_arg, server_loop

from .WPContext import WPContext, logger


def launch_wii_party_client(*args):
    Utils.init_logging("Wii Party Client")

    async def main(main_args):
        multiprocessing.freeze_support()

        main_parser = get_base_parser()
        parser_args = main_parser.parse_args()

        ctx = WPContext(parser_args.connect, parser_args.password)
        ctx.auth = main_args.name

        logger.info("Connecting to server...")
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        logger.info("Running game...")
        ctx.dolphin_sync_task = asyncio.create_task(ctx.dolphin_sync_task(), name="Dolphin Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None

        if ctx.dolphin_sync_task:
            await asyncio.sleep(3)
            await ctx.dolphin_sync_task

    import colorama

    parser = get_base_parser(description="Wii Party Archipelago Client.")
    parser.add_argument("--name", default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()
    asyncio.run(main(launch_args))
    colorama.deinit()


if __name__ == "__main__":
    launch_wii_party_client()
