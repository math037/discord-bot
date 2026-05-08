const { Client, GatewayIntentBits } = require('discord.js');
// GatewayIntentBits.MessageContent requires "Message Content Intent" to be explicitly
// enabled in the Discord Developer Portal (Bot → Privileged Gateway Intents).
// Add it back to the array below once that toggle is saved in the portal.
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages] });

client.on('ready', async () => {
  console.log(`Bot connecté en tant que ${client.user.tag}`);
  const channel = client.channels.cache.get('1502015834674036856');
  if (channel) {
    await channel.send('Starting Container');
  }
});

client.on('messageCreate', (message) => {
  if (message.content === 'ping') message.reply('pong');
});

client.login(process.env.DISCORD_TOKEN);