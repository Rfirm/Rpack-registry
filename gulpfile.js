// require main gulp
var gulp = require('gulp');

// require gulp package
// var imagemin = require('gulp-imagemin');
// var recess = require('gulp-recess');
// var cssmin = require('gulp-cssmin');
var less = require('gulp-less');
// var usemin = require('gulp-usemin');
var Combine = require('stream-combiner');
var path = require('path');


// set paths
var paths = {
  styles: ['static/less/**/*.less', '!static/less/**/_*.less'],
  images: 'public/images/**/*',
  fonts: 'public/fonts/**/*',
  bower: 'public/bower_components/**/*'
};
// compile less to css
gulp.task('styles', function () {
  var combined = Combine(
    gulp.src(paths.styles)
    ,less()
    ,gulp.dest('public/stylesheets')

  )
  // any errors in the above streams
  // will get caught by this listener,
  // instead of being thrown:
  combined.on('error', function(err) {
    console.info(err.message)
  });

  return combined;
});

// //minify all css
// gulp.task('cssmin', function() {
//   gulp.src(paths.css_styles)
//     .pipe(cssmin())
//     .pipe(gulp.dest('public/build/stylesheets'));
// });

// // Copy all static images
// gulp.task('images', function() {
//  return gulp.src(paths.images)
//     // Pass in options to the task
//     .pipe(imagemin({optimizationLevel: 5}))
//     .pipe(gulp.dest('public/build/images'));
// });

// gulp.task('fonts', function() {
//   return gulp.src(paths.fonts)
//     .pipe(gulp.dest('public/build/fonts'))
// })

// gulp.task('bower_copy', function() {
//   return gulp.src(paths.bower)
//     .pipe(gulp.dest('public/javascripts/bower_components'))
// })

// Rerun the task when a file changes
gulp.task('watch', function () {
  gulp.watch(paths.styles, ['styles']);
});

// gulp.task('watch-img', function() {
//   gulp.watch(paths.images, ['images']);
// })

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['styles', 'watch']);
// gulp.task('build', ['cssmin', 'images', 'fonts'])
