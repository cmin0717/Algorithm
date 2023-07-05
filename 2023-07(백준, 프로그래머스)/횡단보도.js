const path = process.platform === "win32" ? "input.txt" : "dev/stdin";
const splitType = process.platform === "win32" ? "\r\n" : "\n";
const input = require("fs")
  .readFileSync(path)
  .toString()
  .trim()
  .split(splitType);

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.length = 0;
  }

  enqueue(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
    } else {
      this.rear.next = node;
    }
    this.rear = node;
    this.length++;
  }

  dequeue() {
    if (!this.head) {
      return false;
    }
    const data = this.head.data;
    this.head = this.head.next;
    this.length--;

    return data;
  }
}

const [n, m] = input.shift().split(" ").map(Number);
const link = Array.from(Array(n + 1), () => []);

input.forEach((line, i) => {
  const [s, e] = line.split(" ").map(Number);
  link[s].push([i + 1, e]);
  link[e].push([i + 1, s]);
});

const visit = Array(n + 1).fill(Infinity);
visit[1] = 0;
const q = new Queue()
q.enqueue([1,0])

while (q.length !== 0) {
  let [now, cost] = q.dequeue()

  if (visit[now] < cost) {
    continue;
  }

  for (let [c, next] of link[now]) {
    const [div, mod] = [Math.floor(cost / m), cost % m];
    const new_cost = mod < c ? m * div + c : m * (div + 1) + c;
    if (visit[next] > new_cost) {
      visit[next] = new_cost;
      q.enqueue([next, new_cost])
    }
  }
}
console.log(visit[n]);

// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int, input().split())
// link = [[] for _ in range(n+1)]
// visit = [float('inf')] * (n+1)

// for i in range(1,m+1):
//     s,e = map(int, input().split())
//     link[s].append((i, e))
//     link[e].append((i, s))

// q = deque([(0, 1)])
// visit[1] = 0
// while q:
//     cost, now = q.popleft()

//     if visit[now] < cost:
//         continue

//     for c, next in link[now]:
//         div,mod = divmod(cost, m)
//         new_cost = m*div + c if mod < c else  m*(div+1) + c
//         if visit[next] > new_cost:
//             visit[next] = new_cost
//             q.append((new_cost, next))
// print(visit[n])
