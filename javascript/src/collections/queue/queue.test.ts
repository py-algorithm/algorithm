import { Queue } from "./queue";

describe("Queue", () => {
  test("should be defined", () => {
    const queue = new Queue();

    expect(queue).toBeDefined();
  });

  test("should be init", () => {
    const queue = new Queue([1, 2, 3]);

    expect(queue.length).toBe(3);
  });

  test("should be pop front item", () => {
    const queue = new Queue([1, 2, 3]);

    expect(queue.pop()).toBe(1);
  });

  test("should be push rear item", () => {
    const queue = new Queue([1, 2, 3]);
    queue.push(4);
    expect(queue.front).toBe(1);
    expect(queue.rear).toBe(4);
  });

  test("should throw error if queue is empty", () => {
    const queue = new Queue();
    expect(() => queue.pop()).toThrow("queue is empty");
  });
});
