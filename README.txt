This application is the Course Project for CSC 122 Network and Web Programming.

This application utilizes Flask and Postgres to create a web server that relies on a database.

The web server is of a convenience store that my parents own. On the web server, there are 5 main pages: home, About, Contact, Menu, and Admin.

The first 3 pages, Home, About, and Contact are static web pages that display relevant information about the convenience store. The last 2 pages are how the user can interact with the web server.

The menu page displays that database that is utilizes for this application. The database is a representation of the menu items in the Deli. The user is able to filter the menu based on what type of item they want. They are able to filter by 'All', 'Burgers', 'Sandwiches', "Salads", "Appetizers", "Subs", and "Fried Chicken".

The admin page allows the user to add new items or delete items from the database.

Adding new items prompts the user for a name, price, category, and toppings for the thing. The toppings are optional as only some categories need toppings. Appetizers, for instance, do not have toppings.

This application has been deployed on Azure but can also be run locally.

Author: Jade Harbert