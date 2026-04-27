# ES6 - Les Bases

## Qu'est-ce qu'ES6 ?

**ES6** (aussi appelé **ECMAScript 2015**) est la sixième édition du standard ECMAScript — la spécification sur laquelle JavaScript est basé. Publié en juin 2015, il a introduit des améliorations majeures au langage, rendant JavaScript plus puissant, lisible et expressif.

---

## Nouvelles fonctionnalités introduites dans ES6

| Fonctionnalité | Description |
|---|---|
| `let` / `const` | Déclarations de variables à portée de bloc |
| Fonctions fléchées | Syntaxe raccourcie avec `this` lexical |
| Paramètres par défaut | Valeurs par défaut pour les arguments |
| Rest / Spread | Gestion d'arguments en nombre variable |
| Template literals | Expressions intégrées dans les chaînes |
| Déstructuration | Extraire des valeurs de tableaux/objets |
| Classes | Syntaxe plus claire pour la POO |
| Modules | Système `import` / `export` |
| Promises | Code asynchrone plus propre |
| Itérateurs & `for...of` | Parcourir des objets itérables |

---

## Constante vs Variable

| | `var` | `let` | `const` |
|---|---|---|---|
| Portée | Fonction | Bloc | Bloc |
| Réassignable | Oui | Oui | Non |
| Re-déclarable | Oui | Non | Non |
| Hissée (hoisting) | Oui (undefined) | Oui (TDZ) | Oui (TDZ) |

```js
var nom = "Alice";    // portée fonction, peut être re-déclarée
let age = 25;         // portée bloc, peut être réassignée
const PI = 3.14159;   // portée bloc, ne peut PAS être réassignée
```

> **TDZ** = Zone Morte Temporelle : la variable existe mais ne peut pas être accédée avant sa déclaration.

---

## Variables à portée de bloc

`let` et `const` sont limitées au bloc `{ }` le plus proche, contrairement à `var` qui s'échappe des blocs.

```js
{
  let blocVar = "J'existe seulement ici";
  const blocConst = 42;
}
// console.log(blocVar); // ReferenceError

for (let i = 0; i < 3; i++) {
  // `i` est limité à cette boucle uniquement
}
// console.log(i); // ReferenceError
```

---

## Fonctions fléchées & Paramètres par défaut

### Fonctions fléchées

Une syntaxe plus courte pour écrire des fonctions. Elles ne **lient pas leur propre `this`**.

```js
// Traditionnelle
function addition(a, b) {
  return a + b;
}

// Fléchée
const addition = (a, b) => a + b;

// Un seul paramètre — parenthèses optionnelles
const double = n => n * 2;

// Sans paramètre
const saluer = () => "Bonjour !";
```

### Paramètres par défaut

Assigner une valeur par défaut si aucune valeur n'est fournie.

```js
function saluer(nom = "Monde") {
  return `Bonjour, ${nom} !`;
}

saluer("Alice"); // "Bonjour, Alice !"
saluer();        // "Bonjour, Monde !"
```

---

## Paramètres Rest & Spread

### Rest `...`

Regroupe plusieurs arguments dans un seul tableau.

```js
function somme(...nombres) {
  return nombres.reduce((acc, n) => acc + n, 0);
}

somme(1, 2, 3, 4); // 10
```

### Spread `...`

Étale un itérable (tableau, chaîne) en éléments individuels.

```js
const nums = [1, 2, 3];

Math.max(...nums);           // 3
const copie = [...nums, 4]; // [1, 2, 3, 4]

const obj1 = { a: 1 };
const obj2 = { ...obj1, b: 2 }; // { a: 1, b: 2 }
```

---

## Template Literals

Chaînes entourées de backticks `` ` `` qui supportent les expressions intégrées et le texte multiligne.

```js
const nom = "Alice";
const age = 25;

// Interpolation d'expression
const message = `Je m'appelle ${nom} et j'ai ${age} ans.`;

// Chaînes multilignes
const html = `
  <div>
    <h1>Bonjour, ${nom} !</h1>
  </div>
`;

// Expressions dans ${}
const resultat = `2 + 2 = ${2 + 2}`;
```

---

## Création d'objets et leurs propriétés en ES6

### Noms de propriétés raccourcis

```js
const nom = "Alice";
const age = 25;

// ES5
const utilisateur = { nom: nom, age: age };

// ES6 raccourci
const utilisateur = { nom, age };
```

### Noms de propriétés calculés

```js
const cle = "couleur";
const obj = { [cle]: "bleu" }; // { couleur: "bleu" }
```

### Méthodes raccourcies

```js
// ES5
const obj = {
  saluer: function() { return "Bonjour"; }
};

// ES6
const obj = {
  saluer() { return "Bonjour"; }
};
```

### Déstructuration

```js
const { nom, age } = utilisateur;
const [premier, deuxieme] = [10, 20];
```

---

## Itérateurs & Boucles for...of

### Qu'est-ce qu'un itérateur ?

Un objet est **itérable** s'il implémente la méthode `[Symbol.iterator]` qui retourne un itérateur avec une méthode `next()`.

Itérables natifs : `Array`, `String`, `Map`, `Set`, `arguments`, `NodeList`.

```js
const iter = [1, 2, 3][Symbol.iterator]();
iter.next(); // { value: 1, done: false }
iter.next(); // { value: 2, done: false }
iter.next(); // { value: 3, done: false }
iter.next(); // { value: undefined, done: true }
```

### Boucle for...of

Parcourt n'importe quel objet itérable — plus propre que `for` ou `forEach`.

```js
const fruits = ["pomme", "banane", "cerise"];

for (const fruit of fruits) {
  console.log(fruit);
}

// Fonctionne sur les chaînes aussi
for (const char of "bonjour") {
  console.log(char); // b, o, n, j, o, u, r
}

// Fonctionne sur les Maps
const map = new Map([["a", 1], ["b", 2]]);
for (const [cle, valeur] of map) {
  console.log(cle, valeur);
}
```

### Itérateur personnalisé

```js
function intervalle(debut, fin) {
  return {
    [Symbol.iterator]() {
      let courant = debut;
      return {
        next() {
          return courant <= fin
            ? { value: courant++, done: false }
            : { value: undefined, done: true };
        }
      };
    }
  };
}

for (const n of intervalle(1, 5)) {
  console.log(n); // 1, 2, 3, 4, 5
}
```

---

## Ressources

- [MDN Web Docs — JavaScript (FR)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [Spécification ECMAScript 2015](https://www.ecma-international.org/ecma-262/6.0/)
- [javascript.info](https://javascript.info/)
