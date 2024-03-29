# Data Structure

1. [배열 (Array)](배열-(Array))
2. [연결 리스트 (Linked List)](#연결-리스트-(Linked-List))
3. [이중 연결 리스트 (Doubly Linked List)](#이중-연결-리스트-(Doubly-Linked-List))
4. [스택 (Stack)](#스택-(Stack))
5. [큐 (Queue)](#큐-(Queue))
6. [해시 테이블 (Hash Table)](#해시-테이블-(Hash-Table))
7. [트리 (Tree)](#트리-(Tree))
8. [이진 트리 (Binary Tree)](#이진-트리-(Binary-Tree))
9. [힙 (Heap)](#힙-(Heap))
10. [이진 탐색 트리 (Binary Search Tree)](#이진-탐색-트리-(Binary-Search-Tree))
11. [AVL 트리](#AVL-트리)
12. [Red-Black 트리](#Red-Black-트리)
13. [그래프 (Graph)](#그래프-(Graph))


------------------------------------------------------
<br>

## [배열 (Array)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(n) | O(n) | O(n) |

배열은 한가지 데이터 타입으로 묶어진 집합이다. 배열은 생성할 때 크기를 정해줘야 한다.

```
int[] array = new int[5]; // 배열 크기가 5인 int 배열
```

기본적으로 배열은 정적 데이터이므로 스택에 할당이 된다. 즉, 배열의 크기를 정했으면 주어진 크기에서 연산 작업으 할 수 있으나 새로 데이터를 뒤에 추가하거나 삭제해서 크기를 줄일 수 없다. 만약 크기를 변경하고 싶으면 새로운 크기의 배열을 생성한 후 기존 배열에 있는 데이터들을 복사해야 한다. 반대로 Java에서 ArrayList는 동적 할당이 가능해서 데이터를 새로 추가하거나 삭제할 수 있다. 동적 할당이므로 힙 영역에서 실행이 된다.

<br>

## [연결 리스트 (Linked List)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(1) | O(n) | O(1) |

연결 리스트는 데이터가 노드의 연결로 지어진 자료구조이다. 배열의 크기를 크게 정하면 자원을 낭비하게 된다. 그러므로 연결 리스트는 일정 크기를 메모리게 지정하지 않고 필요할 때 노드를 생성해서 이어주는 방식으로 데이터 연산들을 처리한다. 배열에서는 데이터를 추가하거나 제거하려면 새로운 배열을 생성해서 기존 배열의 데이터를 복사해야 된다. 그러나 연결 리스트는 현재 노드와 추가/제거할 노드간의 연결을 이어주거나 끊으면 되어서 효율적이다. 하지만 연결 리스트는 다음 노드에 대한 정보가 필요하므로 추가적인 자원이 필요하다.

![](pics/linkedlist.png)

[이미지 출처](https://www.geeksforgeeks.org/data-structures/linked-list/)

<br>

## [이중 연결 리스트 (Doubly Linked List)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(1) | O(n) | O(1) |

연결 리스트는 다음 노드에 대한 주소가 있는 반면 이중 연결 리스트는 이전 노드에 대한 주소도 가지고 있는 연결 리스트이다. 만약 연결 리스트를 사용하면 이전 노드에 정보가 없어서 느린 포인터와 빠른 포인터를 사용해서 연산 작업을 해야 할 때가 많다. 그러므로 하나의 연결 리스트에 이전 노드와 다음 노드에 대한 정보를 두어서 쉽게 노드들간의 연산을 할 수 있게 도와준다.

![](pics/doublylinkedlist.png)

[이미지 출처](https://www.geeksforgeeks.org/data-structures/linked-list/)

<br>

## [스택 (Stack)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(1) | O(n) | O(1) |

스택은 Last-In-First-Out (LIFO) 형식으로 데이터를 관리하는 자료구조이다. 즉, 마지막으로 들어간 데이터를 먼저 꺼내는 형식의 구조이다.

<br>

## [큐 (Queue)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(1) | O(n) | O(1) |

큐는 스택과 반대로 First-In-First-Out (FIFO) 형식으로 구성된 자료구조이다. 먼저 들어온 데이터를 먼저 꺼내는 방식이다. 큐 외에도 **덱 (Deque, Double-ended Queue)** 라는 자료구조가 있다. 큐와 반대로 양쪽에서 데이터를 넣고 빼는 작업을 할 수 있다.

<br>

## [해시 테이블 (Hash Table)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(n) | O(n) | O(n) |

해시 테이블은 키와 값을 사용해서 데이터를 관리하는 자료구조이다. 키는 해시 함수를 사용해서 나온 해시값의 셀에 원래의 데이터를 삽입한다. 그 외에도 검색할 때도 키의 해시값을 구해서 해당 셀에 접근할 수 있어서 O(1)이라는 시간이 걸린다.

![](pics/graph8.png)

[이미지 출처](https://en.wikipedia.org/wiki/Hash_table)


하지만 **해시 함수 (hash function)** 를 잘못 고를경우 키의 값은 다르나 해시값이 같아질 수 있다. 이를 **해시 충돌 (hash collision)** 이라고 한다. 해시 충돌에 대한 해결 방법은 다음과 같다.

**1. Open addressing**

개방 주소 방법은 충돌된 값을 다른 셀에 저장하는 방법이다. **Linear probing** 방법은 충돌 된 셀 옆으로 이동하면서 빈 공간이 나오면 저장하는 방법이다 (마지막 셀에 들면 첫번째 셀로 이동한다). 최악의 경우 검색을 할 때 테이블 전채를 확인해야 할 수 있어 O(n) 이라는 시간 복잡도를 갖는다. 그 외에도 **double hashing** 을 통해 해시 함수를 하나 더 사용하는 방법이다.

![Linear Probing](pics/linearprobing.png)

**2.Chaining**

체이닝은 해당 키의 셀에 연결 리스트를 사용해서 같은 해시값을 가진 데이터들을 연결해 추가하는 방식이다. 이렇게 되면 최악의 경우 한 셀에 데이터가 몰릴 수 있어서 O(n) 이라는 시간 복잡도를 갖는다.

![Chaining](pics/chaining.png)

<br>

## [트리 (Tree)](#Data-Structure)

트리 자료구는 계층 구조의 추상적 모델이다.

## [이진 트리 (Binary Tree)](#Data-Structure)

이진 트리는 각 노드가 최대 2개의 자식 노드를 가질 수 있는 트리 구조이다.

![](pics/binarytree.png)

[이미지 출처](https://en.wikipedia.org/wiki/Binary_tree)


**1. Full Binary Tree (정 이진 트리)**

각 노드는 0개 아니면 최대 2개의 자식 노드를 갖는 트리이다.

![](pics/fullbinarytree.png)

[이미지 출처](https://en.wikipedia.org/wiki/Binary_tree)


**2. Complete Binary Tree (완전 이진 트리)**

마지막 레벨을 제외하고 모든 노드는 2개의 자식 노드를 가지고 있어야 하며 마지막 레벨은 왼쪽부터 순차적으로 채워져야 하는 구조이다.

![](pics/completebinarytree.png)

[이미지 출처](https://en.wikipedia.org/wiki/Binary_tree)


**3. Perfect Binary Tree (포화 이진 트리)**

정 이진 트리와 완전 이진 트리를 합친 트리라고 볼 수 있다. 모든 내부 노드는 2개의 자식 노드를 가지고 있어야 한며 leaf 노드들은 같은 레벨에 있어야 한다.

![](pics/perfectbinarytree.png)

[이미지 출처](https://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/)


<br>

## [힙 (Heap)](#Data-Structure)

|   삽입    | 검색  |   삭제    | 최대/최소 검색 |
|----------|------|----------|-------------|
| O(log n) | O(n) | O(log n) |     O(1)    |

힙은 완전 이진 트리 구조를 사용하여 최솟값 또는 최댓값을 구하기 위한 자료구조이다. 힙 구조에는 최소 힙 (Min heap) 과 최대 힙 (Max heap) 이 있다. 최소 힙은 각 노드 값이 자식 노드보다 작은 값을 가지게 구현된 구조이고 반대로 최대 힙은 각 노드 값이 자식 노드들의 값보다 큰 값을 가진 구조이다. 힙 구조는 우선순위 큐에 주로 사용된다. 우선순위 큐란 값에 순위로 두어서 순차적으로 값을 가져올 수 있게 도와주는 구조이다.

힙 구조는 완전 이진 트리이므로 마지막 레벨의 맨 오른쪽 노드에 노드가 삽입된다. 그리고 heapify를 통해 최대/최소 힙 구조로 변환시킨다.

삭제를 할 때는 루트 값을 마지막 레벨의 맨 오른쪽 노드와 교체한 후 기존 루트 노드를 제거한다. 교체 후 새로운 루트 노드를 시작으로 heapify를 실행시켜 최대/최소 힙 구조로 변환시킨다.

![](pics/graph9.png)

![](pics/graph10.png)

배열에 있는 데이터들을 힙으로 구현힐 수 있으며 최대 힙으로 바꿀 수 있다.


![](pics/heap1.png)

![](pics/heap2.png)

![](pics/heap3.png)

![](pics/heap4.png)

![](pics/heap5.png)

Max heap 으로 바꾸는 과정이다.

<br>

## [이진 탐색 트리 (Binary Search Tree)](#Data-Structure)

| 삽입  | 검색  | 삭제  |
|------|------|------|
| O(n) | O(n) | O(n) |

이진 프리는 각 노드에 최대 2개의 자식 노드를 가질 수 있다. 그런데 값을 지정하는데 제한이 없어서 특정 값을 검색하려면 모든 노드를 탐색하면서 찾아야 한다. 이를 개선하기 위해서 이진 탐색 트리는 왼쪽 자식 노드는 부모 노드보다 작아야 하고 오른쪽 자식 노드는 부모 노드보다 값이 커야되는 자료구조이다. 즉, 부모 노드의 왼쪽 서브 트리의 모든 노드 값들은 부모 노드보다 값이 작아야 하고 오른쪽 서브 트리의 값들은 부모 노드보다 값이 커야 한다. 그 결과 검색, 삽입, 제거 작업들을 O(log n)에 달성할 수 있다. 하지만 이진 탐색 트리는 불균형하게 구성될 수 있어서 최악의 경우 O(n) 시간 복잡도를 갖는다.

![](pics/binarysearchtree.png)

[이미지 출처](https://en.wikipedia.org/wiki/Binary_search_tree)


<br>

## [AVL 트리](#Data-Structure)

|   삽입    |   검색    |   삭제    |
|----------|----------|----------|
| O(log n) | O(log n) | O(log n) |


이진 탐색 트리는 검색을 효율적으로 하기 위해 사용하지만 불균형적으로 구성되면 O(n) 이라는 시간 복잡도를 갖는다. 그래서 AVL 트리는 항상 균형을 잡아 O(log n) 으로 연산 작업을 할 수 있게 해주는 자료구조이다. 균형을 잡기 위해 AVL 트리는 아래 조건을 항상 만족시켜야 한다.

- 이진 탐색 트리여야 한다.
- \|왼쪽 서브 트리 높이\| - \|오른쪽 서브 트리 높이\| = {-1, 0, 1} 이여야 한다.

만약 조건이 만족되지 않으면 균형 잡히게 구조를 조정해야 한다.

![](pics/avltree.png)

[이미지 출처](https://en.wikipedia.org/wiki/AVL_tree)

avltree
<br>

## [Red-Black 트리](#Data-Structure)

|   삽입    |   검색    |   삭제    |
|----------|----------|----------|
| O(log n) | O(log n) | O(log n) |


레드-블랙 트리 또한 이진 탐색 트리의 불균형 구조를 균형있게 잡아주는 자료구조 이다. 그러나 AVL 트리처럼 높이의 차이를 구해서 균형을 잡는게 아니라 레드 노드와 블랙 노드를 사용해서 균형을 잡는다. 레드-블랙 트리의 조건은 다음과 갖다.

- 이진 탐색 트리여야 한다.
- 노드의 색은 레드 아니면 블랙 이여야 한다.
- 루트 노드는 항상 블랙이다.
- NULL 포인터들은 (NIL 노드) 블랙이다. 즉 자식이 없으면 그것은 NULL 포인터를 가리킨다.
- 노드가 **빨강**이면 자식들은 **블랙**이여야 한다.
- 노드부터 후손 NIL 노드까지의 블랙 노드의 수는 모두 같아야 한다.

![](pics/redblacktree.png)

[이미지 출처](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)


<br>

## [그래프 (Graph)](#Data-Structure)

그래프는 **G** 는 노드/정점 **V**ertex 와 간선 **E**dge 쌍으로 지어진 자료구조이다. 트리 구조 또한 cycle 이 없는 그래프 구조이다.

그래프는 방향성이 있는 그래프 **(Directed Graph)** 와 무방향 그래프 **(Undirected Graph)** 로 나눠질 수 있다. 그리고 그래프는 인접 행렬 **(Adjacency Matrix)** 와 인접 리스트 **(Adjacency List)** 로 구현할 수 있다.

![그래프](pics/graph.png)
