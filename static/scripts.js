document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav a, .cta-btn');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 60,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add animation to feature cards on scroll
    const featureCards = document.querySelectorAll('.feature-card');
    
    function checkScroll() {
        featureCards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top;
            const triggerBottom = window.innerHeight * 0.8;
            
            if (cardTop < triggerBottom) {
                card.classList.add('show');
            }
        });
    }

    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Check on initial load
});

/*javascript for build resume start */
document.addEventListener('DOMContentLoaded', function() {
    const addMoreButtons = document.querySelectorAll('.build-add-more');

    addMoreButtons.forEach(button => {
        button.addEventListener('click', function() {
            const section = this.closest('.build-section');
            const inputs = section.querySelectorAll('input, textarea');
            let allFilled = true;

            // Check if all inputs in the current section are filled
            inputs.forEach(input => {
                if (!input.value) {
                    allFilled = false;
                }
            });

            if (allFilled) {
                // Clone the current section
                const newSection = section.cloneNode(true);

                // Clear all input fields in the new section
                const newInputs = newSection.querySelectorAll('input, textarea');
                newInputs.forEach(input => {
                    input.value = '';
                });

                // Insert the new section after the current section
                section.parentNode.insertBefore(newSection, section.nextSibling);

                // Add event listener to the new "Add More" button
                newSection.querySelector('.build-add-more').addEventListener('click', function() {
                    const newSectionInputs = newSection.querySelectorAll('input, textarea');
                    let newSectionAllFilled = true;

                    // Check if all inputs in the new section are filled
                    newSectionInputs.forEach(input => {
                        if (!input.value) {
                            newSectionAllFilled = false;
                        }
                    });

                    if (newSectionAllFilled) {
                        const anotherNewSection = newSection.cloneNode(true);
                        anotherNewSection.querySelectorAll('input, textarea').forEach(input => input.value = '');
                        newSection.parentNode.insertBefore(anotherNewSection, newSection.nextSibling);
                    } else {
                        alert('Please fill out all fields before adding more.');
                    }
                });
            } else {
                alert('Please fill out all fields before adding more.');
            }
        });
    });
});

/*javascript for build resume end */


/*javascript for build resume start */

document.addEventListener('DOMContentLoaded', function() {
    const uploadBtn = document.getElementById('upload-btn');
    const jobDescription = document.getElementById('job-description');
    const scoreValue = document.getElementById('score-value');

    uploadBtn.addEventListener('click', function() {
        if (jobDescription.value.trim() !== '') {
            // Simulating file upload and scoring process
            setTimeout(() => {
                const randomScore = Math.floor(Math.random() * 31) + 70; // Random score between 70 and 100
                scoreValue.textContent = randomScore;
            }, 1500); // Simulating a delay for processing
        } else {
            alert('Please enter a job description before uploading your resume.');
        }
    });
});
/*javascript for build resume end */