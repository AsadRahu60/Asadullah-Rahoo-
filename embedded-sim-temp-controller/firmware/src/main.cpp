#include <iostream>
#include <string>
#include <sstream>
#include "temp_controller.h"

int main() {
    controller_t ctrl;
    controller_init(&ctrl, 18.0f, 24.0f);

    std::string line;
    std::cout << "READY\n" << std::flush;
    while (std::getline(std::cin, line)) {
        if (line.rfind("READ ", 0) == 0) {
            std::istringstream iss(line.substr(5));
            float t;
            if (iss >> t) {
                mode_t m = controller_update(&ctrl, t);
                std::cout << "TEMP " << t << " MODE " << controller_mode_str(m) << "\n" << std::flush;
            } else {
                std::cout << "ERR BAD_INPUT\n" << std::flush;
            }
        } else if (line == "STATUS") {
            std::cout << "STATUS " << controller_mode_str(ctrl.mode) << " LAST " << ctrl.last_temp << "\n" << std::flush;
        } else if (line == "EXIT") {
            std::cout << "BYE\n" << std::flush;
            break;
        } else {
            std::cout << "ERR UNKNOWN_CMD\n" << std::flush;
        }
    }
    return 0;
}
