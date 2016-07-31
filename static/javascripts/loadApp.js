/**
 * Created by irunika on 6/20/16.
 */

$(document).ready(function(){

    var app_id = $('#app-image').attr('app-id');
    var image_url = '/facebook/getResultImage/'+app_id;
    console.log('image_utl :'+ image_url);

    $.get(image_url).done(function(data){
        console.log('data : '+data['imageUrl']);
        $('#app-image').attr('src', data['imageUrl']);

        // var url = $('#facebook-share').attr('href');
        // url = url.replace('######', data['imageUrl']);

        var newUrl = $('#facebook-share-url').attr('href').replace('######', data['imageUrl']);
        $('#facebook-share-url').attr('href', newUrl);

        $('#facebook-share-url').attr('href', newUrl);
        $('#facebook-share-url').show();
        // setTimeout( function () {
        //     console.log('data : '+data['imageUrl']);
        //     $('#app-image').attr('src', data['imageUrl']);
        //     var url = $('#facebook-share').attr('href');
        //     url = url.replace('######', data['imageUrl']);
        //     $('#facebook-share').attr('href', url);
        //     $('#facebook-share').show();
        // }, 3000);
    })
});
