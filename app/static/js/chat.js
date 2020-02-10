'use strict';

$(function() {
    $('a#send_message').bind('click', function() {

      $.getJSON('/request_messages', {
        message: $('input[name="text"]').val(),
      }, function(data) {
          //Separate recipes by '_'
          var split_data = data.result.split("_");

          var i;
          for (i=3; i<split_data.length; i+=2){
              // Insert a speech bubble for every recipe id and recipe name
              var recipe = split_data[i] + ' ' + split_data[i+1];
              if (recipe == undefined) break;
              $('#chat_container').append('<div class="bubble" id="' + split_data[i] + '">' + split_data[i+1] + '</div>');
              $('#chat_container').append('<br><br>');
          }
      });

      return false;
    });
  });