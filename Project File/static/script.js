// ========================================
// OptiCrop JavaScript
// ========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("OptiCrop Loaded Successfully");

    // Form Validation
    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", function (event) {

            const inputs = form.querySelectorAll("input");

            for (let input of inputs) {

                if (input.hasAttribute("required")) {

                    if (input.value.trim() === "") {

                        alert("Please fill all required fields.");

                        event.preventDefault();

                        return;
                    }
                }

                // Validate Numeric Inputs

                if (input.type === "number") {

                    let value = parseFloat(input.value);

                    if (isNaN(value)) {

                        alert("Please enter valid numeric values.");

                        event.preventDefault();

                        return;
                    }

                }

            }

        });

    });

});


// ========================================
// Reset Form
// ========================================

function resetForm() {

    const form = document.querySelector("form");

    if (form) {

        form.reset();

    }

}


// ========================================
// Show Loading
// ========================================

function showLoading(button) {

    button.disabled = true;

    button.innerHTML =
        "Predicting...";

}


// ========================================
// Hide Loading
// ========================================

function hideLoading(button) {

    button.disabled = false;

    button.innerHTML =
        "Predict Crop";

}


// ========================================
// Validate pH
// ========================================

function validatePH(value) {

    if (value < 0 || value > 14) {

        alert("pH value should be between 0 and 14.");

        return false;

    }

    return true;

}


// ========================================
// Validate Temperature
// ========================================

function validateTemperature(value) {

    if (value < -10 || value > 60) {

        alert("Temperature must be between -10°C and 60°C.");

        return false;

    }

    return true;

}


// ========================================
// Validate Rainfall
// ========================================

function validateRainfall(value) {

    if (value < 0) {

        alert("Rainfall cannot be negative.");

        return false;

    }

    return true;

}


// ========================================
// Display Success Message
// ========================================

function showSuccess(message) {

    alert(message);

}


// ========================================
// Display Error Message
// ========================================

function showError(message) {

    alert(message);

}