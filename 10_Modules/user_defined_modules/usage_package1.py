import package.module1 as m1 # alias import
from package import module2 # selective import
import package.module3 # subpackage import


if __name__ == "__main__":
    m1.hello_world()
    module2.hello_world()
    
    # module3.hello_world()
    package.module3.hello_world()