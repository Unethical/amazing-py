var mMazeStart, mMazeEnd = null;

function ReadURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#sourceImage')
                .attr('src', e.target.result);
            $('#sourceImage')
                .show();
            $('#sliderContainer')
                .show();
        };

        reader.readAsDataURL(input.files[0]);

    }
}

function scaleSourceImage() {
    $('#sourceImage').width($('#imageSlider').val() + '%');
}



$('#sourceImage').click(function(e)
{
    var offset_t = $(this).offset().top - $(window).scrollTop();
    var offset_l = $(this).offset().left - $(window).scrollLeft();

    var left = Math.round( (e.clientX - offset_l) );
    var top = Math.round( (e.clientY - offset_t) );

    alert("Left: " + left + " Top: " + top);

});
