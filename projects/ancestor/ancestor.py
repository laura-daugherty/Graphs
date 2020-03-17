class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
            # Mark it as visited
            # Print
            # Call DFT_Recursive on each child
        # visited = set()
        if visited == None:
            visted = set()
        if starting_vertex in visited:
            return
        else:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            print("path", path)
            # GRAB THE LAST VERTEX FROM THE PATH
            last = path[-1]
            # CHECK IF IT'S THE TARGET
            if last == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            elif last not in visited:
            # If it has not been visited...
                # Mark it as visited
                visited.add(last)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    pathTwo = path.copy()
                    pathTwo.append(neighbor)
                    q.enqueue(pathTwo)
                    # (Make a copy of the path before adding)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue
        s = Stack()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue, the first PATH
            path = s.pop()
            print("path", path)
            # GRAB THE LAST VERTEX FROM THE PATH
            last = path[-1]
            # CHECK IF IT'S THE TARGET
            if last == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            elif last not in visited:
            # If it has not been visited...
                # Mark it as visited
                visited.add(last)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(last):
                    pathTwo = path.copy()
                    pathTwo.append(neighbor)
                    s.push(pathTwo)
                    # (Make a copy of the path before adding)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
            
        if destination_vertex == starting_vertex:
            print("path", path)
            path.append(destination_vertex)
            return path
        else:
            visited.add(starting_vertex)
            path2 = path.copy()
            path2.append(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    temp = self.dfs_recursive(neighbor, destination_vertex, visited, path2)
                    if temp is not None:
                        return temp
        return None

    def earliest_ancestor_recursive(self, starting_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        neighbors = set(self.get_neighbors(starting_vertex))
        #if all of my neighbors are in visited
        if neighbors.issubset(visited):
            print("path", path)
            path.append(starting_vertex)
            return path
        else:
            visited.add(starting_vertex)
            path2 = path.copy()
            path2.append(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                longest = 0
                if neighbor not in visited:
                    temp = self.dfs_recursive(neighbor, visited, path2)
                    

        return None

# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input individual. 
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
# If the input individual has no parents, the function should return -1.

#TRANSLATE INTO GRAPH TERMINOLOGY
#DFT
#directed, acyclic, sparse graph
#nodes are ID's
#edges are relationships from parent to child

#BUILD YOUR GRAPH


#TRAVERSE YOUR GRAPH
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node, path=None):
  #BUILD GRAPH
  
  #TRAVERSE GRAPH

  # Create an empty stack
  # Push the starting vertex_id to the stack
  # Create an empty set to store visited nodes
  # visited = set()
  # While the stack is not empty..

      # Pop the first vertex

      # Check if it's been visited
      # If it has not been visited...
      # pathCopy = path.copy()

      # if v not in visited:
          # Mark it as visited
          # pathPop = pathPop + [v]
      # print("pathCopy", pathCopy)
      # print(v)
      # visited.add(v)
      # print("visited", visited)
          # Then push all neighbors to the top of the stack

        
        


