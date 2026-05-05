# ES6 Data Manipulation

## Description

Ce projet couvre les techniques avancées de manipulation de données en JavaScript ES6+, notamment l'utilisation de `map`, `filter` et `reduce` sur les tableaux, ainsi que les Typed Arrays et les nouvelles structures de données introduites en ES6 : `Set`, `Map` et `WeakMap`.

## Ressources

- [Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Typed_arrays)
- [Set](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

## Objectifs pédagogiques

À la fin de ce projet, vous devez être capable d'expliquer :

- **Utilisation de map, filter et reduce sur les tableaux** : `map` transforme chaque élément d'un tableau en appliquant une fonction, `filter` sélectionne uniquement les éléments qui satisfont une condition, et `reduce` agrège tous les éléments en une seule valeur (somme, objet, etc.).

```js
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(n => n * 2);       // [2, 4, 6, 8, 10]
const evens   = numbers.filter(n => n % 2 === 0); // [2, 4]
const sum     = numbers.reduce((acc, n) => acc + n, 0); // 15
```

- **Tableaux typés** : les tableaux typés (`Int8Array`, `Float32Array`, etc.) permettent de stocker des données binaires brutes avec un type fixe, offrant de meilleures performances pour les opérations bas niveau comme le traitement de fichiers ou la communication réseau.

```js
const buffer = new ArrayBuffer(4);
const view   = new Int8Array(buffer);
view[0] = 42;
console.log(view[0]); // 42
```

- **Les structures de données Set, Map et WeakMap** : `Set` stocke des valeurs uniques sans doublons, `Map` associe des clés à des valeurs avec n'importe quel type de clé, et `WeakMap` fait la même chose mais avec des références faibles, permettant au garbage collector de libérer la mémoire automatiquement.

```js
// Set
const set = new Set([1, 2, 2, 3]);
console.log(set); // Set { 1, 2, 3 }

// Map
const map = new Map();
map.set('pomme', 5);
map.set('banane', 3);
console.log(map.get('pomme')); // 5

// WeakMap
const weakMap = new WeakMap();
const obj = {};
weakMap.set(obj, 'valeur');
console.log(weakMap.get(obj)); // 'valeur'
```

## Prérequis

| Élément | Détail |
|---------|--------|
| Environnement | Ubuntu 20.04 LTS |
| Runtime | Node 20.x.x |
| Gestionnaire de paquets | npm 9.x.x |
| Éditeurs autorisés | vi, vim, emacs, Visual Studio Code |
| Extension des fichiers | `.js` |
| Tests | Jest (`npm run test`) |
| Lint | ESLint (`npm run full-test`) |
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

## Tâches

### 0. Liste de base d'objets
**Fichier :** `0-get_list_students.js`

Retourne un tableau d'objets étudiants avec les attributs `id`, `firstName` et `location`.

---

### 1. Mapping
**Fichier :** `1-get_list_student_ids.js`

Retourne un tableau des IDs d'étudiants à partir d'une liste d'objets en utilisant `map`.

---

### 2. Filter
**Fichier :** `2-get_students_by_loc.js`

Retourne les étudiants situés dans une ville spécifique en utilisant `filter`.

---

### 3. Reduce
**Fichier :** `3-get_ids_sum.js`

Retourne la somme de tous les IDs d'étudiants en utilisant `reduce`.

---

### 4. Combinaison
**Fichier :** `4-update_grade_by_city.js`

Retourne les étudiants d'une ville donnée avec leurs notes mises à jour, en utilisant `filter` et `map`.

---

### 5. Typed Arrays
**Fichier :** `5-typed_arrays.js`

Crée un `Int8Array` et définit une valeur entière à une position spécifique.

---

### 6. Structure de données Set
**Fichier :** `6-set.js`

Retourne un `Set` créé à partir d'un tableau.

---

### 7. Plus de Set
**Fichier :** `7-has_array_values.js`

Retourne un booléen indiquant si tous les éléments d'un tableau sont présents dans un `Set` donné.

---

### 8. Nettoyage de Set
**Fichier :** `8-clean_set.js`

Retourne une chaîne des valeurs du Set commençant par une chaîne donnée, séparées par `-`.

---

### 9. Structure de données Map
**Fichier :** `9-groceries_list.js`

Retourne une `Map` d'articles de courses avec leurs quantités.

---

### 10. Plus de Map
**Fichier :** `10-update_uniq_items.js`

Met à jour toutes les entrées d'une Map dont la quantité est `1` à `100`.

---

### 11. WeakMap
**Fichier :** `11-weak.js`

Utilise une `WeakMap` pour suivre le nombre d'appels à `queryAPI` par endpoint. Lève une erreur quand le compteur atteint 5 ou plus.

---

## Auteur

**Hinoto-LH** — [GitHub](https://github.com/Hinoto-LH)

*Projet réalisé dans le cadre du cursus Holberton School.*
