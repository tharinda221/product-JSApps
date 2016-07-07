/**
 * Created by irunika on 6/20/16.
 */

$(document).ready(function(){

    var app_id = $('#app-image').attr('app-id');
    var image_url = '/facebook/getResultImage/'+app_id;
    console.log('image_utl :'+ image_url);

    $.get(image_url).done(function(data){
        // var facebookHref = $('#facebook-share').attr('href');
        // facebookHref = facebookHref.replace('######', data['imageUrl']);
        // $('#facebook-share').attr('href', facebookHref);
        setTimeout( function () {
            console.log('data : '+data['imageUrl']);
            $('#app-image').attr('src', data['imageUrl']);
            var url = $('#facebook-share').attr('href');
            url = url.replace('######', data['imageUrl']);
            $('#facebook-share').attr('href', url);
            $('#facebook-share').show();
        }, 1000);
    })
});
