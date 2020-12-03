const { accessSync } = require("fs");
const fetch = require("node-fetch");
const url='http://inkfactory.pythonanywhere.com/Validate_Employee/adil@theinkfactory.ca+1234567890';


function help (link) {
fetch(link).then(
  function(data){return data.json()}
)
.then(
  function(json){
    if (json==true){
      var a ="";
      a = json.toString()
      console.log(a)
      if (a =="true"){
        console.log("log em in");
      }
    }
    else{
      console.log("fuck off")
    }
  }
)
}

help(url)
