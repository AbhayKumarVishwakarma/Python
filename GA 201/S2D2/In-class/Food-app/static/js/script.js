// Establish a WebSocket connection
        var socket = io.connect('http://localhost:8000');
        console.log("xxxxx")

        // Handle initial orders event
        socket.on('initial_orders', function(orders) {
            // Update the orders on the page
            updateOrders(orders);
        });

        // Handle order update event
        socket.on('order_update', function(orders) {
            // Update the orders on the page
            updateOrders(orders);
        });

        // Function to update the orders on the page
        function updateOrders(orders) {
            // Update the order status for each order
            orders.forEach(function(order) {
                var orderElement = document.getElementById('order-' + order.id);
                console.log("-----")
                if (orderElement) {
                    orderElement.innerHTML = order.status;
                }
            });
        }