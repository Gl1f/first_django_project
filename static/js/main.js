console.log("main.js подключился ✅");

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("ctaOrders");
  if (btn) {
    btn.addEventListener("click", () => {
      console.log("Клик по кнопке 'Перейти к заявкам' ✅");
    });
  }
});
