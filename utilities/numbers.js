const numbers = document.querySelectorAll(".numbers li");
numbers.forEach(li => {
  const number = Number(li.textContent);

  li.textContent = li.textContent.trim()[[percent_suffix]];

  if (number % 20 !== 0) {
    li.classList.add("hide-for-mobile");
  }
});
