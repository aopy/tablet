/* Lavalamp Menu jQuery-Funktionen */

$(document).ready(function(){

    $('.floatr').each(function() {
        var $this = $(this), $parent, $active;

        $parent = $(this).closest('.lavalamp');
        $active = $parent.find('li.active');

        //macht die Position des floatr Elements gleich wie die aktuelle Position des active Elements
        $this.css({
            "left": $active.offset().left - $parent.offset().left + "px",
            "width": $active.width() + "px"
        });
    });

    $('.lavalamp').delegate('li', 'mouseenter mouseleave click', function(e) {
        var type = e.type,
            $this = $(this), left, width;
        
        //wenn die Maus über ein Menu-Element ist, macht das die neue Position des floatr Elements
        if (type === 'mouseenter') {
            left = $this.offset().left - ($this.closest('.lavalamp').offset().left);
            width = $this.width();

            $this.closest('ul').next('div.floatr').css({
                "width": width + "px",
                "left": left + "px"
            });
          
        //wenn die Maus das Menu verlässt, setzt den floatr Element zu das aktive Element zurück
        } else if (type === 'mouseleave') {

            left = $this.siblings('li.active').offset().left - ($this.closest('.lavalamp').offset().left);
            width = $this.siblings('li.active').width();

            $this.closest('ul').next('div.floatr').css({
                "width": width + "px",
                "left": left + "px"

            });
          
       //wenn der User auf ein Menu-Element klickt, macht das das neue active Element 
        } else if (type === 'click') {
            
              $this.addClass('active').siblings('li').removeClass('active');

              return true;
        }
    });
});
