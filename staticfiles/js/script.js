// ======================================
// WHO CARES PHOTOGRAPHY
// Main JavaScript File
// ======================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Who Cares Photography Loaded Successfully");

    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                e.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

});


// ======================================
// Future Features
// ======================================

// Image Lightbox
// Gallery Filter
// Counter Animation
// Testimonials Slider
// Mobile Navigation
// Booking Validation
// Contact Form Validation
// Payment Integration