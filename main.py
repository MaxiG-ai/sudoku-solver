import numpy as np
from dataclasses import dataclass

def check_numbers(ls: np.array):
    """Checks if the given array contains the numbers between 1 and 9 exactely once and is of length 9. Ensures the 

    Args:
        ls (np.array): array with numbers

    Returns:
        bool: true or false
    """
    if not isinstance(ls, np.ndarray):
        raise TypeError("Input must be a numpy array")
    
    if len(ls) != 9:
        return False
    elif not set(ls) == set(range(1, 10)):
        return False
    else: 
        return True

@dataclass
class Sudoku:
    name: str
    field: np.array
    
    def check_finished(self):
        """
        A sudoku is finished if
        - Each row contains all the numbers once
        - Each column contains all the numbers once
        - Each sub-quarter contains all the numbers once
        """
        # iterate over rows
        for row in self.field:
            if check_numbers(row):
                return True
            else:
                return False
        
        # iterate over columns
        for col in zip(*field):
            if check_numbers(col):
                return True
            else:
                return False
        return True
    
        # iterate over small quarters
        # Split the field into 3x3 blocks
        blocks = field.reshape(3, 3, 3, 3).transpose(0, 2, 1, 3).reshape(9, 9)

        # Flatten the blocks into a 1D array
        flat_blocks = blocks.flatten()

        # Print the blocks
        for block in flat_blocks:
            if check_numbers(row):
                return True
            else:
                return False

if __name__ == "__main__":
    print("Welcome to Sudoku Solver by Maxi!")
    
    s1 = Sudoku(name="My First Sudoku", field=np.zeros((9,9), dtype = int))
    
    print(s1.check_finished())
    
    # print(s1)