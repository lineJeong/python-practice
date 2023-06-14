let enemies = 1;

function increase_enemies() {
  enemies = 2;
  console.log(`enemies inside function: ${enemies}`); // 2
}

increase_enemies();
console.log(`enemies out function: ${enemies}`); // 2

if (3 > 2) {
  const aVariable = 10;
  console.log(`a_variable : ${aVariable}`);
}

game_level = 3;
enemies = ["Skeleton", "Zombie", "Alien"];
if (game_level < 5) {
  var new_enemy = enemies[0]; // var면 블록스코프 X, let, const면 블록스코프 O
}

console.log(new_enemy);
