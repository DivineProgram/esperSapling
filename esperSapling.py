
class BranchError(Exception):
  def __init__(self,*args: object):
    self.message = ' '.join(args)
    super().__init__(self.message)



def AZ(arg: str=''):
  for letter in arg:
    if ord(letter) < ord('A') or ord(letter) > ord('Z'):
      raise IndexError('Argument not between A and Z')



class tree():
  
  def __init__(self, arrays=[]):
    if len(arrays) > 26:
      raise ValueError('Too many array branches in tree')
    self.branches = arrays
    self.nodeCount = 1

  
  def __repr__(self):
    return ' '.join(map(str, self.keys()))
    
  
  def __getitem__(self, index: str):
    AZ(index)
      # Indexing Tree
    pointer = 0
    for path in index:
      path = ord(path) - ord('A')
      if path >= len(self.branches) or pointer >= len(self.branches[path]) or self.branches[path][pointer] is None:
        raise IndexError('Branch route does not exist')
        # Raise error is anything is out of range of if pointer leads to None
      pointer = self.branches[path][pointer]
    return pointer

  
  
  def __contains__(self, key: int):
      # See if an index exists in tree
    return key in self

  

  def junc(self, index: str=''):
    AZ(index)
      # Get specific junction at given index
    # Go to index
    pointer = self[index]
    paths = {}
    # Check every branch to see what the index branches off into
    for branch_index in range(len(self.branches)):
      branch = self.branches[branch_index]
      try: leaf = branch[pointer]
      except: leaf = None
      else:
        if leaf is not None:
          paths[chr(branch_index+ord('A'))] = leaf
    return paths


  
  def keys(self):
      # Get an array of all ids in tree
    all = []
    for branch in self.branches:
      for leaf in branch:
        if leaf is not None:
          all.append(leaf)
    return all

  
  
  def append(self, index: str='', key: int=None):
    AZ(index)
      # Appending a new node
    if type(key) != int or key <= 0:
      raise ValueError('Key must be positive integer')
    # Go to one-before index
    pointer = self[index[:-1]]
    branch_index = ord(index[-1]) - ord('A')
    # Create branch if doesn't exist
    while branch_index >= len(self.branches):
      self.branches.append([])
    while pointer >= len(self.branches[branch_index]):
      self.branches[branch_index].append(None)
    # Raise error if index preoccupied
    if self.branches[branch_index][pointer] is not None:
      raise ValueError('Given index already occupied')
    # Set new node
    self.branches[branch_index][pointer] = key
