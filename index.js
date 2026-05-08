const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

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