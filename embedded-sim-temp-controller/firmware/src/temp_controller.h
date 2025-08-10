#ifndef TEMP_CONTROLLER_H
#define TEMP_CONTROLLER_H

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    MODE_IDLE = 0,
    MODE_HEATING = 1,
    MODE_COOLING = 2
} mode_t;

typedef struct {
    float threshold_low;
    float threshold_high;
    mode_t mode;
    float last_temp;
} controller_t;

void controller_init(controller_t* c, float low, float high);
mode_t controller_update(controller_t* c, float temperature);
const char* controller_mode_str(mode_t m);

#ifdef __cplusplus
}
#endif

#endif // TEMP_CONTROLLER_H
