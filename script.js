$(document).ready(function () {
  // set the image-map width and height to match the img size
  $("#image-map").css({
    width: $("#image-map img").width(),
    height: $("#image-map img").height()
  });

  //tooltip direction
  var tooltipDirection;

  for (i = 0; i < $(".pin").length; i++) {
    // set tooltip direction type - up or down
    if ($(".pin").eq(i).hasClass("pin-down")) {
      tooltipDirection = "tooltip-down";
    } else {
      tooltipDirection = "tooltip-up";
    }

    // append the tooltip
    $("#image-map").append(
      "<div style='left:" +
        $(".pin").eq(i).data("xpos") +
        "px;top:" +
        $(".pin").eq(i).data("ypos") +
        "px' class='" +
        tooltipDirection +
        "'>\
                                            <div class='tooltip'>" +
        $(".pin").eq(i).html() +
        "</div>\
                                    </div>"
    );
  }

  // show/hide the tooltip
  $(".tooltip-up, .tooltip-down")
    .mouseenter(function () {
      $(this).children(".tooltip").fadeIn(100);
    })
    .mouseleave(function () {
      $(this).children(".tooltip").fadeOut(100);
    });
});
function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
$(document).ready(function CreateTableFromJSON() {
  var results = [
    {
      Класс: "6А",
      Балл: "125"
    },
    {
      Класс: "6Б",
      Балл: "56"
    }
  ];

  var col = [];
  for (var i = 0; i < results.length; i++) {
    for (var key in results[i]) {
      if (col.indexOf(key) === -1) {
        col.push(key);
      }
    }
  }

  var table = document.createElement("table");
  var tr = table.insertRow(-1);

  for (var i = 0; i < col.length; i++) {
    var th = document.createElement("th");
    th.innerHTML = col[i];
    tr.appendChild(th);
  }

  for (var i = 0; i < results.length; i++) {
    tr = table.insertRow(-1);

    for (var j = 0; j < col.length; j++) {
      var tabCell = tr.insertCell(-1);
      tabCell.innerHTML = results[i][col[j]];
    }
  }
  var divContainer = document.getElementById("showData");
  divContainer.innerHTML = "";
  divContainer.appendChild(table);
});
