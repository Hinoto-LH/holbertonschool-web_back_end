# Node.js Basics

## Description

Ce projet introduit les fondamentaux de Node.js, de la création de serveurs HTTP avec le module natif jusqu'à l'utilisation d'Express.js pour des routes avancées. Vous apprendrez également à moderniser votre workflow avec Babel et Nodemon.

## Ressources

- [Node.js Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide)
- [Process API](https://node.js.org/dist/latest/docs/api/process.html)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express.js Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://github.com/remy/nodemon)

## Objectifs pédagogiques

---

### Exécuter JavaScript avec Node.js

Node.js permet d'exécuter du JavaScript côté serveur, en dehors du navigateur. On lance un fichier avec la commande :

```bash
node mon_fichier.js
```

---

### Les modules Node.js

Node.js utilise un système de modules pour organiser le code. On exporte avec `module.exports` et on importe avec `require()` :

```js
// math.js
module.exports = { add: (a, b) => a + b };

// main.js
const math = require('./math');
console.log(math.add(2, 3)); // 5
```

---

### Lire des fichiers avec Node.js

Le module natif `fs` (file system) permet de lire des fichiers. On peut le faire de façon **synchrone** ou **asynchrone** :

```js
const fs = require('fs');

// Synchrone (bloque l'exécution)
const contenu = fs.readFileSync('fichier.txt', 'utf8');
console.log(contenu);

// Asynchrone (non bloquant)
fs.readFile('fichier.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

---

### Accéder aux arguments et à l'environnement avec `process`

L'objet `process` donne accès aux arguments de la ligne de commande et aux variables d'environnement :

```js
// Arguments : node script.js arg1 arg2
console.log(process.argv);       // ['node', 'script.js', 'arg1', 'arg2']
console.log(process.argv[2]);    // 'arg1'

// Variables d'environnement
console.log(process.env.PORT);   // valeur de la variable PORT
```

---

### Créer un serveur HTTP avec Node.js natif

Le module `http` permet de créer un serveur sans dépendance externe :

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Bonjour le monde !');
});

server.listen(1245, () => {
  console.log('Serveur démarré sur le port 1245');
});
```

---

### Créer un serveur HTTP avec Express.js

Express.js simplifie la création de serveurs et la gestion des routes :

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bonjour le monde !');
});

app.listen(1245, () => {
  console.log('Serveur Express démarré sur le port 1245');
});
```

---

### Routes avancées avec Express.js

Express permet de définir des routes dynamiques avec des paramètres :

```js
// Route avec paramètre
app.get('/user/:name', (req, res) => {
  res.send(`Bonjour ${req.params.name} !`);
});

// Route avec query string (?age=25)
app.get('/search', (req, res) => {
  res.send(`Âge recherché : ${req.query.age}`);
});

// Regrouper les routes dans un Router
const router = express.Router();
router.get('/profil', (req, res) => res.send('Profil utilisateur'));
app.use('/user', router);
```

---

### ES6 avec Node.js via Babel

Babel permet d'utiliser la syntaxe ES6+ (`import/export`) dans Node.js :

```bash
npm install @babel/core @babel/node @babel/preset-env --save-dev
```

Fichier `.babelrc` :
```json
{
  "presets": ["@babel/preset-env"]
}
```

Lancer le fichier avec Babel :
```bash
npx babel-node mon_fichier.js
```

---

### Développer plus vite avec Nodemon

Nodemon redémarre automatiquement le serveur à chaque modification de fichier :

```bash
npm install nodemon --save-dev
```

Dans `package.json` :
```json
"scripts": {
  "dev": "nodemon mon_fichier.js"
}
```

```bash
npm run dev
```

---

## Prérequis

| Élément | Détail |
|---------|--------|
| Environnement | Ubuntu 20.04 LTS |
| Runtime | Node 20.x.x |
| Gestionnaire de paquets | npm 9.x.x |
| Éditeurs autorisés | vi, vim, emacs, Visual Studio Code |
| Extension des fichiers | `.js` |
| Tests | Jest + Mocha (`npm run test`) |
| Linting | ESLint (`npm run full-test`) |
| Exports | Toutes les fonctions doivent être exportées |
| Fin de fichier | Tous les fichiers doivent se terminer par une nouvelle ligne |

## Installation

```bash
npm install
```

## Utilisation

Lancer tous les tests et le lint :
```bash
npm run full-test
```

Lancer les tests uniquement :
```bash
npm run test
```

Lancer le serveur en développement :
```bash
npm run dev
```

## Auteur

**Hinoto-LH** — [GitHub](https://github.com/Hinoto-LH)

*Projet réalisé dans le cadre du cursus Holberton School.*
