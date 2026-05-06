# ES6 Promises

## Description

Ce projet explore les Promises en JavaScript ES6+, un mécanisme fondamental pour gérer les opérations asynchrones. Vous apprendrez à créer, chaîner et gérer des Promises, ainsi qu'à utiliser `async/await` pour écrire du code asynchrone lisible et maintenable.

## Ressources

- [Promise](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise : Introduction](https://web.dev/promises/)
- [Await](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/throw)

## Objectifs pédagogiques

À la fin de ce projet, vous devez être capable d'expliquer :

---

### Promises : comment, pourquoi et quoi

Une **Promise** (promesse) représente une valeur qui sera disponible dans le futur — immédiatement, plus tard, ou jamais. Elle a trois états possibles :

| État | Description |
|------|-------------|
| `pending` | En attente, opération en cours |
| `fulfilled` | Résolue avec succès |
| `rejected` | Échouée avec une erreur |

```js
const promise = new Promise((resolve, reject) => {
  const succes = true;
  if (succes) resolve('Opération réussie !');
  else reject(new Error('Quelque chose a mal tourné'));
});
```

**Pourquoi les utiliser ?** Pour éviter le "callback hell" et gérer proprement les opérations asynchrones (appels API, lecture de fichiers, timers...).

---

### Les méthodes `then`, `resolve` et `catch`

- **`then`** : s'exécute quand la Promise est résolue. Permet de chaîner des opérations.
- **`catch`** : intercepte les erreurs si la Promise est rejetée.
- **`resolve`** : crée directement une Promise déjà résolue.

```js
Promise.resolve('Bonjour')
  .then((valeur) => {
    console.log(valeur); // 'Bonjour'
    return valeur + ' le monde !';
  })
  .then((valeur) => console.log(valeur)) // 'Bonjour le monde !'
  .catch((err) => console.error(err));
```

---

### Toutes les méthodes de l'objet Promise

| Méthode | Description |
|---------|-------------|
| `Promise.resolve(val)` | Retourne une Promise résolue avec `val` |
| `Promise.reject(err)` | Retourne une Promise rejetée avec `err` |
| `Promise.all(promises)` | Attend que **toutes** les Promises soient résolues. Échoue si l'une échoue |
| `Promise.allSettled(promises)` | Attend que **toutes** soient terminées, qu'elles réussissent ou échouent |
| `Promise.any(promises)` | Retourne la **première** résolue avec succès |
| `Promise.race(promises)` | Retourne la **première** terminée (résolue ou rejetée) |

```js
const p1 = Promise.resolve(1);
const p2 = Promise.resolve(2);
const p3 = Promise.resolve(3);

Promise.all([p1, p2, p3]).then((valeurs) => console.log(valeurs)); // [1, 2, 3]
Promise.race([p1, p2, p3]).then((val) => console.log(val));        // 1
```

---

### Throw / Try

`try/catch` permet de gérer les erreurs de manière synchrone. Avec les Promises et `async/await`, il capture aussi les rejets.

```js
function diviser(a, b) {
  if (b === 0) throw new Error('Division par zéro impossible');
  return a / b;
}

try {
  console.log(diviser(10, 0));
} catch (err) {
  console.error(err.message); // 'Division par zéro impossible'
}
```

---

### L'opérateur `await`

`await` met en **pause** l'exécution d'une fonction `async` jusqu'à ce que la Promise soit résolue. Cela rend le code asynchrone aussi lisible que du code synchrone.

```js
async function fetchData() {
  const data = await fetch('https://api.example.com/data');
  const json = await data.json();
  return json;
}
```

> `await` ne peut s'utiliser qu'à l'intérieur d'une fonction `async`.

---

### Les fonctions `async`

Une fonction déclarée avec `async` retourne **toujours une Promise**, même si elle retourne une valeur simple.

```js
async function bonjour() {
  return 'Bonjour !';
}

// Équivalent à :
function bonjour() {
  return Promise.resolve('Bonjour !');
}

bonjour().then(console.log); // 'Bonjour !'
```

Combinée avec `await` et `try/catch`, elle remplace élégamment les chaînes de `.then().catch()` :

```js
async function getData() {
  try {
    const result = await someAsyncOperation();
    console.log(result);
  } catch (err) {
    console.error('Erreur :', err.message);
  }
}
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
| Tests | Jest (`npm run test`) |
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

## Auteur

**Hinoto-LH** — [GitHub](https://github.com/Hinoto-LH)

*Projet réalisé dans le cadre du cursus Holberton School.*
