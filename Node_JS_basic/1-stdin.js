const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false,
});

process.stdout.write('Welcome to Holberton School, what is your name?\n');

rl.on('line', (name) => {
  process.stdout.write(`Your name is: ${name}\n`);
  if (process.stdin.isTTY) {
    rl.close();
  }
});

rl.on('close', () => {
  if (!process.stdin.isTTY) {
    process.stdout.write('This important software is now closing\n');
  }
});
