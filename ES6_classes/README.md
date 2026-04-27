# ES6 Classes

## Définir une classe

Une classe est un **modèle** pour créer des objets. Elle se définit avec le mot-clé `class` et contient un constructeur qui initialise les propriétés de l'instance.

```js
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const lion = new Animal('Lion', 5);
console.log(lion.name); // "Lion"
```

> Le `constructor` est appelé automatiquement lors du `new`.

---

## Ajouter des méthodes à une classe

Les méthodes se définissent directement dans le corps de la classe, sans le mot-clé `function`.

```js
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  speak() {
    return `${this.name} fait un bruit.`;
  }

  describe() {
    return `Je suis ${this.name} et j'ai ${this.age} ans.`;
  }
}

const chat = new Animal('Chat', 3);
console.log(chat.speak());    // "Chat fait un bruit."
console.log(chat.describe()); // "Je suis Chat et j'ai 3 ans."
```

### Getters & Setters

```js
class Animal {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw new Error('Le nom doit être une chaîne.');
    this._name = value;
  }
}

const chien = new Animal('Rex');
console.log(chien.name); // "Rex"
chien.name = 'Max';
console.log(chien.name); // "Max"
```

---

## Méthodes statiques

Une méthode **statique** appartient à la **classe elle-même**, pas à ses instances. Elle est utile pour des fonctions utilitaires liées à la classe.

### Pourquoi ?
- Pas besoin de créer une instance pour l'appeler
- Idéal pour des helpers, factories, ou validations

```js
class MathUtils {
  static add(a, b) {
    return a + b;
  }

  static multiply(a, b) {
    return a * b;
  }
}

console.log(MathUtils.add(2, 3));      // 5
console.log(MathUtils.multiply(4, 5)); // 20

// ❌ Impossible sur une instance
const utils = new MathUtils();
utils.add(1, 2); // TypeError
```

### Cas concret : factory method

```js
class User {
  constructor(name, role) {
    this.name = name;
    this.role = role;
  }

  static createAdmin(name) {
    return new User(name, 'admin');
  }
}

const admin = User.createAdmin('Alice');
console.log(admin.role); // "admin"
```

---

## Étendre une classe (Héritage)

Le mot-clé `extends` permet à une classe enfant d'hériter des propriétés et méthodes d'une classe parent.  
`super()` appelle le constructeur du parent.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} fait un bruit.`;
  }
}

class Chien extends Animal {
  speak() {
    return `${this.name} aboie.`;
  }
}

class Chat extends Animal {
  speak() {
    return `${this.name} miaule.`;
  }
}

const rex = new Chien('Rex');
const misty = new Chat('Misty');

console.log(rex.speak());   // "Rex aboie."
console.log(misty.speak()); // "Misty miaule."
```

### `super` pour appeler le parent

```js
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

class Chien extends Animal {
  constructor(name, age, breed) {
    super(name, age); // appelle le constructeur d'Animal
    this.breed = breed;
  }

  describe() {
    return `${this.name} est un ${this.breed} de ${this.age} ans.`;
  }
}

const rex = new Chien('Rex', 4, 'Labrador');
console.log(rex.describe()); // "Rex est un Labrador de 4 ans."
```

---

## Métaprogrammation et Symbols

### Qu'est-ce qu'un Symbol ?

Un `Symbol` est un type primitif **unique et immuable**. Deux symbols sont toujours différents, même s'ils ont le même nom.

```js
const sym1 = Symbol('description');
const sym2 = Symbol('description');

console.log(sym1 === sym2); // false — toujours uniques
```

### Utilité des Symbols

Ils permettent de créer des **clés de propriétés privées** qui n'entrent pas en conflit avec d'autres propriétés.

```js
const id = Symbol('id');

class User {
  constructor(name) {
    this.name = name;
    this[id] = Math.random(); // clé non accessible facilement de l'extérieur
  }
}

const user = new User('Alice');
console.log(user.name);  // "Alice"
console.log(user[id]);   // un nombre aléatoire
```

### Symbols bien connus (Well-Known Symbols)

ES6 expose des symbols intégrés qui permettent de modifier le comportement natif des objets — c'est la **métaprogrammation**.

| Symbol | Rôle |
|---|---|
| `Symbol.iterator` | Rendre un objet itérable (`for...of`) |
| `Symbol.toPrimitive` | Contrôler la conversion en valeur primitive |
| `Symbol.hasInstance` | Contrôler `instanceof` |
| `Symbol.toStringTag` | Personnaliser `Object.prototype.toString` |

### Exemple : rendre une classe itérable avec `Symbol.iterator`

```js
class Range {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  [Symbol.iterator]() {
    let current = this.start;
    const end = this.end;
    return {
      next() {
        return current <= end
          ? { value: current++, done: false }
          : { value: undefined, done: true };
      },
    };
  }
}

const range = new Range(1, 5);
for (const n of range) {
  console.log(n); // 1, 2, 3, 4, 5
}
```

### Exemple : personnaliser `toString` avec `Symbol.toStringTag`

```js
class Collection {
  get [Symbol.toStringTag]() {
    return 'Collection';
  }
}

const col = new Collection();
console.log(Object.prototype.toString.call(col)); // "[object Collection]"
```

---

## Ressources

- [MDN — Classes JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes)
- [MDN — Symbol](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
- [javascript.info — Classes](https://fr.javascript.info/classes)
