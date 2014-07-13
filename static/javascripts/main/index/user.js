require(["./config"], function(config) {

  require([
    'jquery',
    'backbone',
    'marionette',
    'underscore',
    ], function ($, Backbone, Marionette, _){
        var User = new Marionette.Application();
        // User.on("initialize:after", function(){
        //     console.log("hi");
        // });


        User.start();
    });
})

