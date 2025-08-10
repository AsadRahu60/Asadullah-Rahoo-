#include <unity.h>
#include "temp_controller.h"

void setUp(void) {}
void tearDown(void) {}

void test_idle_between_thresholds(void) {
    controller_t c; controller_init(&c, 18.0f, 24.0f);
    TEST_ASSERT_EQUAL(MODE_IDLE, controller_update(&c, 21.0f));
}

void test_heating_below_low(void) {
    controller_t c; controller_init(&c, 18.0f, 24.0f);
    TEST_ASSERT_EQUAL(MODE_HEATING, controller_update(&c, 10.0f));
}

void test_cooling_above_high(void) {
    controller_t c; controller_init(&c, 18.0f, 24.0f);
    TEST_ASSERT_EQUAL(MODE_COOLING, controller_update(&c, 30.0f));
}

void test_boundaries(void) {
    controller_t c; controller_init(&c, 18.0f, 24.0f);
    TEST_ASSERT_EQUAL(MODE_IDLE, controller_update(&c, 18.0f));
    TEST_ASSERT_EQUAL(MODE_IDLE, controller_update(&c, 24.0f));
}

int main(int argc, char **argv) {
    UNITY_BEGIN();
    RUN_TEST(test_idle_between_thresholds);
    RUN_TEST(test_heating_below_low);
    RUN_TEST(test_cooling_above_high);
    RUN_TEST(test_boundaries);
    return UNITY_END();
}
