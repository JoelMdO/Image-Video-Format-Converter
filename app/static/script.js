document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".menu-toggle button");
  if (!buttons.length) return;

  buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      // remove active from all
      buttons.forEach((b) => b.classList.remove("active"));
      // add active to clicked
      btn.classList.add("active");
    });
  });
});
