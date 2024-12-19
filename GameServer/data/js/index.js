// Slider functionality
(function sliderScript() {
    document.addEventListener('DOMContentLoaded', () => {
        const slides = document.querySelectorAll('.carousel-item');
        const dots = document.querySelectorAll('.carousel-indicators button');
        const leftArrow = document.querySelector('.carousel-control-prev');
        const rightArrow = document.querySelector('.carousel-control-next');

        let currentIndex = 0;
        let autoplayInterval = null;
        const autoplayDelay = 8000;

        const updateSlides = (index) => {
            slides.forEach((slide, i) => {
                const video = slide.querySelector('video');
                if (i === index) {
                    slide.classList.add('active');
                    if (video) video.play();
                } else {
                    slide.classList.remove('active');
                    if (video) {
                        video.pause();
                        video.currentTime = 0;
                    }
                }
            });

            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });

            currentIndex = index;
        };

        const nextSlide = () => {
            updateSlides((currentIndex + 1) % slides.length);
        };

        const prevSlide = () => {
            updateSlides((currentIndex - 1 + slides.length) % slides.length);
        };

        const startAutoplay = () => {
            autoplayInterval = setInterval(nextSlide, autoplayDelay);
        };

        const stopAutoplay = () => {
            clearInterval(autoplayInterval);
        };

        rightArrow.addEventListener('click', () => {
            nextSlide();
            stopAutoplay();
            startAutoplay();
        });

        leftArrow.addEventListener('click', () => {
            prevSlide();
            stopAutoplay();
            startAutoplay();
        });

        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => {
                updateSlides(i);
                stopAutoplay();
                startAutoplay();
            });
        });

        startAutoplay();
        updateSlides(currentIndex);
    });
})();