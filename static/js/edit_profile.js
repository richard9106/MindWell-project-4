let first_name = document.getElementById("id_first_name");
let last_name = document.getElementById("id_last_name");
let my_location = document.getElementById("id_location");
let email = document.getElementById("id_email");
let profession = document.getElementById("id_profession");
let description = document.getElementById("id_description");



let edit_profile_button = document.getElementById("edit_profile_button");

edit_profile_button.addEventListener("click", function () {

 

  let first_name_content = document.getElementById("first_name").textContent
  let my_last_name_content = document.getElementById("Last_name_id").textContent
  let location_content = document.getElementById("location").textContent
  let email_content = document.getElementById("email").textContent
  let profession_content = document.getElementById("profession").textContent
  let description_content = document.getElementById("description").textContent

  console.log(my_last_name_content);
  console.log(last_name);

  first_name.value = first_name_content;
  last_name.value = my_last_name_content;
  my_location.value = location_content;
  email.value = email_content;
  profession.value = profession_content;
  description.value = description_content;
});
