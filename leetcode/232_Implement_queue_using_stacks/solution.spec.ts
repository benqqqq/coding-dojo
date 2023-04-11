import { MyQueue } from './solution';
import { describe, test, expect, beforeEach } from 'vitest';

describe('MyQueue', () => {
  let queue;

  beforeEach(() => {
    queue = new MyQueue();
  });

  test('initial state', () => {
    expect(queue.toString()).toBe('');
    expect(queue.empty()).toBe(true);
  });

  test('push and peek', () => {
    queue.push(1);
    expect(queue.toString()).toBe('1');
    expect(queue.peek()).toBe(1);

    queue.push(2);
    expect(queue.toString()).toBe('1,2');
    expect(queue.peek()).toBe(1);

    queue.push(3);
    expect(queue.toString()).toBe('1,2,3');
    expect(queue.peek()).toBe(1);
  });

  test('pop', () => {
    queue.push(1);
    queue.push(2);
    queue.push(3);

    expect(queue.pop()).toBe(1);
    expect(queue.toString()).toBe('2,3');
    expect(queue.peek()).toBe(2);

    expect(queue.pop()).toBe(2);
    expect(queue.toString()).toBe('3');
    expect(queue.peek()).toBe(3);

    expect(queue.pop()).toBe(3);
    expect(queue.toString()).toBe('');
    expect(queue.empty()).toBe(true);
  });
});
