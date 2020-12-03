const fetch = require("node-fetch");
fetch("http://inkfactory.pythonanywhere.com/Validate_Employee/taiseer142@hotmail.com+56Operahouse")
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    console.log(myJson.ip);
  })
  .catch(function (error) {
    console.log("Error: " + error);
  });