// user_onboarding.js

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the active class from all tabs
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the clicked tab and add active class to the button
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Function to duplicate a section's form group dynamically without affecting the tabs
function addNewSection(sectionId) {
    // Get the sections container that holds all section fields
    const sectionsContainer = document.querySelector(`#${sectionId} .sections-container`);

    if (sectionsContainer) {
        // Clone the first section inside the container (as a template)
        const newSection = sectionsContainer.firstElementChild.cloneNode(true);

        // Clear all input values in the cloned section
        newSection.querySelectorAll('input, textarea').forEach(input => input.value = '');

        // Add an event listener to the delete button if not already present in the cloned section
        const deleteButton = newSection.querySelector('.delete-section');
        if (deleteButton) {
            deleteButton.onclick = function() {
                removeSection(deleteButton);
            };
        }

        // Append the cloned section inside the sections container
        sectionsContainer.appendChild(newSection);

        // Move the 'Add More' button to the end of the container (if not already there)
        const addButton = sectionsContainer.parentNode.querySelector('button[onclick*="addNewSection"]');
        if (addButton) {
            sectionsContainer.appendChild(addButton);
        }
    }
}

// Function to remove a specific section
function removeSection(button) {
    const sectionsContainer = button.closest('.sections-container');
    const sectionToRemove = button.closest('.section-fields');

    // Check if there is more than one section remaining before deleting
    if (sectionsContainer.querySelectorAll('.section-fields').length > 1) {
        sectionToRemove.remove();
    } else {
        alert("At least one section must remain.");
    }
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("Profile").style.display = "block";
});
