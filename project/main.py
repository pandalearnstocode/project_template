from sub1.helper import helper_foo
from sub2.utils import utils_foo


def this_is_main():
    print(helper_foo())
    print(utils_foo())
    return True


if __name__ == "__main__":
    this_is_main()
