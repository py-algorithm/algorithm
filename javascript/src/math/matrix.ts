/**
 *
 * @param c - target col 0-indexed
 * @param matrix
 */
export function reverseCol(c: number, matrix: number[][]): number[][] {
  const col = matrix[0].length;

  if (c < 0 || c >= col) {
    throw new Error(`Matrix Index Out of Range\nnMatrix col: ${col}, c: ${c}`);
  }

  const newMatrix = [...matrix.map((row) => [...row])];

  for (let i = 0; i < matrix.length; i++) {
    const temp = matrix[i][c];
    newMatrix[i][c] = matrix[matrix.length - 1 - i][c];
    newMatrix[matrix.length - 1 - i][c] = temp;
  }

  return newMatrix;
}

/**
 * @description reverse row
 * @param r - target row 0-indexed
 * @param matrix
 */
export function reverseRow(r: number, matrix: number[][]): number[][] {
  const row = matrix.length;

  if (r < 0 || r >= row) {
    throw new Error(`Matrix Index Out of Range\nMatrix row: ${row}, r: ${r}`);
  }
  const reversedRow = matrix[r].reverse();

  return [...matrix.slice(0, r), reversedRow, ...matrix.slice(r + 1)];
}
