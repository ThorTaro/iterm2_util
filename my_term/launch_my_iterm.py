#!/usr/bin/env python3
import asyncio
import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)
    
    # main memo pane
    left_pane = app.current_terminal_window.current_tab.current_session

    # sub memo pane
    right_top_pane = await left_pane.async_split_pane(vertical=True, before=False)

    # myping command pane(right-bottom, and left window)
    right_bottom_pane = await right_top_pane.async_split_pane(vertical=False, before=False) 
    await right_bottom_pane.async_send_text("myping\n")

    # myclock command pane(right-bottom, and right upper window)
    myclock_pane = await right_bottom_pane.async_split_pane(vertical=True, before=False)
    await myclock_pane.async_send_text("myclock\n")

    # getssid command pane(right-bottom, and right bottom window)
    getssid_pane = await myclock_pane.async_split_pane(vertical=False, before=False)
    await getssid_pane.async_send_text("getssid\n")

    # switch cursor to main memo pane
    await left_pane.async_activate()
    # move cursor upto the top on main pane
    await left_pane.async_send_text("clear\n")

iterm2.run_until_complete(main)
