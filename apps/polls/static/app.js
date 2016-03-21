angular.module('project', ['restangular', 'ngRoute']).
  config(function($routeProvider, RestangularProvider) {
    $routeProvider.
      when('/', {
        controller:ListCtrl, 
        templateUrl:'list.html'
      }).
      when('/edit/:projectId', {
        controller:EditCtrl, 
        templateUrl:'detail.html',
        resolve: {
          project: function(Restangular, $route){
            return Restangular.one('polls', $route.current.params.projectId).get();
          }
        }
      }).
      when('/new', {controller:CreateCtrl, templateUrl:'detail.html'}).
      otherwise({redirectTo:'/'});

//        RestangularProvider.setUseCannonicalId(true);
//        RestangularProvider.setUseCannonicalId = true;
//      RestangularProvider.setBaseUrl('https://api.mongolab.com/api/1/databases/angularjs/collections');
        RestangularProvider.setRequestSuffix('/');
//        RestangularProvider.setRequestSuffix('\\/');
      RestangularProvider.setBaseUrl('http://127.0.0.1:8000/webservices');
//      RestangularProvider.setDefaultRequestParams({ apiKey: '4f847ad3e4b08a2eed5f3b54' })
//      RestangularProvider.setRestangularFields({
//        id: '_id.$oid'
//      });
      
      RestangularProvider.setRequestInterceptor(function(elem, operation, what) {
        
        if (operation === 'put') {
            console.log(elem);
            console.log(operation);
            console.log(what);
          elem._id = undefined;
          return elem;
        }
        return elem;
      })
  });


function ListCtrl($scope, Restangular) {
   $scope.projects = Restangular.all("polls").getList().$object;
//    console.log($scope.projects);
}


function CreateCtrl($scope, $location, Restangular) {
  $scope.save = function() {
    Restangular.all('polls').post($scope.project).then(function(project) {
      $location.path('/list');
    });
  }
}

function EditCtrl($scope, $location, Restangular, project) {
  var original = project;
  $scope.project = Restangular.copy(original);
  

  $scope.isClean = function() {
    return angular.equals(original, $scope.project);
  }

  $scope.destroy = function() {
    original.remove().then(function() {
      $location.path('/list');
    });
  };

  $scope.save = function() {
    $scope.project.put().then(function() {
      $location.path('/');
    });
  };
}