#include <package1/tool.h>
#include <iostream>

enum class TestEnum
{
    FOO,
    BAR
};

int main()
{
    TestEnum p{TestEnum::BAR};
    std::cout << enumToString(p) << std::endl;
}