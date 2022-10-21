function solution(numbers) {
    const avr = numbers.reduce((ans, number) => ans + number, 0) / numbers.length
    return avr;
}