window.onload=function(){alert('Bienvenido a esta pagina');}

      

function hora() {
    var DateString=(new Date()).toString();
    self.status=DateString.substring(0,3+DateString.lastIndexOf(':'))+
    "Cualquier mensaje";
    setTimeout("hora()",200);}
hora()



function ajustarPie() {
    var winH = $(window).height();
    var docH = $("body").height();
    var pieH = $("footer").height();
    
    if (docH + pieH < winH) {
      $("footer").attr("class", "bottom");
      } else {
        $("footer").attr("class", "");
        }
    }
  
  $(document).ready(ajustarPie);
  $(window).on("resize", ajustarPie);

