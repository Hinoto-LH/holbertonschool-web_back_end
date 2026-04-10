# Python Async Comprehensions

## Asynchronous Generators

Un **générateur asynchrone** est une fonction qui combine `async def` et `yield`. Il produit des valeurs une à une de manière asynchrone, ce qui permet d'effectuer des opérations non-bloquantes entre chaque valeur émise.

### Syntaxe de base

```python
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)       # opération non-bloquante
        yield random.uniform(0, 10)  # produit une valeur
```

### Consommer un générateur asynchrone

On utilise `async for` pour itérer sur un générateur asynchrone :

```python
async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

> Un générateur asynchrone **ne peut pas** utiliser `return` avec une valeur (seulement `return` vide pour arrêter l'itération).

### Différences : générateur classique vs asynchrone

| | Générateur classique | Générateur asynchrone |
|---|---|---|
| Déclaration | `def` + `yield` | `async def` + `yield` |
| Itération | `for x in gen()` | `async for x in gen()` |
| Opérations async | Non | Oui (`await`) |
| Type retourné | `Generator` | `AsyncGenerator` |

---

## Async Comprehensions

Les **comprehensions asynchrones** permettent de construire des listes, sets ou dicts à partir d'un générateur asynchrone, de manière concise et lisible.

### List comprehension asynchrone

```python
async def main():
    results = [value async for value in async_generator()]
    print(results)
```

### Avec condition (filtering)

```python
async def main():
    big_values = [v async for v in async_generator() if v > 5.0]
```

### Set et dict comprehensions asynchrones

```python
async def main():
    unique = {v async for v in async_generator()}
    mapping = {i: v async for i, v in enumerate(async_generator())}
```

### Avec `await` dans la comprehension

On peut aussi `await` des coroutines directement dans une comprehension, à condition d'être dans un contexte `async` :

```python
async def fetch(n):
    await asyncio.sleep(0.1)
    return n * 2

async def main():
    results = [await fetch(i) for i in range(5)]
```

> Note : `[await ...]` exécute les appels **séquentiellement**. Pour la concurrence, préférer `asyncio.gather()`.

---

## Type-Annotate Generators

### Générateur classique — `Generator`

```python
from typing import Generator

def count_up(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i
```

`Generator[YieldType, SendType, ReturnType]` :
- **YieldType** : type des valeurs produites par `yield`
- **SendType** : type envoyé via `.send()` (souvent `None`)
- **ReturnType** : type retourné à la fin (souvent `None`)

### Générateur asynchrone — `AsyncGenerator`

```python
from typing import AsyncGenerator

async def async_gen() -> AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(0.1)
        yield random.uniform(0, 10)
```

`AsyncGenerator[YieldType, SendType]` :
- **YieldType** : type des valeurs produites
- **SendType** : type envoyé via `.asend()` (souvent `None`)

### Iterator types (alternative simplifiée)

```python
from typing import Iterator, AsyncIterator

def simple_gen() -> Iterator[int]:
    yield 1
    yield 2

async def async_simple() -> AsyncIterator[float]:
    yield 1.0
    yield 2.0
```

`Iterator` et `AsyncIterator` sont plus simples quand on n'utilise pas `send()` ni `return`.

### Récapitulatif des types

| Cas d'usage | Type à importer | Signature |
|---|---|---|
| Générateur classique (complet) | `Generator` | `Generator[Y, S, R]` |
| Générateur classique (simple) | `Iterator` | `Iterator[Y]` |
| Générateur asynchrone (complet) | `AsyncGenerator` | `AsyncGenerator[Y, S]` |
| Générateur asynchrone (simple) | `AsyncIterator` | `AsyncIterator[Y]` |

---

## Exemple complet

```python
import asyncio
import random
from typing import AsyncGenerator, List

async def async_random_gen(size: int) -> AsyncGenerator[float, None]:
    for _ in range(size):
        await asyncio.sleep(0.1)
        yield random.uniform(0, 10)

async def collect(size: int) -> List[float]:
    return [v async for v in async_random_gen(size)]

asyncio.run(collect(10))
```
