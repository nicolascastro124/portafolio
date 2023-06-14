var jsonPath = "static/json/particles-config.json";
var jsonPath2 = "static/json/particles-config-move-disable.json";
var isMoving = true;
var particlesLoaded = true;

document.addEventListener("DOMContentLoaded", function () {
  particlesJS.load("particles-js", jsonPath);
});

function toggleMode() {
  var icon = document.getElementById("icon-mode");

  if (document.body.classList.contains("light-mode")) {
    document.body.classList.remove("light-mode");
    document.body.classList.toggle("dark-mode");
    icon.classList.remove("fa-moon");
    icon.classList.add("fa-sun");
  } else {
    document.body.classList.remove("dark-mode");
    document.body.classList.toggle("light-mode");
    icon.classList.remove("fa-sun");
    icon.classList.add("fa-moon");
  }
}

function toggleMovement() {
  isMoving = !isMoving;
  var icon = document.getElementById("icon-toggle");

  if (isMoving) {
    particlesJS.load("particles-js", jsonPath);
    icon.classList.remove("fa-person");
    icon.classList.add("fa-person-walking");
  } else {
    particlesJS.load("particles-js", jsonPath2);
    icon.classList.remove("fa-person-walking");
    icon.classList.add("fa-person");
  }
}


function toggleMenu(){
  var menu_links = document.querySelectorAll('.menu-link');
  var icons = document.querySelectorAll('.icon');

  changeDisplay(menu_links, "none", "flex");
  changeDisplay(icons, "none", "flex");
  //changeBackground(elemento)
}


function changeDisplay(elementos,display1,display2){
  /*
  var nav = document.querySelector('nav');
  var links = nav.querySelectorAll('a');
  var linkClasses = links.classList; 
  console.log(linkClasses);
*/
  
  var menu_ul = document.getElementById("menu-ul");

  elementos.forEach(elemento => {
    var estilo = window.getComputedStyle(elemento);
    if(estilo.display === display1){
      elemento.style.display = display2;
      elemento.style.zIndex = 9999;
      menu_ul.classList.remove("menu-color");
      menu_ul.classList.add("menu-color-transparent");
    }else{
      elemento.style.display = display1;
      elemento.style.zIndex = 1;
      menu_ul.classList.remove("menu-color-transparent");
      menu_ul.classList.add("menu-color");

    }
  });

}

function changeBackground(elemento,color){
  elemento.style.backgroundColor = color;
}


function mostrarElementos(dis,dis2) {
  var menu_links = document.querySelectorAll('.menu-link');
  var icons = document.querySelectorAll('.icon');

  // iterar sobre los elementos ocultos y cambiar su display a flex
  menu_links.forEach(elemento => {
    var estilo = window.getComputedStyle(elemento);
    if(estilo.display === dis){
      elemento.style.display = dis2;
    }
  });
  icons.forEach(elemento => {
    var estilo = window.getComputedStyle(elemento);
    if(estilo.display === dis){
      elemento.style.display = dis2;
    }
  });

}

window.addEventListener("resize", function() {
  var menu_ul = document.getElementById("menu-ul");

  if (window.innerWidth > 768) {
    mostrarElementos("none","flex")

  }else{
    mostrarElementos("flex","none")
    menu_ul.classList.remove("menu-color-transparent");
    menu_ul.classList.add("menu-color");
  }
});




