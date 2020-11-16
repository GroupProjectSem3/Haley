(function() {

    var db = {

        loadData: function(filter) {
            return $.grep(this.clients, function(client) {
                return (!filter.Name || client.Name.indexOf(filter.Name) > -1)
                    && (!filter.Specialization  || client.Specialization.indexOf(filter.Specialization)> -1)
                    && (!filter.Address || client.Address.indexOf(filter.Address) > -1)
                    && (!filter.contact || client.contact.indexOf(filter.contact) > -1);
            });
        },

        insertItem: function(insertingClient) {
            this.clients.push(insertingClient);
        },

        updateItem: function(updatingClient) { },

        deleteItem: function(deletingClient) {
            var clientIndex = $.inArray(deletingClient, this.clients);
            this.clients.splice(clientIndex, 1);
        }

    };

    window.db = db;


    db.countries = [
        { Name: "", Id: 0 },
        { Name: "United States", Id: 1 },
        { Name: "Canada", Id: 2 },
        { Name: "United Kingdom", Id: 3 },
        { Name: "France", Id: 4 },
        { Name: "Brazil", Id: 5 },
        { Name: "China", Id: 6 },
        { Name: "Russia", Id: 7 }
    ];

    db.clients = [
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
        {
            "Name": "Otto Clay",
            "Specialization": "Heart",
            "Address": "Ap #897-1459 Quam Avenue",
             "contact":"+353 851234560"
        },
    ];
}());