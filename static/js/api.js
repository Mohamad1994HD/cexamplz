api = angular.module('api', ['ngResource'])

api.factory('Post', ['$resource', function($resource){
    return $resource('/api/v1/posts/:id',{id:'@id'});
}]);
