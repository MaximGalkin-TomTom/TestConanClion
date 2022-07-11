#include <boost/any.hpp>
#include <iostream>

void print(boost::any value) {
    if (value.type() == typeid(int))
        std::cout << "value is: " << boost::any_cast<int>(value) << std::endl;
    else
        std::cout << "value is: " << boost::any_cast<std::string&>(value) << std::endl;
}

int main() {
    print(std::string("This is a string"));
    print(42);
}