#include <package1/tool.h>
#include <iostream>

template <typename T>
void printEnum(const T &p)
{
    std::cout << enumToString(p) << std::endl;
}