#include <iostream>
#include <string>
#include <typeinfo>

int main() {
    int integer;
    double drob;
    std::string text;

    std::cout << "Введите целое число: ";
    std::cin >> integer;

    std::cout << "Введите дробное число: ";
    std::cin >> drob;

    std::cin.ignore();

    std::cout << "Введите строку: ";
    std::getline(std::cin, text);

    std::cout << "Значение: " << integer << ", тип: "
        << typeid(integer).name() << std::endl;
    std::cout << "Значение: " << drob << ", тип: "
        << typeid(drob).name() << std::endl;
    std::cout << "Значение: " << text << ", тип: "
        << typeid(text).name() << std::endl;

    return 0;
    }