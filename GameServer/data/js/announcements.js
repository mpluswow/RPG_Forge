document.addEventListener("DOMContentLoaded", () => {
    const announcements = [
        "Welcome to DreamerZz! We’re hiring contributors for DreamerZz projects! New features are coming soon, stay tuned!",
        "Join our Discord for the latest updates. Check out our GitHub repository for updates.",
        "New features are coming soon, stay tuned! Join our Discord for the latest updates.",
        "Check out our GitHub repository for updates.",
        "We’re hiring contributors for DreamerZz projects!",
    ];

    const announcementText = document.querySelector(".announcement-text");

    if (!announcementText) {
        console.error("Announcement text element not found.");
        return;
    }

    let currentIndex = 0;

    const displayAnnouncement = () => {
        // Set the current announcement text
        announcementText.textContent = announcements[currentIndex];

        // Slide in from the right
        announcementText.style.transform = "translateY(-50%) translateX(0)";

        // After 4 seconds, slide out to the left
        setTimeout(() => {
            announcementText.style.transform = "translateY(-50%) translateX(-100%)";
        }, 4000);

        // Move to the next announcement
        currentIndex = (currentIndex + 1) % announcements.length;
    };

    // Start the announcement cycle
    setInterval(displayAnnouncement, 5000);
    displayAnnouncement(); // Show the first announcement immediately
});
