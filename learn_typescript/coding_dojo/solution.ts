export function isValidWalk(walk: string[]) {
  const countDirection = (direction: 'n' | 's' | 'w' | 'e') => (w: string[]) => w.filter((d) => d === direction).length;
  return (
    walk.length === 10 &&
    countDirection('n')(walk) - countDirection('s')(walk) === 0 &&
    countDirection('w')(walk) - countDirection('e')(walk) === 0
  );
}
