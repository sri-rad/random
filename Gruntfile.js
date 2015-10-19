module.exports = function(grunt) {

	grunt.initConfig({
		clean: ['dist'],
		copy: {
			dist: {
				files: [{
					expand: true,
					src: ['index.html','jsmain.js','cssmain.css'],
					dest: 'dist/'
				}]
			}
		},
		htmlmin: {
			dist: {
				files: [{
					expand: true,
					cwd: 'dist',
					src: 'index.html',
					dest: 'dist/'
				}],
				options: {
					removeComments: true,
					collapseWhitespace: true,
					removeRedundantAttributes: true
				}
			}
		},
		
		'gh-pages': {
			options: {
				base: 'dist'
			},
			src: ['**']
		}
	});

    grunt.registerTask('build', ['clean', 'copy:dist', 'htmlmin']);

	require('load-grunt-tasks')(grunt);
};
