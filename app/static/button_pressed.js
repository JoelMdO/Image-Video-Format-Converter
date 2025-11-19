document.addEventListener("DOMContentLoaded", () => {
  const convertButton = document.querySelector(".button-convert");
  const faviconButton = document.querySelector(".button-favicon");

  if (!convertButton || !faviconButton) {
    return;
  }

  const setActiveButton = (nextActive) => {
    [convertButton, faviconButton].forEach((button) => {
      button.classList.toggle("active", button === nextActive);
    });
  };

  // Sync initial state to markup (convert is active by default in the template).
  const defaultActive = convertButton.classList.contains("active")
    ? convertButton
    : faviconButton;
  setActiveButton(defaultActive);

  convertButton.addEventListener("click", () => setActiveButton(convertButton));
  faviconButton.addEventListener("click", () => setActiveButton(faviconButton));
});
