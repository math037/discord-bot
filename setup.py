from setuptools import setup
import subprocess
import sys
import os

def patch_discord():
    """Patch discord.py to comment out audioop import after installation."""
    try:
        import discord
        player_file = os.path.join(os.path.dirname(discord.__file__), 'player.py')
        if os.path.exists(player_file):
            with open(player_file, 'r') as f:
                content = f.read()
            if 'import audioop' in content:
                patched = content.replace('import audioop', '#import audioop')
                with open(player_file, 'w') as f:
                    f.write(patched)
                print(f"✓ Patched audioop import in {player_file}")
    except Exception as e:
        print(f"Warning: Could not patch discord.py: {e}")

# Run patch after pip install
class PostInstallCommand:
    def run(self):
        patch_discord()

setup(
    name='discord-bot',
    version='1.0',
    py_modules=['bot'],
    install_requires=[
        'discord.py',
        'python-dotenv',
    ],
)
