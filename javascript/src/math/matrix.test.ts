import { reverseCol, reverseRow } from "./matrix";

const matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
];

describe("reverseCol", () => {
  it("should reverseCol", () => {
    const reversed = reverseCol(1, matrix);
    console.log(reversed);
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
      expect(error.message).toBe(
        `Matrix Index Out of Range\nMatrix row: ${3}, r: ${4}`
      );
    }
  });
});
