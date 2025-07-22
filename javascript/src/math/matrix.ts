import { MatrixIndexOutOfRangeException } from "./except";

/**
 *
 * @param c - target col 0-indexed
 * @param matrix
 */
export function reverseCol(c: number, matrix: number[][]): number[][] {
  const col = matrix[0].length;

  if (c < 0 || c >= col) {
    throw new MatrixIndexOutOfRangeException(
      `Matrix Index Out of Range\nnMatrix col: ${col}, c: ${c}`
    );
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
    throw new MatrixIndexOutOfRangeException(
      `Matrix Index Out of Range\nMatrix row: ${row}, r: ${r}`
    );
  }
  const reversedRow = [...matrix[r]].reverse();

  return [...matrix.slice(0, r), reversedRow, ...matrix.slice(r + 1)];
}

/**
 * @description swap col
 * @param c1 - target col 0-indexed
 * @param c2 - target col 0-indexed
 * @param matrix
 */
export function swapCol(
  c1: number,
  c2: number,
  matrix: number[][]
): number[][] {
  const col = matrix[0].length;

  if (c1 < 0 || c1 >= col || c2 < 0 || c2 >= col) {
    throw new MatrixIndexOutOfRangeException(
      `Matrix Index Out of Range\nMatrix col: ${col}, c1: ${c1}, c2: ${c2}`
    );
  }

  const newMatrix = [...matrix.map((row) => [...row])];

  for (let i = 0; i < matrix.length; i++) {
    const temp = matrix[i][c1];
    newMatrix[i][c1] = matrix[i][c2];
    newMatrix[i][c2] = temp;
  }

  return newMatrix;
}

/**
 * @description swap row
 * @param r1 - target row 0-indexed
 * @param r2 - target row 0-indexed
 * @param matrix
 */
export function swapRow(
  r1: number,
  r2: number,
  matrix: number[][]
): number[][] {
  const row = matrix.length;

  if (r1 < 0 || r1 >= row || r2 < 0 || r2 >= row) {
    throw new MatrixIndexOutOfRangeException(
      `Matrix Index Out of Range\nMatrix row: ${row}, r1: ${r1}, r2: ${r2}`
    );
  }

  const lessRow = r1 < r2 ? r1 : r2;
  const moreRow = r1 < r2 ? r2 : r1;

  return [
    ...matrix.slice(0, lessRow),
    matrix[moreRow],
    ...matrix.slice(lessRow + 1, moreRow),
    matrix[lessRow],
    ...matrix.slice(moreRow + 1),
  ];
}
/**
 * @description rotate matrix 90 degrees
 * @param matrix
 * @param clockwise - rotate clock wise if true, counter clock wise if false
 * @default clockwise true
 */
export function rotate90(
  matrix: number[][],
  clockwise: boolean = true
): number[][] {
  const rows = matrix.length;
  const cols = matrix[0].length;

  // 회전 후 행렬은 cols x rows 크기가 됨
  const rotated = Array.from({ length: cols }, () => Array(rows).fill(0));

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (clockwise) {
        rotated[j][rows - 1 - i] = matrix[i][j];
      } else {
        rotated[cols - 1 - j][i] = matrix[i][j];
      }
    }
  }

  return rotated;
}
