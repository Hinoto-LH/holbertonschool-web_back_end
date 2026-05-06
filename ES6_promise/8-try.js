export default function divideFunction(numerator, denominator) {
  // division par zéro est mathématiquement impossible
  if (denominator === 0) throw new Error('cannot divide by 0');
  return numerator / denominator;
}
