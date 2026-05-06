export default function guardrail(mathFunction) {
  const queue = [];
  try {
    // on exécute la fonction et on ajoute le résultat au tableau
    queue.push(mathFunction());
  } catch (err) {
    // si une erreur est levée, on ajoute le message d'erreur
    queue.push(err.message);
  } finally {
    // toujours exécuté, qu'il y ait une erreur ou non
    queue.push('Guardrail was processed');
  }
  return queue;
}
