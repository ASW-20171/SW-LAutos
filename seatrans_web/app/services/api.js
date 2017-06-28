app
    .factory("API", function($resource, config) {
    var url = config.tutoriaUrl;
    return {

        //Eje
        Asiento: $resource(url + "asientos/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: false, params: { query: '@query', page: '@page', page_size: '@page_size' } }
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }),
        //Eje

        //Periodo
        Cliente: $resource(url + "clientes/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: true, params: { query: '@query' } }
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }), 
        //Periodo

        //Test

        Destino: $resource(url + "destinos/:id/", { 'id': '@id' }, {
            //"update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: true, params: { query: '@query' } }
            "update": { method: 'PUT' },
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }),
        //Test

        //Dimensiones
        Origen: $resource(url + "origens/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: false, params: { query: '@query', page: '@page', page_size: '@page_size' } }
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }),
        //Dimensiones

         //Evaluacion
        Reserva: $resource(url + "reservas/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: true, params: { query: '@query' } }
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }),
        //Evaluacion

        //Categoria
        Pago: $resource(url + "pagos/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            //"list": { method: 'GET', isArray: true, params: { query: '@query' } }
            "list": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results: angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options:{"count":1,"pages":1,"page":1,"per":1,"range":"all",
                    "previous":null,"page_size":1,"next":null};
                    return { results: results, options: options };
                }
            },
            "options": {
                method: 'OPTIONS',
                isArray: false,
                transformResponse: function(r) {
                    return angular.fromJson(r).actions.POST;
                }
            }
        }),
        //Categoria
    };
});



