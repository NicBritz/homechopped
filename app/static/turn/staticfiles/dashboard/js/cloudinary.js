$(document).ready(function () {
    // src: https://cloudinary.com/documentation/upload_widget
    // upload image to cloudinary
    let myWidget = cloudinary.createUploadWidget({
            cloudName: 'dauzoqnfv',
            uploadPreset: 'zvcpxnbx',
            sources: ['local', 'url', 'image_search', 'dropbox'],
        }, (error, result) => {
            if (!error && result && result.event === "success") {
                // update image and link
                $('#id_header_image_url').val(result.info.secure_url);
                $('#current-image').attr('src', result.info.secure_url);
            }
        }
    );

    document.getElementById("upload_widget").addEventListener("click", function () {
        myWidget.open();
    }, false);

});

