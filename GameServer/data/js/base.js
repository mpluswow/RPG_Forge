// Base JavaScript for DreamerZz

(function baseScript() {
    document.addEventListener('DOMContentLoaded', () => {
        // Mobile menu toggle for navbar
        const navbarToggle = document.querySelector('.navbar-toggle');
        const navbarMenu = document.querySelector('.navbar ul');

        if (navbarToggle) {
            navbarToggle.addEventListener('click', () => {
                navbarMenu.classList.toggle('active');

                // Update aria-expanded for accessibility
                const isExpanded = navbarMenu.classList.contains('active');
                navbarToggle.setAttribute('aria-expanded', isExpanded);
            });
        }

        // Footer social links hover animation
        const socialLinks = document.querySelectorAll('.footer .social-links a');
        socialLinks.forEach(link => {
            link.addEventListener('mouseenter', () => {
                link.style.transform = 'scale(1.2)';
                link.style.transition = 'transform 0.2s ease';
            });

            link.addEventListener('mouseleave', () => {
                link.style.transform = 'scale(1)';
            });
        });
    });
})();
