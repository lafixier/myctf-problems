#include <iostream>
#include <string>

std::string a();

int main()
{
    std::string flag_1 = "Flag{chm0d_c0mmand";
    std::string flag_2 = "_892743589734583829745";
    std::cout << flag_1;
    std::cout << flag_2;
    std::cout << a() + "43564356456}" << std::endl;
    return 0;
}

std::string a()
{
    int x = 3829;
    int y = 8932;
    std::string f = std::to_string(x) + std::to_string(x) + std::to_string(y) + "865789789789";
    return f;
}
