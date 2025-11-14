#!/usr/bin/env python3
"""Direct script to open Chrome and navigate to github.com/iiviie without agent reasoning"""

import asyncio
import os
from dotenv import load_dotenv
from droidrun import AdbTools

# Load environment variables
load_dotenv()

async def main():
    # Initialize ADB tools
    tools = AdbTools()

    print("Opening Chrome...")
    await tools.start_app("com.android.chrome")

    await asyncio.sleep(2)  # Wait for Chrome to open

    print("Taking screenshot to see current state...")
    screenshot = await tools.take_screenshot()
    print(f"Screenshot saved")

    print("Typing URL into address bar...")
    # Use adb input text directly
    await tools.press_key("KEYCODE_L", ctrl=True)  # Ctrl+L to focus address bar
    await asyncio.sleep(0.5)

    # Type the URL
    result = await tools.input_text("github.com/iiviie", clear=True)
    print(f"Input result: {result}")

    await asyncio.sleep(0.5)

    print("Pressing Enter...")
    await tools.press_key("KEYCODE_ENTER")

    await asyncio.sleep(2)

    print("Done! Chrome should now be on github.com/iiviie")

if __name__ == "__main__":
    asyncio.run(main())
