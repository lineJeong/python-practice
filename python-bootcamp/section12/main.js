let enemies = 1;

function increase_enemies() {
  enemies = 2;
  console.log(`enemies inside function: ${enemies}`); // 2
}

increase_enemies();
console.log(`enemies out function: ${enemies}`); // 2
