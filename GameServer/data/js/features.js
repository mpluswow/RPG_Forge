// Example for interactivity
(function featuresScript() {
    document.addEventListener("DOMContentLoaded", () => {
        const featureItems = document.querySelectorAll(".feature-item");

        featureItems.forEach((item) => {
            item.addEventListener("click", () => {
                alert(`Feature: ${item.querySelector("h3").textContent}`);
            });
        });
    });
})();
