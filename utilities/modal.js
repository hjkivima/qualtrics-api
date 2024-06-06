const modal = document.querySelector(".modal");
const linkToModal = document.querySelector(".link-to-modal");
const closeModalButton = document.querySelector(".close-modal-button");

linkToModal.addEventListener("click", () => {
  Qualtrics.SurveyEngine.setEmbeddedData("modalHasBeenClicked_instructions", 1);
  modal.style.display = "block";
  window.scrollTo(0, 0);
});

closeModalButton.addEventListener("click", () => {
  window.scrollTo(0, 0);
  modal.style.display = "none";
});
