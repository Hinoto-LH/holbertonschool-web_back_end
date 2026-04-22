# NoSQL & MongoDB

---

## What NoSQL means

**NoSQL** (*Not Only SQL*) désigne une famille de bases de données qui ne reposent pas sur le modèle relationnel traditionnel (tables, lignes, colonnes).

Le terme "Not Only SQL" reflète l'idée que ces bases ne remplacent pas forcément SQL, mais offrent une **alternative adaptée à certains besoins** : grandes volumétries, données non structurées, scalabilité horizontale, flexibilité du schéma.

---

## SQL vs NoSQL

| Critère | SQL | NoSQL |
|---|---|---|
| Structure | Tables avec schéma fixe | Documents, clés-valeurs, graphes... |
| Schéma | Rigide (défini à l'avance) | Flexible (peut varier par entrée) |
| Relations | Jointures entre tables | Données souvent dénormalisées |
| Scalabilité | Verticale (+ de RAM/CPU) | Horizontale (+ de serveurs) |
| Transactions | ACID garanties | Eventual consistency (souvent) |
| Exemples | MySQL, PostgreSQL, SQLite | MongoDB, Redis, Cassandra, Neo4j |
| Cas d'usage | Données structurées, relations complexes | Big data, temps réel, schéma variable |

---

## What is ACID

**ACID** est un ensemble de propriétés qui garantissent la fiabilité des transactions dans une base de données.

| Propriété | Signification | Exemple |
|---|---|---|
| **A**tomicity | Tout ou rien — si une étape échoue, tout est annulé | Virement bancaire : débit + crédit, les deux ou aucun |
| **C**onsistency | La base reste dans un état valide avant et après | Un solde ne peut pas être négatif |
| **I**solation | Les transactions simultanées ne s'interfèrent pas | Deux achats en même temps du dernier article |
| **D**urability | Une transaction validée est permanente même en cas de crash | Les données survivent à un redémarrage |

Les bases SQL garantissent ACID nativement. Les bases NoSQL sacrifient souvent certaines propriétés au profit des performances et de la scalabilité.

---

## What is a document storage

Le **stockage document** est un type de base NoSQL où les données sont stockées sous forme de **documents** (généralement JSON ou BSON).

Chaque document est une unité autonome qui peut contenir des structures imbriquées (tableaux, sous-documents) sans schéma imposé.

```json
{
  "_id": "64a1f2e3c8b9d12345678abc",
  "name": "Emma",
  "age": 25,
  "address": {
    "city": "Paris",
    "zip": "75001"
  },
  "hobbies": ["coding", "reading"]
}
```

Contrairement au SQL, pas besoin de jointure : toutes les infos liées à un utilisateur sont dans **un seul document**.

**Exemples :** MongoDB, CouchDB, Firestore.

---

## NoSQL Types

Il existe 4 grandes familles de bases NoSQL :

### 1. Document stores
Données stockées en JSON/BSON. Flexibles et intuitifs.
> **Exemples :** MongoDB, CouchDB
> **Usage :** catalogues produits, profils utilisateurs, CMS

### 2. Key-Value stores
Structure la plus simple : une clé → une valeur. Ultra-rapide.
> **Exemples :** Redis, DynamoDB
> **Usage :** cache, sessions, files de messages

### 3. Column-family stores
Données organisées par colonnes plutôt que par lignes. Optimisé pour les agrégations sur de grandes colonnes.
> **Exemples :** Apache Cassandra, HBase
> **Usage :** analytics, IoT, séries temporelles

### 4. Graph databases
Données stockées comme des nœuds et des relations (arêtes). Parfait pour les données très connectées.
> **Exemples :** Neo4j, Amazon Neptune
> **Usage :** réseaux sociaux, moteurs de recommandation, détection de fraude

---

## Benefits of a NoSQL database

- **Schéma flexible** — pas besoin de migrer la base pour ajouter un champ
- **Scalabilité horizontale** — on ajoute des serveurs au lieu d'en améliorer un seul
- **Performances élevées** — optimisé pour lecture/écriture massive
- **Adapté au Big Data** — gère des volumes de données très importants
- **Développement agile** — le modèle de données évolue facilement avec le projet
- **Haute disponibilité** — réplication native et tolérance aux pannes

---

## How to query information from a NoSQL database

### Avec MongoDB

#### Trouver tous les documents
```javascript
db.users.find()
```

#### Trouver avec un filtre
```javascript
db.users.find({ age: 25 })
```

#### Opérateurs de comparaison
```javascript
db.users.find({ age: { $gt: 18 } })        // age > 18
db.users.find({ age: { $gte: 18 } })       // age >= 18
db.users.find({ age: { $lt: 30 } })        // age < 30
db.users.find({ age: { $in: [20, 25] } })  // age dans la liste
```

#### Filtres combinés
```javascript
db.users.find({ age: { $gt: 18 }, city: "Paris" })
```

#### Limiter / trier les résultats
```javascript
db.users.find().sort({ age: 1 }).limit(10)  // tri croissant, 10 résultats
db.users.find().sort({ age: -1 })           // tri décroissant
```

#### Trouver un seul document
```javascript
db.users.findOne({ name: "Emma" })
```

---

## How to insert / update / delete information

### Insérer

```javascript
// Un document
db.users.insertOne({ name: "Emma", age: 25, city: "Paris" })

// Plusieurs documents
db.users.insertMany([
  { name: "Liam", age: 22 },
  { name: "Olivia", age: 28 }
])
```

### Mettre à jour

```javascript
// Modifier un champ (updateOne)
db.users.updateOne(
  { name: "Emma" },           // filtre
  { $set: { age: 26 } }      // modification
)

// Modifier plusieurs documents (updateMany)
db.users.updateMany(
  { city: "Paris" },
  { $set: { country: "France" } }
)

// Incrémenter une valeur
db.users.updateOne({ name: "Emma" }, { $inc: { age: 1 } })
```

### Supprimer

```javascript
// Supprimer un document
db.users.deleteOne({ name: "Emma" })

// Supprimer plusieurs documents
db.users.deleteMany({ age: { $lt: 18 } })

// Vider une collection
db.users.deleteMany({})
```

---

## How to use MongoDB

### Lancer MongoDB (avec Docker)

```bash
docker start mongodb44
docker exec -it mongodb44 mongo
```

### Commandes de base du shell

```javascript
show dbs                    // lister les bases de données
use my_database             // créer / sélectionner une base
show collections            // lister les collections
db.dropDatabase()           // supprimer la base courante
```

### Workflow typique

```javascript
// 1. Sélectionner la base
use school

// 2. Insérer des données
db.students.insertMany([
  { name: "Alice", grade: "A", age: 20 },
  { name: "Bob",   grade: "B", age: 22 },
  { name: "Carol", grade: "A", age: 21 }
])

// 3. Requêter
db.students.find({ grade: "A" })

// 4. Mettre à jour
db.students.updateOne({ name: "Bob" }, { $set: { grade: "A" } })

// 5. Supprimer
db.students.deleteOne({ name: "Carol" })
```

### Avec Python (pymongo)

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["students"]

# Insérer
collection.insert_one({ "name": "Alice", "grade": "A" })

# Lire
for student in collection.find({ "grade": "A" }):
    print(student)

# Mettre à jour
collection.update_one({ "name": "Alice" }, { "$set": { "grade": "B" } })

# Supprimer
collection.delete_one({ "name": "Alice" })
```

---

## Résumé

| Action | MongoDB Shell | Python (pymongo) |
|---|---|---|
| Insérer | `insertOne()` / `insertMany()` | `insert_one()` / `insert_many()` |
| Lire | `find()` / `findOne()` | `find()` / `find_one()` |
| Mettre à jour | `updateOne()` / `updateMany()` | `update_one()` / `update_many()` |
| Supprimer | `deleteOne()` / `deleteMany()` | `delete_one()` / `delete_many()` |
