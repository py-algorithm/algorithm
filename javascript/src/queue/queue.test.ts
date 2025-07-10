import { Queue } from "./queue";

describe("Queue", () => {
  test("should be defined", () => {
    const queue = new Queue();
    expect(queue).toBeDefined();
  });
});
