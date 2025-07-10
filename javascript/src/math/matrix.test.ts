import { reverseRow } from "./matrix";

describe("reverseRow", () => {
  const matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
  ];

  it("should reverseRow", () => {
    const reversed = reverseRow(1, matrix);
    expect(reversed).toEqual([
      [1, 2, 3, 4],
      [8, 7, 6, 5],
      [9, 10, 11, 12],
      [13, 14, 15, 16],
    ]);
  });

  it("throw error if out of index", () => {
    try {
      const outOfIndexErrorRes = reverseRow(4, matrix);
    } catch (error) {
      expect(error.message).toBe(`Matrix Index Out of Range\nr: ${4}`);
    }
  });
});
