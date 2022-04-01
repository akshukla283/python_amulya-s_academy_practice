# Now we will use "if __name__ == '__main__' " to avoid output of imported module file
from unicodedata import name

from pip import main
import multiply

# in vscode we wil use name == main at the place of if __name__ == '__main__'
if name==main:    
    print(multiply.mul(2.3,4.2))
    print(__name__)
