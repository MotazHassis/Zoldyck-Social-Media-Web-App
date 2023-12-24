


// -------------
// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()


// // popover
// var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
// var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
//   return new bootstrap.Popover(popoverTriggerEl);
// });

// // Gender Select
// if (window.location.pathname === "/") {
//   const radioBtn1 = document.querySelector("#flexRadioDefault1");
//   const radioBtn2 = document.querySelector("#flexRadioDefault2");
//   const radioBtn3 = document.querySelector("#flexRadioDefault3");
//   const genderSelect = document.querySelector("#genderSelect");

//   radioBtn1.addEventListener("change", () => {
//     genderSelect.classList.add("d-none");
//   });
//   radioBtn2.addEventListener("change", () => {
//     genderSelect.classList.add("d-none");
//   });
//   radioBtn3.addEventListener("change", () => {
//     genderSelect.classList.remove("d-none");
//   });
// }

