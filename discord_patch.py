import sys
# Prevent discord.py from importing voice support which requires audioop
sys.modules['discord.voice_client'] = None
