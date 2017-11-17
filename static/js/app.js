app = angular.module('postApp',['ngRoute', 'ngSanitize', 'api']).
        config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
            $routeProvider.
                when('/', {
                    templateUrl:'static/angular_templates/posts_list.html',
                    controller: 'listCtrl'
                    }).
                when('/problems/:postId', {
                    templateUrl:'static/angular_templates/post_detail.html',
                    controller: 'detailCtrl'
                    }).
                otherwise({redirectTo:'/'});
            
            $locationProvider.html5Mode(true);
        }]);

app.controller('listCtrl', ['$scope', 'Post', function($scope, Post){
    $scope.posts = Post.query(); 
}]);

app.controller('detailCtrl', ['$scope', '$routeParams', 'Post', function($scope, $routeParams, Post){
    console.log($routeParams.postId);
    post_id = $routeParams.postId
    $scope.post = Post.get({id:post_id});
}]);

app.filter('capitalize', function() {
    return function(input) {
      return (!!input) ? input.charAt(0).toUpperCase() + input.substr(1).toLowerCase() : '';
    }
});
