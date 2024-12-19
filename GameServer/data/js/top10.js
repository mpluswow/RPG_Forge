// Script for dynamically populating Top 10 lists with a typing effect
(function top10Script() {
    document.addEventListener("DOMContentLoaded", () => {
        console.log("Top 10 script is running...");

        const contributorsList = document.getElementById("contributors-list");
        const playersList = document.getElementById("players-list");

        if (!contributorsList || !playersList) {
            console.error("List elements not found in the DOM.");
            return;
        }

        // Example data (replace with actual data as needed)
        const topContributors = [
            "Alice - 150 contributions",
            "Bob - 120 contributions",
            "Charlie - 110 contributions",
            "Dave - 100 contributions",
            "Eve - 95 contributions",
            "Frank - 90 contributions",
            "Grace - 85 contributions",
            "Heidi - 80 contributions",
            "Ivan - 75 contributions",
            "Judy - 70 contributions",
        ];

        const topPlayers = [
            "Player1 - 2000 points",
            "Player2 - 1800 points",
            "Player3 - 1700 points",
            "Player4 - 1600 points",
            "Player5 - 1500 points",
            "Player6 - 1400 points",
            "Player7 - 1300 points",
            "Player8 - 1200 points",
            "Player9 - 1100 points",
            "Player10 - 1000 points",
        ];

        // Function to add text with a typing effect
        function typeText(element, text, delay = 50) {
            let index = 0;
            function type() {
                if (index < text.length) {
                    element.textContent += text.charAt(index);
                    index++;
                    setTimeout(type, delay);
                }
            }
            type();
        }

        // Function to populate a list with static place text and typing effect for names
        function populateListWithPlaces(listElement, items, label = "Top") {
            listElement.innerHTML = ""; // Clear any existing items
            items.forEach((item, idx) => {
                const li = document.createElement("li");
                const placeText = `${label} ${idx + 1}: `;
                li.textContent = placeText; // Add the place text first
                listElement.appendChild(li);
                setTimeout(() => typeText(li, item, 50), placeText.length * 50); // Delay typing of the name
            });
        }

        // Function to handle the visibility of the list
        function handleVisibility(entries, observer, listElement, data) {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    // Populate the list when it becomes visible
                    const alreadyPopulated = listElement.getAttribute("data-typed");
                    if (!alreadyPopulated) {
                        populateListWithPlaces(listElement, data);
                        listElement.setAttribute("data-typed", "true"); // Mark as typed
                    }
                }
            });
        }

        // Create an Intersection Observer for each list
        const observerOptions = {
            root: null, // Use the viewport as the root
            rootMargin: "0px",
            threshold: 0.1, // Trigger when 10% of the element is visible
        };

        const contributorsObserver = new IntersectionObserver((entries, observer) => {
            handleVisibility(entries, observer, contributorsList, topContributors);
        }, observerOptions);

        const playersObserver = new IntersectionObserver((entries, observer) => {
            handleVisibility(entries, observer, playersList, topPlayers);
        }, observerOptions);

        // Observe the lists
        contributorsObserver.observe(contributorsList);
        playersObserver.observe(playersList);

        console.log("Intersection Observers initialized.");
    });
})();
