# apps/bot/main.py
"""
JJK MMORPG Discord Bot - Main Entry Point
Production MMORPG for Jujutsu Kaisen themed gameplay
"""
import asyncio
import logging
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from apps.bot.launcher import main

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot shutdown by user")
        sys.exit(0)
    except Exception as e:
        logging.critical(f"Critical error: {e}", exc_info=True)
        sys.exit(1)