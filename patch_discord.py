import subprocess
import sys
import os

# Install dependencies into the venv
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
    check=True,
)

# Locate discord/player.py in the active Python path and patch out the
# audioop import so the bot can start on environments that lack audioop
# (Python 3.13+, where audioop was removed from the stdlib).
player_file = None
for path in sys.path:
    candidate = os.path.join(path, "discord", "player.py")
    if os.path.exists(candidate):
        player_file = candidate
        break

if player_file:
    with open(player_file, "r") as f:
        content = f.read()
    patched = content.replace("import audioop", "#import audioop")
    if patched != content:
        with open(player_file, "w") as f:
            f.write(patched)
        print(f"Patched audioop import in {player_file}")
    else:
        print(f"No audioop import found in {player_file} — nothing to patch")
else:
    print("discord/player.py not found in sys.path — skipping patch")
