#include "temp_controller.h"

void controller_init(controller_t* c, float low, float high) {
    c->threshold_low = low;
    c->threshold_high = high;
    c->mode = MODE_IDLE;
    c->last_temp = 0.0f;
}

mode_t controller_update(controller_t* c, float temperature) {
    c->last_temp = temperature;
    if (temperature > c->threshold_high) {
        c->mode = MODE_COOLING;
    } else if (temperature < c->threshold_low) {
        c->mode = MODE_HEATING;
    } else {
        c->mode = MODE_IDLE;
    }
    return c->mode;
}

const char* controller_mode_str(mode_t m) {
    switch (m) {
        case MODE_HEATING: return "HEATING";
        case MODE_COOLING: return "COOLING";
        case MODE_IDLE:
        default: return "IDLE";
    }
}
