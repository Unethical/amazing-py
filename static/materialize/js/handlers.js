function ReadURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#sourceImage')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);

    }
}

function ScaleSourceImage(image, scalar)
{
    //image.style.height
}
