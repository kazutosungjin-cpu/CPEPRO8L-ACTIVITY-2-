# Stacks and Queues — Guide Questions

## 1. Difference Between Stack and Queue

- **Stack (LIFO – Last In, First Out):** The element added last is the first one to be removed.
- **Queue (FIFO – First In, First Out):** The element added first is the first one to be removed.

## 2. Why Check for Overflow and Underflow

It is important to check for overflow and underflow before performing push/pop or enqueue/dequeue operations to prevent errors, data loss, and invalid memory access when adding to a full structure or removing from an empty one.

## 3. Advantage of a Circular Queue

The advantage of a circular queue is that it efficiently reuses empty spaces created by dequeue operations, unlike a simple linear queue, which may waste available space.

## 4. Real-World Applications

- **Stack:** Appropriate for the Undo function in a text editor, where the most recent action is undone first.
- **Queue:** Appropriate for a printer queue, where documents are printed in the order they were submitted.
