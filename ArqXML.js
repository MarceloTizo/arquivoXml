const fs = require('fs');
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const contactsFile = 'contacts.bin';

function addContact() {
  rl.question('Digite o nome do contato: ', (name) => {
    rl.question('Digite o número de telefone do contato: ', (phone) => {
      rl.question('Digite o e-mail do contato: ', (email) => {
        const contact = { name, phone, email };
        saveContact(contact);
        rl.close();
      });
    });
  });
}

function saveContact(contact) {
  let contacts = [];

  try {
    const data = fs.readFileSync(contactsFile);
    contacts = JSON.parse(data);
  } catch (error) {
    
  }

  contacts.push(contact);

  fs.writeFileSync(contactsFile, JSON.stringify(contacts));

  console.log('Contato adicionado com sucesso!');
}

function main() {
  console.log('1 - Adicionar contato');
  console.log('2 - Sair');

  rl.question('Escolha uma opção: ', (option) => {
    if (option === '1') {
      addContact();
    } else if (option === '2') {
      rl.close();
    } else {
      console.log('Opção inválida. Tente novamente.');
      main();
    }
  });
}

main();
