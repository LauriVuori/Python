/*This code tests NUCLEO-L152RE board transmitter UART communication by using
9600 BAUD and float print with sprintf
*/
/**
 * Pin config
 * PA5 PWM TIM2
 * PA6 PWM TIM3
 * PB6 PWM TIM4
 * 
 * 
 */

/**
 * @file main.c
 * @author Lauri Vuori
 * @brief VDF driver
 * @version 0.1
 * @date 2022-01-26
 * 
 * 
 */



/* Includes */
#include "include.h"
#include "nucleo152start.h"
#include "table.h"
/* Private typedef */
/* Private define  */
/**
 * @brief pwm / timer configurations
 */
#define TIM2_PRESCALER_VAL 1 		// 32 mHz / 1 = 32mHz
#define TIM3_PRESCALER_VAL 1 		// 32 mHz / 1 = 32mHz
#define TIM4_PRESCALER_VAL 1 		// 32 mHz / 1 = 32mHz
#define TIM2_ARR_REGISTER 2000		// 32 mHz / 2000 = 16 000 Hz
#define TIM3_ARR_REGISTER 2000		// 32 mHz / 2000 = 16 000 Hz
#define TIM4_ARR_REGISTER 2000		// 32 mHz / 2000 = 16 000 Hz
#define TIM2_DUTY_CYCLE 30
#define TIM3_DUTY_CYCLE 10
#define TIM4_DUTY_CYCLE 30

/* Private macro */
/* Private variables */
/* Private function prototypes */
/* Private functions */


// struct duty_cycles {
// 	uint16_t *tim2_pulse_width;
// 	uint16_t *tim3_pulse_width;
// 	uint16_t *tim4_pulse_width;
// };


void delay_Ms(int delay);
void init_PWM_TIM2(void);
void init_PWM_TIM3(void);
void init_PWM_TIM4(void);
void init_PWM_TIM9(void);
void init_GPIO_PA8(void);
void set_GPIO_PA8(uint8_t set_bit);
void debug_APB1_TIM2_freeze(void);
void debug_APB1_TIM2_unfreeze(void);

uint8_t tim2_counter = 0;
uint8_t tim3_counter = 0;
uint8_t tim4_counter = 0;
/**
**===========================================================================
**
**  Abstract: main program
**
**===========================================================================
*/

// struct duty_cycles duty_cycles_values;
int rand(void);
void init_board_button1(void);
int main(void) {
	/* Configure the system clock to 32 MHz and update SystemCoreClock */
	SetSysClock();
	SystemCoreClockUpdate();
	USART2_Init();
	init_PWM_TIM2();
	init_PWM_TIM3();
	init_PWM_TIM4();
	init_GPIO_PA8();
	init_board_button1();
	// debug_APB1_TIM2_unfreeze();
	debug_APB1_TIM2_freeze();

	uint8_t counter = 0;
	while (1) {
		if(~(GPIOC->IDR) & 0x2000){ 	//if PC13 is high state (button released)
			while(~(GPIOC->IDR) & 0x2000);
			delay_Ms(15);
			if (counter == 0) {
				TIM4->CCR1 = TIM4_DUTY_CYCLE - 1;
				TIM2->CCR1 = 1 - 1;
				TIM3->CCR1 = 1 - 1;
				counter++;

			} 
			else if (counter == 1) {
				TIM3->CCR1 = TIM3_DUTY_CYCLE - 1;
				TIM4->CCR1 = 1 - 1;
				TIM2->CCR1 = 1 - 1;
				counter++;

			}
			else if (counter == 2) {
				TIM2->CCR1 = TIM2_DUTY_CYCLE - 1;
				TIM4->CCR1 = 1 - 1;
				TIM3->CCR1 = 1 - 1;
				counter++;

			}
			else if (counter == 3) {
				TIM2->CCR1 = TIM2_DUTY_CYCLE - 1;
				TIM3->CCR1 = TIM3_DUTY_CYCLE - 1;
				TIM4->CCR1 = TIM4_DUTY_CYCLE - 1;
				counter++;

			}

			else {
				TIM2->CCR1 = 1 - 1; 
				TIM3->CCR1 = 1 - 1; 
				TIM4->CCR1 = 1 - 1; 
				counter = 0;
			}
		
		}
	}
	return 0;
}
void init_board_button1(void) {
    // B1 USER: the user button is connected to the I/O PC13 (pin 2) of the STM32 
    // microcontroller.
    // PORT C 19 bit
    RCC->AHBENR |= 0x4;
    // 00 input
    GPIOC->MODER |= (0 << 26) | (0 << 27);

}

int rand(void) {
	int seed = 123456789;
	seed = (2 * seed + TIM2->CNT) % 4;
	return seed;
}
void set_GPIO_PA8(uint8_t set_bit) {
	if (set_bit == 0) {
		GPIOA->ODR &= ~((1 << 8));
	}
	else if (set_bit == 1) {
		GPIOA->ODR |= (1 << 8);
	}
}

/**
 * @brief Init GPIO PA8
 * 
 * 
 */
void init_GPIO_PA8(void) {
	RCC->AHBENR |= 1; 					// Enable PORT A clock, does not matter if its already on
	GPIOA->MODER &= ~((1 << 17) | (1 << 16));		// Clear bits 16,17
	GPIOA->MODER |= (1 << 16);			// bits 16. output 01.
}
/**
 * @brief TIM2 interrupt
 * 
 * 
 */

void TIM2_IRQHandler(void) {
	TIM2->SR=0;			                //clear UIF
	GPIOA->ODR ^= (1 << 8);
	//TIM2->CCER = table[tim2_counter];
}
/**
 * @brief Unfreeze TIM2 while debugging, timer will run while pause
 * 
 * 
 */
void debug_APB1_TIM2_unfreeze(void) {
	DBGMCU->APB1FZ &= ~1;
}
/**
 * @brief TIM2 will freeze durign debugging pause
 * 
 * 
 */
void debug_APB1_TIM2_freeze(void) {
	// Debug MCU APB1 freeze register
	DBGMCU->APB1FZ |= 1;
}

//dont work
void init_PWM_TIM9(void) {
	// AHB peripheral clock enable register
	RCC->AHBENR |= 1;				// Enable GPIOA clock
	// GPIO alternate function low register (GPIOx_AFRL)
	// AF03
	GPIOA->AFR[0] |= ((1 << 29) | (1 << 28));  	// PA7 pin for TIM9
	// GPIO port mode register (GPIOx_MODER) (x = A..H)
	GPIOA->MODER &= ~((1<< 14) | (1 << 15));		// Clear bits
	GPIOA->MODER |= (1 << 15);		// Set bits


	//Setup TIM9
	// APB1 peripheral clock enable register
	RCC->APB2ENR |= (2 << 1); 		// Enable TIM9 clock
	// TIMx prescaler (TIMx_PSC)
	TIM9->PSC = 32000 - 1;			// divided by 16000
	// TIMx auto-reload register
	TIM9->ARR = 2000 - 1; 			// divided by 26667
	// TIMx counter (TIMx_CNT)
	TIM9->CNT = 0;
	// TIMx capture/compare mode register 1
	TIM9->CCMR1 = 0x0060; 			// PWM mode
	// TIMx capture/compare enable register (TIMx_CCER)
	TIM9->CCER = 1;					// Enable PWM Ch1
	// TIMx capture/compare register 1
	TIM9->CCR1 = 10 - 1; 			// Pulse width 1/3 of the period
	// TIMx control register 1
	TIM9->CR1 = 1;					// Enable Timer
}

/**
 * @brief 
 * 
 * 
 */

void init_PWM_TIM4(void) {
	// AHB peripheral clock enable register
	RCC->AHBENR |= (1 << 1);				// Enable GPIOB clock
	// GPIO alternate function low register (GPIOx_AFRL)
	GPIOB->AFR[0] |= (1 << 25);   			// PB6 pin for tim4
	// GPIO port mode register (GPIOx_MODER) (x = A..H)
	GPIOB->MODER &= ~((1<< 13) | (1 << 12));// Clear bits
	GPIOB->MODER |= (1 << 13);				// Set bits

	//Setup TIM4
	// APB1 peripheral clock enable register
	RCC->APB1ENR |= (2 << 1); 		// Enable TIM4 clock
	// TIMx prescaler (TIMx_PSC)
	TIM4->PSC = TIM4_PRESCALER_VAL - 1;			// divided by 16000
	// TIMx auto-reload register
	TIM4->ARR = TIM4_PRESCALER_VAL - 1; 			// divided by 26667
	// TIMx counter (TIMx_CNT)
	TIM4->CNT = 0;
	// TIMx capture/compare mode register 1
	TIM4->CCMR1 = 0x0060; 			// PWM mode
	// TIMx capture/compare enable register (TIMx_CCER)
	TIM4->CCER = 1;					// Enable PWM Ch1
	// TIMx capture/compare register 1
	TIM4->CCR1 = TIM4_DUTY_CYCLE - 1; 			// Pulse width 1/3 of the period
	// TIMx control register 1
	TIM4->CR1 = 1;					// Enable Timer
}

void init_PWM_TIM3(void) {
	// AHB peripheral clock enable register
	RCC->AHBENR |= 1;				// Enable GPIOA clock
	// GPIO alternate function low register (GPIOx_AFRL)
	GPIOA->AFR[0] |= (1 << 25); 	// PA6 pin for tim3


	// GPIO port mode register (GPIOx_MODER) (x = A..H)
	GPIOA->MODER &= ~((1<< 13) | (1 << 12));		// Clear bits
	GPIOA->MODER |= (1 << 13);		// Set bits

	//Setup TIM3
	// APB1 peripheral clock enable register
	RCC->APB1ENR |= (1 << 1); 		// Enable TIM3 clock
	// TIMx prescaler (TIMx_PSC)
	TIM3->PSC = TIM3_PRESCALER_VAL - 1;			// divided by 16000
	// TIMx auto-reload register
	TIM3->ARR = TIM3_ARR_REGISTER - 1; 			// divided by 26667
	// TIMx counter (TIMx_CNT)
	TIM3->CNT = 0;
	// TIMx capture/compare mode register 1
	TIM3->CCMR1 = 0x0060; 			// PWM mode
	// TIMx capture/compare enable register (TIMx_CCER)
	TIM3->CCER = 1;					// Enable PWM Ch1
	// TIMx capture/compare register 1
	TIM3->CCR1 = TIM3_DUTY_CYCLE - 1; 			// Pulse width 1/3 of the period
	// TIMx control register 1
	TIM3->CR1 = 1;					// Enable Timer
}
//Clock 32 000 000
//PSC 	16 000
//Arr 	200
//32 000 000 / 16 000 = 2000
// 2000 / 200 = 20Hz
//CCr1 100/200 = 50%
//CCr1 150/200 = 75%

// 32 000 000 / 2 = 16 000 000
// 16 000 000 / 1000 = 16000
void init_PWM_TIM2(void) {
	// AHB peripheral clock enable register
	RCC->AHBENR |= 1;				// Enable GPIOA clock
	// GPIO alternate function low register (GPIOx_AFRL)
	// GPIOA->AFR[0] |= 0x00100000; 	// PA5 pin for tim2
	GPIOA->AFR[0] |= (1 << 20);
	// GPIO port mode register (GPIOx_MODER) (x = A..H)
	GPIOA->MODER &= ~0x0000C00;		// Clear bits
	GPIOA->MODER |= (1 << 11);		// Set bits

	//Setup TIM2
	// APB1 peripheral clock enable register
	RCC->APB1ENR |= 1; 				// Enable TIM2 clock
	// TIMx prescaler (TIMx_PSC)
	TIM2->PSC = TIM2_PRESCALER_VAL - 1;				// divided by 16000
	// TIMx auto-reload register
	TIM2->ARR = 2000 - 1; 			// divided by 26667
	// TIMx counter (TIMx_CNT)
	TIM2->CNT = 0;
	// TIMx capture/compare mode register 1
	TIM2->CCMR1 = 0x0060; 			// PWM mode
	// TIMx capture/compare enable register (TIMx_CCER)
	TIM2->CCER = 1;					// Enable PWM Ch1
	// TIMx capture/compare register 1
	TIM2->CCR1 = TIM2_DUTY_CYCLE - 1; 			// Pulse width 1/3 of the period
	// TIMx control register 1
	TIM2->CR1 = 1;					// Enable Timer

	
	// TIM2->DIER |= (1 << 1);		            //enable UIE, interrupt enable -> falling edge
	// TIM2->DIER |= 1;		            //enable UIE, interrupt enable -> interrupt from ccr1 val
    // NVIC_EnableIRQ(TIM2_IRQn);
}

void delay_Ms(int delay) {
	int i=0;
	for(; delay>0;delay--){
		for(i=0;i<2460;i++); //measured with oscilloscope
	}
}
