/**
 * @description reverse row
 * @param r
 * @param matrix
 */
export function reverseRow(r: number, matrix: number[][]): number[][] {
  const row = matrix.length;

  if (r < 0 || r >= row) {
    throw new Error(`Matrix Index Out of Range\nr: ${r}`);
  }
  const reversedRow = matrix[r].reverse();

  return [...matrix.slice(0, r), reversedRow, ...matrix.slice(r + 1)];
}
