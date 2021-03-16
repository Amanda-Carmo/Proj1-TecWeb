function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});


// function edit1(id, btn) {
//   document.getElementById(id).style.display = "block";
//   // hide the link
//   btn.style.display = 'none';
// }

function edit(className, btn) {
  var x = document.getElementsByClassName(className);
  var i;

  for (i = 0; i < x.length; i++) {
    x[i].style.display = 'block';
  }
  btn.style.display = 'none';
}

// var x = document.getElementsByClassName("xyz");
// var i;
// for (i = 0; i < x.length; i++) {
//     x[i].style.display = 'none';
// }

// var howManycards = document.getElementsByClassName("card").length;
// var cardCollection = document.getElementsByClassName("card");
// for (let i=0; i < howManycards; i++) {
//   cardCollection[i].onclick = function edit1(id, btn) {
  
//   document.getElementById(id).style.display = "block";
//   btn.style.display = 'none';

//   }
// }