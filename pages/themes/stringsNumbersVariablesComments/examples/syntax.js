var numbers = [1, 2, 3, 4],
    total = 0,
    product = 1;

for (i = 0; i < numbers.length; i += 1) {
    total += numbers[i];
    product *= numbers[i];
}
console.log(total, product)