Simple Web Stack

![Image of a simple web stack](0-simple_web_stack.PNG)

Overview
This web infrastructure is a straightforward setup designed to host the website accessible through www.foobar.com. Notably, there are no firewalls or SSL certificates implemented for network security. The server's resources, including CPU, RAM, and SSD, are shared among the various components, such as the database and application server.
Components and Functions
* Server Definition: A server, whether in the form of hardware or software, acts as a provider of services to other computers, referred to as clients.
* Domain Name Significance: The domain name, such as www.foobar.com, serves as a human-friendly alias for an IP address. This mapping is facilitated through the Domain Name System (DNS).
* DNS Record Type: The DNS record for www.foobar.com is an A record, responsible for associating a hostname with its corresponding IPv4 address.
* Web Server Role: The web server, functioning in both HTTP and secure HTTPS, responds to incoming requests with the requested resource or an error message.
* Application Server Purpose: The application server manages and hosts applications and related services for end-users, IT services, and organizations, enabling the hosting and delivery of high-end applications.
* Database Function: The database's role is to organize information systematically, facilitating easy access, management, and updates.
* Client-Server Communication: Communication between the client (user's computer) and the server occurs over the internet network, utilizing the TCP/IP protocol suite.
Infrastructure Challenges
* Single Points of Failure (SPOF): The infrastructure presents multiple SPOFs; for instance, if the MySQL database server experiences downtime, the entire website becomes inaccessible.
* Downtime During Maintenance: Performing maintenance checks on any component or the server itself requires temporary shutdowns, resulting in website downtime due to the single-server nature.
* Limited Scalability: The infrastructure faces challenges in scaling due to its singular server configuration. Increased incoming traffic may exhaust resources or lead to performance slowdowns. Scaling becomes a complex task in such a setup.

