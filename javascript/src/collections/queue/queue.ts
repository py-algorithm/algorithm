export type QueueItem<T> = {
  value: T;
  next: QueueItem<T> | null;
} | null;

export class Queue<T> {
  private _front: QueueItem<T> = null;
  private _rear: QueueItem<T> = null;
  private _length = 0;

  constructor(init?: Iterable<T>) {
    if (!init) {
      return;
    }
    for (const item of init) {
      this.push(item);
    }
  }

  push = (val: T) => {
    const newItem: QueueItem<T> = { value: val, next: null };
    if (this._front === null) {
      this._front = newItem;
    } else if (this._rear !== null) {
      this._rear.next = newItem;
    }

    this._rear = newItem;
    this._length++;
  };

  pop = () => {
    if (this._rear === null || this._front === null) {
      throw new Error("queue is empty");
    }
    const ret = this._front.value;
    this._front = this._front.next;
    this._length--;

    return ret;
  };

  get front() {
    return this._front?.value;
  }

  get rear() {
    return this._rear?.value;
  }

  get length() {
    return this._length;
  }
}
