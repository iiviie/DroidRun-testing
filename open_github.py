#!/usr/bin/env python3
"""Script to open Chrome and navigate to github.com/iiviie"""

import asyncio
import os
from dotenv import load_dotenv
from droidrun import AdbTools, DroidAgent
from llama_index.llms.google_genai import GoogleGenAI

# Load environment variables
load_dotenv()

async def main():
    # Initialize ADB tools
    tools = AdbTools()

    # Configure Gemini LLM
    llm = GoogleGenAI(
        api_key=os.getenv("GOOGLE_API_KEY"),
        model="models/gemini-2.5-pro-preview-03-25"
    )

    # Create agent
    agent = DroidAgent(
        goal="""Create a Google account with these exact steps:
1. Open Settings app
2. Scroll all the way to the bottom
3. Click on 'Users & accounts'
4. Click on 'Add account'
5. Click on 'Google'
6. Click on 'Create account'
7. Click 'For my personal use'
8. Enter first name: test, last name: user
9. Click Next
10. Set birthday: Month = January, Day = 1, Year = 2000
11. Select Gender: Male
12. Click Next
13. For Gmail address, enter: testuseriiviie
14. Click Next
15. Enter password: testuseriiviie123
16. Click Next and complete the account creation""",
        llms=llm,
        tools=tools,
        timeout=600  # 10 minutes for account creation
    )

    # Run the agent
    print("Starting agent to create Google account...")
    result = await agent.run()

    # Handle result
    if hasattr(result, 'get'):
        print(f"Success: {result.get('success', False)}")
        if result.get('output'):
            print(f"Output: {result['output']}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
