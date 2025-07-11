import { MatrixIndexOutOfRangeException } from "./except";
import { reverseCol, reverseRow, swapCol, swapRow } from "./matrix";

const matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
];

describe("reverseCol", () => {
  it("should reverseCol", () => {
    const reversed = reverseCol(1, matrix);
    expect(reversed).toEqual([
      [1, 10, 3, 4],
      [5, 6, 7, 8],
      [9, 2, 11, 12],
    ]);
  });

  it("throw error if out of index", () => {
    try {
      const outOfIndexErrorRes = reverseCol(4, matrix);
    } catch (error) {
      expect(error instanceof MatrixIndexOutOfRangeException).toBe(true);
      expect(error.message).toBe(
        `Matrix Index Out of Range\nnMatrix col: ${4}, c: ${4}`
      );
    }
  });
});

describe("reverseRow", () => {
  it("should reverseRow", () => {
    const reversed = reverseRow(1, matrix);
    expect(reversed).toEqual([
      [1, 2, 3, 4],
      [8, 7, 6, 5],
      [9, 10, 11, 12],
    ]);
  });

  it("throw error if out of index", () => {
    try {
      const outOfIndexErrorRes = reverseRow(4, matrix);
    } catch (error) {
      expect(error instanceof MatrixIndexOutOfRangeException).toBe(true);
      expect(error.message).toBe(
        `Matrix Index Out of Range\nMatrix row: ${3}, r: ${4}`
      );
    }
  });
});

describe("swapCol", () => {
  it("should swap col 1 and 2", () => {
    const swapped = swapCol(1, 2, matrix);
    expect(swapped).toEqual([
      [1, 3, 2, 4],
      [5, 7, 6, 8],
      [9, 11, 10, 12],
    ]);
  });

  it("throw error if out of index", () => {
    try {
      const outOfIndexErrorRes = swapCol(4, 2, matrix);
    } catch (error) {
      expect(error instanceof MatrixIndexOutOfRangeException).toBe(true);
      expect(error.message).toBe(
        `Matrix Index Out of Range\nMatrix col: ${4}, c1: ${4}, c2: ${2}`
      );
    }
  });
});

describe("swapRow", () => {
  it("should swap row 0 and 2", () => {
    const swapped = swapRow(0, 2, matrix);
    expect(swapped).toEqual([
      [9, 10, 11, 12],
      [5, 6, 7, 8],
      [1, 2, 3, 4],
    ]);
  });

  it("throw error if out of index", () => {
    try {
      const outOfIndexErrorRes = swapRow(4, 2, matrix);
    } catch (error) {
      expect(error instanceof MatrixIndexOutOfRangeException).toBe(true);
      expect(error.message).toBe(
        `Matrix Index Out of Range\nMatrix row: ${3}, r1: ${4}, r2: ${2}`
      );
    }
  });
});
