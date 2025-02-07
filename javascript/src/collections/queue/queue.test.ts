import { Queue } from "./queue";

describe("Queue", () => {
  test("should be defined", () => {
    const queue = Queue();
    expect(queue).toBeDefined();
  });
  test("should push itme", () => {
    const q = Queue();
    q.push(1);
    expect(q).toStrictEqual([1]);
    expect(q.length).toBe(1);
  });
});
