#!/usr/bin/env python3
import argparse
import asyncio
import iterm2

async def update_preset(connection, session, preset_name):
    preset = await iterm2.ColorPreset.async_get(connection, preset_name)
    profile = await session.async_get_profile()
    await profile.async_set_color_preset(preset)

async def main(connection):
    app = await iterm2.async_get_app(connection)
    session = app.current_terminal_window.current_tab.current_session
    await update_preset(connection, session, preset_name)


def get_preset_name_from_arg():
    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("env",
                        nargs="?",
                        default="local",
                        help="environment(local, dev, stg, prd). default=local")
    args = parser.parse_args()

    # switch preset_name
    preset_name = "Twilight"
    if args.env == "dev":
        preset_name = "Violet Light"

    elif args.env == "stg":
        preset_name = "Solarized Dark Higher Contrast"

    elif args.env == "prd":
        preset_name = "Ubuntu"

    return preset_name


if __name__ == '__main__':
    preset_name = get_preset_name_from_arg()
    iterm2.run_until_complete(main)
