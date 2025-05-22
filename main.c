// main.c for STM32 transmitter side (joystick + potentiometer -> NRF24L01)

#include "stm32f1xx_hal.h"
#include "nrf24.h"
#include <string.h>

ADC_HandleTypeDef hadc1;
SPI_HandleTypeDef hspi1;

uint16_t joystick_x = 0;
uint16_t joystick_y = 0;
uint16_t potentiometer = 0;

uint8_t tx_payload[6];

void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_ADC1_Init(void);
static void MX_SPI1_Init(void);

void read_inputs(void) {
    HAL_ADC_Start(&hadc1);
    HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
    joystick_x = HAL_ADC_GetValue(&hadc1);

    HAL_ADC_Start(&hadc1);
    HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
    joystick_y = HAL_ADC_GetValue(&hadc1);

    HAL_ADC_Start(&hadc1);
    HAL_ADC_PollForConversion(&hadc1, HAL_MAX_DELAY);
    potentiometer = HAL_ADC_GetValue(&hadc1);
}

void package_and_send(void) {
    tx_payload[0] = joystick_x >> 8;
    tx_payload[1] = joystick_x & 0xFF;
    tx_payload[2] = joystick_y >> 8;
    tx_payload[3] = joystick_y & 0xFF;
    tx_payload[4] = potentiometer >> 8;
    tx_payload[5] = potentiometer & 0xFF;

    nrf24_send(tx_payload);
}

int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_ADC1_Init();
    MX_SPI1_Init();

    nrf24_init(&hspi1);
    nrf24_configure_tx_mode();

    while (1) {
        read_inputs();
        package_and_send();
        HAL_Delay(100); // send every 100 ms
    }
}

// Peripheral initialization functions go below (MX_GPIO_Init, MX_ADC1_Init, MX_SPI1_Init)
// Add your CubeMX generated code or HAL code here.
