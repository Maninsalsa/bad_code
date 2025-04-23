#include <iostream>

int main() {
  
  int dog_age = 1;

  // Solving for human years

  // The first two years count as 21 human years
  int early_years = 21;

  // Each following year counts as 4 human years
  int later_years = (dog_age - 2) * 4;

  // Add them together for the human years conversion
  int human_years = early_years + later_years;
  
  if (dog_age < 2) {
      std::cout << "My name is Juneau! Ruff ruff, I'm a wee pup!\n";
  } else {
      std::cout << "My name is Juneau! Ruff ruff, I am " << human_years << " years old in human years!\n";
  }
  
  /*
  switch (dog_age) {
  case 0:
  case 1:
    std::cout << "My name is Juneau! Ruff ruff, I'm a wee pup!\n";
    break;
  default:
    std::cout << "My name is Juneau! Ruff ruff, I am " << human_years << " years old in human years!\n";
  }
  */

  return 0;
}
