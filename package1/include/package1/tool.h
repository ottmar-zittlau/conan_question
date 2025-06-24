#include <magic_enum/magic_enum.hpp>

template <typename T>
std::string_view enumToString(const T &p)
{
    return magic_enum::enum_name(p);
}