export function Queue<T = unknown>(iterable?: Iterable<T> | null | undefined) {
  const _data: T[] = iterable ? [...iterable] : [];
  let length = _data.length;

  return _data;
}

export default Queue;
