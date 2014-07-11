require.config({
    baseUrl: '/static/javascripts/',

    paths: {
        'jquery'                         : 'bower_components/jquery/jquery.min',
        'backbone'                       : 'bower_components/backbone/backbone',
        'marionette'                     : 'bower_components/marionette/lib/backbone.marionette.min',
        'underscore'                     : 'bower_components/underscore/underscore',
        'backbone.marionette.handlebars' : 'bower_components/backbone.marionette.handlebars/backbone.marionette.handlebars.min'
    },

    shim:{
        'underscore': {
            exports: '_'
        },

        'backbone': {
            deps: ['jquery', 'underscore'],
            exports: 'Backbone'
        },

        'backbone.marionette': {
            deps: ['jquery', 'backbone', 'underscore'],
            exports: 'Marionette'
        },

        'backbone.marionette.handlebars': {
            deps: ['jquery', 'backbone', 'underscore', 'backbone.marionette']
        }

    }
});