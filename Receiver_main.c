// main.c (STM32 Receiver Side)
// Receives control signals from NRF24L01 and controls motors accordingly

#include "stm32f1xx_hal.h"
#include "nrf24.h"
#include "motor_control.h"

#define THRESHOLD 10

uint8_t rxData[2];

void SystemClock_Config(void);
void MX_GPIO_Init(void);
void MX_USART2_UART_Init(void);
void MX_SPI1_Init(void);

int main(void) {
    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_USART2_UART_Init();
    MX_SPI1_Init();

    NRF24_begin(GPIOA, GPIO_PIN_4, GPIO_PIN_3, hspi1);
    NRF24_setAutoAck(false);
    NRF24_setPayloadSize(2);
    NRF24_openReadingPipe(1, (uint8_t *)"TXADD");
    NRF24_startListening();

    motor_init();

    while (1) {
        if (NRF24_available()) {
            NRF24_read(rxData, 2);

            int joystick = rxData[0];
            int pot = rxData[1];

            if (joystick > 128 + THRESHOLD) {
                motor_forward(pot);
            } else if (joystick < 128 - THRESHOLD) {
                motor_backward(pot);
            } else {
                motor_stop();
            }
        }
    }
}

// Include clock config, GPIO, UART, and SPI init functions below or use STM32CubeMX generated code.

// Example motor_control.c:
// void motor_forward(int speed) { ... }
// void motor_backward(int speed) { ... }
// void motor_stop(void) { ... }
