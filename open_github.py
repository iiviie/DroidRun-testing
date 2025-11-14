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
        goal="Open Chrome browser and navigate to github.com/iiviie",
        llms=llm,
        tools=tools
    )

    # Run the agent
    print("Starting agent to open Chrome and navigate to GitHub...")
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
