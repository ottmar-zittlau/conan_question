#include <package2/tool.h>

enum class TestEnum
{
    FOO_2,
    BAR_2
};

int main()
{
    TestEnum p{TestEnum::BAR_2};
    printEnum(p);
}