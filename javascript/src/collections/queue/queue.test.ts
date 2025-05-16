import { Queue } from "./queue";

describe("Queue", () => {
  it("should be defined", () => {
    const queue = new Queue();
    expect(queue).toBeDefined();
  });

  it("should initialize with given items", () => {
    const queue = new Queue([1, 2, 3]);
    expect(queue.length).toBe(3);
  });

  it("should pop the front item", () => {
    const queue = new Queue([1, 2, 3]);
    expect(queue.pop()).toBe(1);
  });

  it("should push a new item at the rear", () => {
    const queue = new Queue([1, 2, 3]);
    queue.push(4);
    expect(queue.front).toBe(1);
    expect(queue.rear).toBe(4);
  });

  it("should throw an error when popping from an empty queue", () => {
    const queue = new Queue();
    expect(() => queue.pop()).toThrow("queue is empty");
  });
});
