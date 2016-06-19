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
    })
});
