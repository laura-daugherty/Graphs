from room import Room
from player import Player
from world import World
from util import Queue

import random
import copy
from ast import literal_eval

class Graph:
  def __init__(self, starting_room):
    self.graph = {}

  def travel(self):
    #init dir choice as ''
    dir_choice = ''
    #for dir in exits:
    for dir in player.current_room.get_exits():
      #if dir is a ?
      if self.graph[player.current_room.id][dir] == '?':
        # set dir_choice as direction of the ? to explore unexplored room
        dir_choice = dir
    #if dead end
    if dir_choice == '':
      #BFS to find a new unexplored room from current room
      new_path = self.bfs(player.current_room)
      # for direction in exits
      for direction in player.current_room.get_exits():
        # if current room direction points to the new unexplored room
        if self.graph[player.current_room.id][direction] == str(new_path[1].id):
          #dir_choice is that direction
          dir_choice = direction
    # if goes through all and still ''
    if dir_choice == '':
      return
    #set prev room to current room
    previous_room = player.current_room.id
    # travel in dir_choice
    player.travel(dir_choice)
    #set new room to new current room
    new_room = player.current_room.id

    # Update room maps
    self.map_room(previous_room, str(new_room), dir_choice)
    self.fill_current_room()
    self.map_room(new_room, str(previous_room), self.opposite_direction(dir_choice))
    #fill in traversal path
    self.fill_traversal_path(dir_choice)
    return dir_choice

  def fill_current_room(self):
    current_room = player.current_room.id

    if current_room in self.graph:
      return
    #if current room not in self.graph
    #set current room graph to empty dict
    self.graph[current_room] = {}
    # set each direction to be a ?
    for exit in player.current_room.get_exits():
      self.graph[current_room][exit] = "?"

  def map_room(self, prev, next, dir):
    #set prev room dir to next room
    self.graph[prev][dir] = next

  def opposite_direction(self, direction):
    if direction == "n":
      return "s"
    elif direction == "s":
      return "n"
    elif direction == "e":
      return "w"
    elif direction == "w":
      return "e"
    
  def fill_traversal_path(self, dir_choice):
    #add to traversal path
    traversal_path.append(dir_choice)

  def bfs(self, starting_room):
    """
    Return a list containing the shortest path from
    starting_room to destination_room in
    breath-first order.
    """
    # Create a queue
    q = Queue()
    # Enqueue A PATH TO the starting room
    q.enqueue([starting_room])
    # Create a set to store visited rooms
    visited = set()
    # While the queue is not empty...
    while q.size() > 0:
      # Dequeue the first PATH
      path = q.dequeue()
      # GRAB THE ROOM FROM THE END OF THE PATH
      last_room = path[-1]
      # Check if it's been visited
      if last_room not in visited:
      # If it hasn't been visited...
        visited.add(last_room)
        # Mark it as visited
        # CHECK IF IT'S THE TARGET
        if last_room.id not in self.graph:
          return path
        for exit in self.graph[last_room.id]:
          if exit == '?':
            return path
            # IF SO, RETURN THE PATH]
        else:
          # Enqueue A PATH TO all it's neighbors
          # MAKE A COPY OF THE PATH
          # ENQUEUE THE COPY
          neighbors = []
          neighbors.append(last_room.get_room_in_direction('n'))
          neighbors.append(last_room.get_room_in_direction('s'))
          neighbors.append(last_room.get_room_in_direction('e'))
          neighbors.append(last_room.get_room_in_direction('w'))
          #getting rid of any "None"
          neighbors = [neighbor for neighbor in neighbors if neighbor]

          for neighbor in neighbors:
            path_two = path.copy()
            path_two.append(neighbor)
            q.enqueue(path_two)
        

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



graph = Graph(world.starting_room)
graph.fill_current_room()
while len(graph.graph) < len(world.rooms):
  graph.travel()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
