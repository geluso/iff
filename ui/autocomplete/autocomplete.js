'use strict';

function AutoCompleteCtrl($scope) {
	$scope.terms = ["cheese", "wine", "bread"];

	$scope.addTerm = function() {
		$scope.terms.push($scope.termToAdd);
		$scope.termToAdd = '';
	}
}
