// user_onboarding.js

// Function to handle inner tab switching within edit.html
function openInnerTab(evt, tabName) {
    var i, innerTabContent, innerTabLinks;

    // Hide all inner tab contents
    innerTabContent = document.getElementsByClassName("edit-tabcontent");
    for (i = 0; i < innerTabContent.length; i++) {
        innerTabContent[i].style.display = "none";
    }

    // Remove the active class from all inner tab links
    innerTabLinks = document.getElementsByClassName("edit-tablinks");
    for (i = 0; i < innerTabLinks.length; i++) {
        innerTabLinks[i].classList.remove("active");
    }

    // Display the clicked inner tab content and add active class to the button
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classList.add("active");
}

// Initialize the default inner tab on page load for edit.html
document.addEventListener("DOMContentLoaded", function() {
    // Trigger the click event for the default active inner tab within edit.html
    if (document.querySelector(".edit-tablinks.active")) {
        document.querySelector(".edit-tablinks.active").click();
    }
});


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
