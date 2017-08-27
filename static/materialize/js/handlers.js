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


function scaleSourceImage()
{

    $('#sourceImage').width($('#imageSlider').val() + '%');
    //image.style.height
}
