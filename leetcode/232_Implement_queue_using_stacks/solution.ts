export class MyQueue {
  // pushStack is used to store the push elements
  private pushStack: number[] = [];
  // popStack is used to store those ready to pop elements, when no elements here, pop it from pushStack
  private popStack: number[] = [];
  private frontend: number | null = null;

  public push(x: number): void {
    if (this.pushStack.length === 0) {
      this.frontend = x;
    }
    this.pushStack.push(x);
  }

  public pop(): number | null {
    if (this.popStack.length === 0) {
      while (this.pushStack.length > 0) {
        this.popStack.push(this.pushStack.pop());
      }
    }
    if (this.popStack.length === 0) {
      return null;
    }
    return this.popStack.pop();
  }

  public peek(): number | null {
    if (this.popStack.length > 0) {
      return this.popStack[this.popStack.length - 1];
    }
    if (this.pushStack.length > 0) {
      return this.frontend;
    }
    return null;
  }

  public empty(): boolean {
    return this.pushStack.length === 0 && this.popStack.length === 0;
  }

  public toString(): string {
    const reveredPopStack = [...this.popStack].reverse();
    return [...this.pushStack, ...reveredPopStack].toString();
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
